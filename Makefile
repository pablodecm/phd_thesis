PANDOC=pandoc

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src
TEMPLATE=$(BASEDIR)/templates/default.latex


pdf:
	pandoc "$(INPUTDIR)"/*.md \
	-o "thesis.pdf" \
	--template "$(TEMPLATE)" \
  --top-level-division=chapter \
	--number-sections \
	--verbose

.PHONY: pdf
