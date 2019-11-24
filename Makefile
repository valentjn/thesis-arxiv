LATEX = max_print_line=10000 error_line=254 half_error_line=238 \
	python3 tools/filterOutput.py pdflatex thesis.tex
BIBER = biber thesis
GLOSSARY = python3 tools/buildGlossary.py -q -o thesis.gls thesis

fromScratch:
	$(LATEX) && $(BIBER) && $(GLOSSARY) && \
	$(LATEX) && $(GLOSSARY) && \
	$(LATEX) && $(GLOSSARY) && \
	$(LATEX)

fromRepo:
	$(LATEX) && $(LATEX) && $(LATEX)

archive:
	git ls-files gfx/ tex/ 00README.XXX thesis.bbl thesis.gls thesis.tex | \
	xargs tar -czvf arxiv.tar.gz
