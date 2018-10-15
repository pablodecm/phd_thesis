PANDOC=pandoc
LATEX2PDF=pdflatex
BIBER=biber

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src
TEMPLATE=$(BASEDIR)/templates/thesis.latex

LAST_COMMIT := $(shell git rev-parse HEAD)

pdf: latex
	$(LATEX2PDF) thesis.tex
	$(BIBER) thesis.bcf
	$(LATEX2PDF) thesis.tex

	
latex:
	$(PANDOC) "$(INPUTDIR)"/0[0-1]0_*.md \
	"$(INPUTDIR)"/10*.md -s \
	--template "$(TEMPLATE)" \
	-o thesis.tex --filter=pandoc-crossref \
	--filter=pandoc-citeproc --biblatex \
	--top-level-division=chapter \
	--variable=draft:true \
	--variable=commit:$(LAST_COMMIT) \
	--verbose
		

.PHONY: pdf
