PYTHON = python
TEXC = pdflatex

default : assn3.pdf clean

clean :
	rm assn3.aux
	rm assn3.log

assn3.pdf : drawings
	$(TEXC) assn3.tex > /dev/null

drawings :
	python euler.py
	python plot_energy.py
	python plot_error.py
