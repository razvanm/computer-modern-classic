PFA_FILES = \
	cmr10.pfa cmti10.pfa \
	cmmi10.pfa cmsy10.pfa \
	ecrm10.pfa ecti10.pfa \
	tcrm10.pfa tcti10.pfa \
	eurorm.pfa euroit.pfa

UFO_DIRS = \
	ComputerModernClassic-Regular.ufo \
	ComputerModernClassic-Italic.ufo

MFTRACE = ./mftrace/mftrace.py --verbose --potrace

all: $(PFA_FILES) $(UFO_DIRS)

pfa: $(PFA_FILES)

%.png: %.pbm
	convert $< $@

%.pfa: ./mftrace/mftrace.py
	$(MFTRACE) --keep mftrace.$(basename $@) $(basename $@) \
	  &> mftrace.$(basename $@).log

cmmi10.pfa:
cmr10.pfa:
cmsy10.pfa:
cmti10.pfa:

ecrm10.pfa:
	$(MFTRACE) \
	  --keep mftrace.$(basename $@) \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/base/ec.enc \
	  $(basename $@) &> mftrace.$(basename $@).log

tcrm10.pfa:
	$(MFTRACE) \
	  --keep mftrace.$(basename $@) \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tc.enc \
	  $(basename $@) &> mftrace.$(basename $@).log

ecti10.pfa:
	$(MFTRACE) \
	  --keep mftrace.$(basename $@) \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/base/ec.enc \
	  $(basename $@) &> mftrace.$(basename $@).log

tcti10.pfa:
	$(MFTRACE) \
	  --keep mftrace.$(basename $@) \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tc.enc \
	  $(basename $@) &> mftrace.$(basename $@).log

eurorm.pfa:
euroit.pfa:

ComputerModernClassic-Regular.ufo: $(PFA_FILES) fix.py fix_fontinfo.sh fix-fontinfo.py
	fontforge -quiet -script fix.py cmr10.pfa ComputerModernClassic-Regular.ufo
	./fix_fontinfo.sh ComputerModernClassic-Regular.ufo/fontinfo.plist
	./fix-fontinfo.py ComputerModernClassic-Regular.ufo

ComputerModernClassic-Italic.ufo: $(PFA_FILES) fix.py fix_fontinfo.sh fix-fontinfo.py
	fontforge -quiet -script fix.py cmti10.pfa ComputerModernClassic-Italic.ufo
	./fix_fontinfo.sh ComputerModernClassic-Italic.ufo/fontinfo.plist
	./fix-fontinfo.py ComputerModernClassic-Italic.ufo

clean:
	rm -rf $(PFA_FILES) $(addprefix mftrace.,$(basename $(PFA_FILES)))
	rm mftrace.*.log

.PHONY: clean
