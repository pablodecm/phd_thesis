""" 
Panflute filter that changes epigraphs for blockquotes
"""

import panflute as pf
import re

def prepare(doc):
  pass

def action(elem, doc):
  if isinstance(elem, pf.RawBlock) and elem.format=="tex":
    pattern = r"\\epigraph{(.+)}{(.+)}"
    text = elem.text
    result = re.search(pattern,text, flags=re.DOTALL)
    if result:
      quote = result.group(1)
      # remove double of triple spaces and next lines
      quote = quote.replace(r"\n","").replace(r"\\","")
      quote = quote.replace("   "," ").replace("  "," ")
      author = result.group(2)
      text = (">{} \n"
              ">\n"
              ">-- {}").format(quote, author)
      return pf.convert_text(text,output_format="panflute")
    else:
      pass
      
    

def finalize(doc):
  pass
  
def main(doc=None):
  return pf.run_filter(action,
                       prepare=prepare,
                       finalize=finalize,
                       doc=doc) 

if __name__ == '__main__':
    main()