""" 
Panflute filter that creates a toc for the gitbook template
"""

import panflute as pf
import sys

def prepare(doc):
  doc.toc_list = pf.BulletList()
  doc.toc_depth = int(doc.get_metadata('toc-depth', default=1))

def action(elem, doc):
  if isinstance(elem, pf.Header) and elem.level <= doc.toc_depth:
    item = pf.ListItem(pf.Plain(*elem.content))
    doc.toc_list.content.append(item)
    

def finalize(doc):
  toc_html = pf.convert_text(doc.toc_list,
                  input_format="panflute",
                  output_format="html")
  doc.metadata["toc_html"] = pf.RawBlock(toc_html,format="html")
  md = doc.get_metadata("title")
  pf.debug(type(toc_html),toc_html)
  del doc.toc_list, doc.toc_depth
  
def main(doc=None):
  return pf.run_filter(action,
                       prepare=prepare,
                       finalize=finalize,
                       doc=doc) 

if __name__ == '__main__':
    main()