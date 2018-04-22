PANDOC=pandoc

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src

pdf:
	pandoc "$(INPUTDIR)"/*.md \
	-o "thesis.pdf" \
--top-level-division=chapter \
	--verbose

.PHONY: pdf
