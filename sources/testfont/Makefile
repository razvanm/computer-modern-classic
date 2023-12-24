FONTS = \
	cmmi10 \
	cmr10 \
	cmsy10 \
	cmti10 \
	ecrm10 \
	tcrm10 \
	ecti10 \
	tcti10 \
	eurorm \
	euroit

all: $(addsuffix .gf,$(FONTS)) index.html
svg: $(addsuffix _svg,$(FONTS))
html: index.html

%.gf:
	mf-nowin -interaction=nonstopmode '\mode=ibx; input $(basename $@)'
	ln -s $(basename $@).9600gf $(basename $@).gf

char-%.pbm:
	@mkdir -p $(dir $@)
	../mftrace/gf2pbm -n $(shell printf '%d' 0x$(patsubst char-%.pbm,%,$(notdir $@))) -o $@ $<

%.png: %.pbm
	convert $< $@

%.svg: %.pbm
	potrace --svg -o $@ $<

%.html: font.html.template
	sed s/{{FONTNAME}}/$(basename $@)/g $< > $@

index.html: $(addsuffix .html,$(FONTS)) svg
	rm -f $@
	for i in $(addsuffix .html,$(FONTS)); do \
	  echo '<a href="'$$i'">'$$i'</a><br>' >> $@; \
	done

%.deps: %.gf
	echo -n '$(basename $@)_pbm_FILES = ' > $@; \
	for i in $(shell gftype $< | grep ^Character | cut -d ' ' -f 2 | tr -d ':'); do \
	  printf '$(basename $@)/char-%02x.pbm ' $$i >> $@; \
	done; \
	echo >> $@; \
	echo '$$($(basename $@)_pbm_FILES): $<' >> $@; \
	echo '$(basename $@)_pbm: $$($(basename $@)_pbm_FILES)' >> $@;
	echo '$(basename $@)_svg: $$(addsuffix .svg, $$(basename $$($(basename $@)_pbm_FILES)))' >> $@;
	echo '$(basename $@)_png: $$(addsuffix .png, $$(basename $$($(basename $@)_pbm_FILES)))' >> $@;

.PHONY: clean
clean:
	rm -rf *.log *.html *gf *.tfm *.deps $(FONTS)

.PHONY: deps
deps:
	$(MAKE) $(addsuffix .deps,$(FONTS))

# These files are produced by the deps target.
include cmmi10.deps
include cmr10.deps
include cmsy10.deps
include cmti10.deps
include ecrm10.deps
include tcrm10.deps
include ecti10.deps
include tcti10.deps
include eurorm.deps
include euroit.deps
