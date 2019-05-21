""" 
Panflute filter that substitutes all PDF images by their SVG transform, which
was created using pdf2svg in the make file
"""

import panflute as pf

def prepare(doc):
  pass

def action(elem, doc):
  if isinstance(elem, pf.Image):
    elem.url = elem.url.replace(".pdf",".png")

def finalize(doc):
  pass
  
def main(doc=None):
  return pf.run_filter(action,
                       prepare=prepare,
                       finalize=finalize,
                       doc=doc) 

if __name__ == '__main__':
    main()