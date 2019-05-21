PANDOC=pandoc
LATEX2PDF=pdflatex
BIBER=biber

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/src
TEMPLATE=$(BASEDIR)/templates/thesis.latex

SRC_FILES := $(wildcard gfx/*/*.pdf)
SVG_FILES := $(patsubst gfx/%.pdf, gfx/%.svg,$(SRC_FILES))
PNG_FILES := $(patsubst gfx/%.svg, gfx/%.png,$(SVG_FILES))


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
	--variable=commit:$(LAST_COMMIT) \
	--include-before-body=before.tex --verbose

svg_images: $(SVG_FILES)

png_images: $(PNG_FILES)

gfx/%.svg: gfx/%.pdf
	pdf2svg $< $@

gfx/%.png: gfx/%.svg
	convert $< $@

thesis.html: Makefile templates/gitbook.html src/*.md src/*.bib filters/*.py
	$(PANDOC) "$(INPUTDIR)"/latex_macros.md \
	"$(INPUTDIR)"/000_title_page.md \
  "$(INPUTDIR)"/001_abstract.md \
	"$(INPUTDIR)"/10[1-7]_chapter_*.md \
	 --filter=pandoc-crossref --filter=pandoc-citeproc \
	 --number-sections \
	 -M "linkReferences:true" \
	 --top-level-division=chapter \
	-s --mathjax -o thesis.html \
	--template templates/gitbook.html \
	--section-divs --write=html4 \
	-F panflute

before: src/00[1-3]_*.md
	$(PANDOC) $^ \
	--top-level-division=chapter \
	-o before.tex

gfx/%.pdf: gfx/%.tex
	$(LATEX2PDF) -output-directory $(dir $@) $^

clean:
	rm -f *.pdf *.out *aux *bbl *blg *log *toc \
	      *.ptb *.tod *.fls *.fdb_latexmk *.lof	


.PHONY: pdf
