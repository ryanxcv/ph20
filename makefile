PYTHON = python
TEXC = pdflatex

default : assn3.pdf

assn3.pdf :
	$(TEXC) assn3.tex
