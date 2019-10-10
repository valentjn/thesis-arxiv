LATEX = max_print_line=10000 error_line=254 half_error_line=238 \
	python3 ../tools/filterOutput.py pdflatex thesis.tex
BIBER = biber thesis
GLOSSARY = python3 ../tools/buildGlossary.py -q -o thesis.gls thesis

fromScratch:
	cd tex && \
	$(LATEX) && $(BIBER) && $(GLOSSARY) && \
	$(LATEX) && $(GLOSSARY) && \
	$(LATEX) && $(GLOSSARY) && \
	$(LATEX)

fromRepo:
	cd tex && $(LATEX) && $(LATEX) && $(LATEX)

archive:
	git ls-files bib gfx tex | xargs tar -czvf arxiv.tar.gz
