all: como_empezar_a_empaquetar.pdf

como_empezar_a_empaquetar.pdf: check como_empezar_a_empaquetar.rst
	rst2pdf como_empezar_a_empaquetar.rst

check:
	if ( ! rpm --quiet -q rst2pdf ); then echo; echo 'Please, install rst2pdf with: yum -y install rst2pdf'; echo; exit 1; fi

clean:
	rm *.pdf
