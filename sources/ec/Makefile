FONTS = \
	ecrm \
	tcrm \
	ecti \
	tcti

all: $(addsuffix .gf,$(FONTS))

%.gf: ../custom.mf $(wildcard *.mf)
	mf-nowin -interaction=nonstopmode -jobname=$(basename $@)10 '\smode="../custom"; gensize:=10; input exbase; input $(basename $@)'
	ln -f -s $(basename $@)10.10000gf $(basename $@)10.gf

.PHONY: clean
clean:
	rm -f *.log *gf *.tfm
