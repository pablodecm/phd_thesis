""" 
Panflute filter that substitutes all PDF images by their SVG transform, which
was created using pdf2svg in the make file
"""

from panflute import *

def action(elem, doc):
    if isinstance(elem, Image):
        elem.url = elem.url.replace(".pdf",".png")

def main(doc=None):
    return run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()