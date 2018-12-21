PANDOC=pandoc
LATEX2PDF=pdflatex
BIBER=biber

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src
TEMPLATE=$(BASEDIR)/templates/thesis.latex

LAST_COMMIT := $(shell git rev-parse HEAD)

pdf: thesis.tex
	$(LATEX2PDF) thesis.tex
	$(BIBER) thesis.bcf
	$(LATEX2PDF) thesis.tex

	
thesis.tex: src/*.md before gfx/101_chapter_1/mexican_hat.pdf gfx/104_chapter_4/neural_network.pdf
	$(PANDOC) "$(INPUTDIR)"/latex_macros.md \
	"$(INPUTDIR)"/0[0-1]0_*.md \
	"$(INPUTDIR)"/10*.md -s \
	--template "$(TEMPLATE)" \
	-o thesis.tex --filter=pandoc-crossref \
	--biblatex \
	--top-level-division=chapter \
	--variable=draft:false \
	--variable=commit:$(LAST_COMMIT) \
	--include-before-body=before.tex --verbose

before: src/00[1-2]_*.md
	$(PANDOC) $^ \
	--top-level-division=chapter \
	-o before.tex

gfx/%.pdf: gfx/%.tex
	$(LATEX2PDF) -output-directory $(dir $@) $^

clean:
	rm -f *.pdf *.out *aux *bbl *blg *log *toc \
	      *.ptb *.tod *.fls *.fdb_latexmk *.lof	


.PHONY: pdf
