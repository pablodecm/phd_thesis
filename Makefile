PANDOC=pandoc
LATEX2PDF=pdflatex
BIBER=biber

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src
TEMPLATE=$(BASEDIR)/templates/default.latex


pdf: latex
	$(LATEX2PDF) "$(INPUTDIR)"/thesis.tex
	$(BIBER) thesis.bcf
	$(LATEX2PDF) "$(INPUTDIR)"/thesis.tex

	
latex:
	$(PANDOC) "$(INPUTDIR)"/*.md -s \
	--template "$(TEMPLATE)" \
	-o "$(INPUTDIR)"/thesis.tex --filter=pandoc-crossref \
	--filter=pandoc-citeproc --biblatex \
	--top-level-division=chapter \
	--verbose
		

.PHONY: pdf
