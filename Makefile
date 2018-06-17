PANDOC=pandoc

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src
TEMPLATE=$(BASEDIR)/templates/default.latex


pdf:
	pandoc "$(INPUTDIR)"/*.md \
	-F pandoc-crossref \
	-o "thesis.pdf" \
	--template "$(TEMPLATE)" \
  --top-level-division=chapter \
	--verbose

.PHONY: pdf
