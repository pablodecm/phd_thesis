"""
Splits the resulting HTML file from using the pandoc gitbook template over
several smaller files based on the the section and subsection
"""

from lxml import etree
import lxml.html
from slugify import slugify
import re
from pathlib import Path
import copy
import json

input_file = "thesis.html"
# parse HTML as a tree and remove extra text and comments
parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True)
html_et = etree.parse(input_file, parser=parser)
# this will return the basic root element of the tree
html_el = html_et.getroot()

# get header and footnotes
header_el = html_el.cssselect("#header")[0]
footnotes_el = html_el.cssselect(".footnotes")[0]
# all text content is within the section element
section_el = html_el.cssselect("section")[0]

# we can get all the level 1 section divs (and their h1 field)
div_l1_els = section_el.cssselect(".section.level1")

# to save all the slugs name and their content
slug_content = {}
slug_title = {}
slug_content["index"] = header_el
slug_title["index"] = "Statistical Learning and Inference at Particle Collider Experiments"
section_el.remove(header_el)
section_el.remove(footnotes_el)

# this is list to keep the relative order of the different splits
order_slugs = ["index"]

for div_l1_el in div_l1_els:
  h1_el = div_l1_el.cssselect("h1")[0]
  # get text representation of header text
  h1_text = lxml.html.tostring(h1_el,method="text")
  h1_slug = slugify(h1_text)
  order_slugs.append(h1_slug)

  # add level1 slug to content (now to keep the order)
  slug_content[h1_slug] = div_l1_el
  slug_title[h1_slug] = str(h1_text)
  section_el.remove(div_l1_el)

  # we can get all the level 2 section divs in each div
  div_l2_els = div_l1_el.cssselect(".section.level2")
  for div_l2_el in div_l2_els:
    h2_el = div_l2_el.cssselect("h2")[0]
    # get text representation of header text
    h2_text = lxml.html.tostring(h2_el,method="text")
    h2_slug = slugify(h2_text)
    order_slugs.append(h2_slug)
    # add content to dict and remove
    slug_content[h2_slug] = div_l2_el
    slug_title[h2_slug] = str(h2_text)
    div_l1_el.remove(div_l2_el)

# now for each slug get all ids and add the slug name to a dict
ids_slug_name = {}
slug_footnotes = {}
# this is to filter footnote refs
fn_regex = re.compile(r'#fn[\d]+')
for slug_name, slug_el in slug_content.items():
  # get all ids in slug
  slug_ids = slug_el.xpath('.//*[@id]/@id')
  for slug_id in slug_ids: ids_slug_name[slug_id] = slug_name
  # do not forget the id of the slug element if it exists
  if "id" in slug_el.attrib: ids_slug_name[slug_el.attrib["id"]] = slug_name
  # get footnotes of the slug and their ids
  slug_hrefs = slug_el.xpath('.//*[@href]/@href')
  fn_hrefs = filter(fn_regex.search, slug_hrefs)
  slug_footnotes[slug_name] = []
  for fn_href in fn_hrefs:
    fn_el = footnotes_el.cssselect(fn_href)[0]
    slug_footnotes[slug_name].append(fn_el)
    fn_ids = [fn_el.attrib["id"]]+ fn_el.xpath('.//*[@id]/@id')
    for fn_id in fn_ids: ids_slug_name[fn_id] = slug_name

# now we create an element tree for each of the slugs
# fix the hrefs and write it to file
path = Path("./html_output")
path.mkdir(exist_ok=True)
slug_name_t = "{}.html"
# this counter is to preserve document wise
fn_counter = 0
# this is a list that will be used to create a search index
search_index = []
for slug_name, slug_el in slug_content.items():
  # make a copy of the element tree
  et = copy.deepcopy(html_et)
  # get section element
  section_el = et.getroot().cssselect("section")[0]
  # append the slug element to the section
  section_el.append(slug_el)

  # add footnotes to slug if there are (make copy)
  if (slug_name in slug_footnotes) and (len(slug_footnotes[slug_name])>0):
    fn_counter += len(slug_footnotes[slug_name])
    footnotes_slug_el = copy.deepcopy(footnotes_el)
    footnotes_ol_el = footnotes_slug_el.cssselect("ol")[0]
    footnotes_ol_el.set("start",str(fn_counter))
    for el in footnotes_ol_el: footnotes_ol_el.remove(el)
    for el in slug_footnotes[slug_name]: footnotes_ol_el.append(el)
    section_el.append(footnotes_slug_el)

  # fix all the internal hrefs
  slug_href_els = et.getroot().xpath('.//*[@href]')
  for slug_href_el in slug_href_els:
    int_href_pattern = r"#(.+)"
    int_href_result = re.match(int_href_pattern, slug_href_el.attrib["href"])
    if int_href_result:
      curr_id = int_href_result.group(1)
      if curr_id in ids_slug_name:
        new_id = slug_name_t.format(ids_slug_name[curr_id]) + "#" + curr_id
        slug_href_el.attrib["href"] =  new_id

  # fix the data paths for the search index function
  summary_el = et.getroot().cssselect(".summary")[0]
  for toc_li_el in summary_el.cssselect(".chapter"):
    if "data-path" in toc_li_el.attrib:
      href_all = toc_li_el[0].attrib["href"]
      href_result = re.match(r"(.+\.html)", href_all)
      if href_result:
        toc_li_el.attrib["data-path"] = href_result.group(1)
        data_level = toc_li_el.attrib['data-level']
        # change to file href if unnumbered or up to two level header
        if (data_level=="") or re.match(r"\d+$",data_level) or re.match(r"\d+\.\d+$",data_level):
          toc_li_el[0].set("href", href_result.group(1))

  # the next/prev element will be at the end of the book body
  book_body_el = et.getroot().cssselect(".book-body")[0]
  # add next and previous buttons to page
  slug_index = order_slugs.index(slug_name)
  has_prev = slug_index!=0
  has_next = slug_index!=(len(order_slugs)-1)
  if has_next:
    a_href = "{}.html".format(order_slugs[slug_index+1])
    a_cls = ["navigation", "navigation-next"]
    if not has_prev: a_cls += ["navigation-unique"]
    a_next = """<a href="{a_href}" class="{a_class}" aria-label="Next page">
                <i class="fa fa-angle-right"></i></a>"""
    a_next = a_next.format(a_href=a_href,a_class=" ".join(a_cls))
    next_el = lxml.html.fromstring(a_next)
    book_body_el.append(next_el)
  if has_prev:
    a_href = "{}.html".format(order_slugs[slug_index-1])
    a_cls = ["navigation", "navigation-prev"]
    if not has_next: a_cls += ["navigation-unique"]
    a_prev = """<a href="{a_href}" class="{a_class}" aria-label="Previous page">
                <i class="fa fa-angle-left"></i></a>"""
    a_prev = a_prev.format(a_href=a_href,a_class=" ".join(a_cls))
    prev_el = lxml.html.fromstring(a_prev)
    book_body_el.append(prev_el)
  

  search_index.append([slug_name_t.format(slug_name), slug_title[slug_name],
                      lxml.html.tostring(section_el, encoding="unicode",method="text")])

  # write to file
  file_name = path / slug_name_t.format(slug_name)
  with open(file_name,"wb") as f:
    et.write(f, encoding="utf-8", method="html")

# write also search index to file
index_file_name = path / "search_index.json"
with open(index_file_name, "w") as f:
  json.dump(search_index, f,ensure_ascii=True, indent=2)