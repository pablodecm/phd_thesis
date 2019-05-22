""" 
Panflute filter that compiles latex tables and adds them in as SVGs
with adecuate caption and links
"""

import panflute as pf
import re
import hashlib
import sys
import subprocess
import os

# double braces will be substituted by single by .format
template_standalone = r"""
\documentclass[a4paper]{{standalone}}

\usepackage{{booktabs}}
\begin{{document}}

  \minipage{{1.3\textwidth}}

  \centering
  \small
  
  {tabular}

  \endminipage
\end{{document}}
""" 

def tex_to_svg(f_name):
  
  pdf_f_name = f_name.replace(".tex",".pdf")
  output_dir = os.path.dirname(pdf_f_name)
  subprocess.call(["pdflatex", "-output-directory",
                   output_dir,f_name], stdout=sys.stderr)
  svg_f_name = f_name.replace(".tex",".svg")
  subprocess.call(["pdf2svg", f_name.replace(".tex",".pdf"),
                   svg_f_name], stdout=sys.stderr)
  return svg_f_name
  
def prepare(doc):
  pass

def action(elem, doc):
  if isinstance(elem, pf.RawBlock) and elem.format=="tex":
    text = elem.text
    # check if tabular
    tab_pattern = r"\\begin{tabular}.+\\end{tabular}"
    tab_result = re.search(tab_pattern,text, flags=re.DOTALL)
    # check if table with external tabular
    table_pattern = r"\\begin{table}.+\\end{table}"
    table_result = re.search(table_pattern,text, flags=re.DOTALL)
    input_pattern = r"\\input{.+}"
    input_result = re.search(input_pattern,text)
    # get caption and label
    caption_pattern = r"\\caption{(.+)}" 
    caption_result = re.search(caption_pattern,text, flags=re.DOTALL)
    label_pattern = r"\\label{(.+)}" 
    label_result = re.search(label_pattern,text)
    if tab_result:
      text_latex = template_standalone.format(tabular=tab_result.group())
    elif table_result and input_result:
      text_latex = template_standalone.format(tabular=input_result.group())
    else:
      # do no no anything if not table found
      return None
    # name is either sanitized label or hash of text
    if label_result:
      f_name = "{}.tex".format(label_result.group(1)) \
                       .replace("table:","").replace("tab:","")
    else:
      f_name = "{}.tex".format(hashlib.sha1(text.encode()).hexdigest())
    # set path for the file and write
    f_name = "src/{}".format(f_name)
    with open(f_name,"w") as f:
      f.write(text_latex)
    svg_f_name = tex_to_svg(f_name)
    
    return pf.Para(pf.Image(url=svg_f_name))
      
    

def finalize(doc):
  pass
  
def main(doc=None):
  return pf.run_filter(action,
                       prepare=prepare,
                       finalize=finalize,
                       doc=doc) 

if __name__ == '__main__':
    main()