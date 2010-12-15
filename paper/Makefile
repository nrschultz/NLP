# latex source file name
TARGET=cs65f10

SRC=$(wildcard *.tex) 

PDFCOMMAND=/usr/bin/evince

all: ${TARGET}.pdf

# If you have have a bibtex file then you need to run this set of commands 
# 1. run latex to generate the aux file
# 2. run bibtex to generate the bbl file from the aux file
# 3. run latex to add the bibliography entries (and generate their
# 	labels)
# 4. run latex again so that any reference to them are updated. 
#
${TARGET}.pdf:	${TARGET}.tex
	pdflatex ${TARGET}.tex
	bibtex ${TARGET}
	pdflatex ${TARGET}.tex
	pdflatex ${TARGET}.tex



# create a pdf version of the document using ps2pdf, we first create a
# different postcript file, because it needs a version with type 1 fonts
# otherwise the resulting pdf file is blurry when read with acroread
#
ps:	${TARGET}.ps

# create a postscript version of the document
#
${TARGET}.ps:	${TARGET}.dvi
	dvips -t letter -o ${TARGET}.ps ${TARGET}


view: ${TARGET}.pdf
	${PDFCOMMAND} ${TARGET}.pdf

clean:
	rm -f ${TARGET}.dvi ${TARGET}.log ${TARGET}.ps ${TARGET}.aux ${TARGET}.bbl  ${TARGET}.blg $(EPS) ${TARGET}.pdf

