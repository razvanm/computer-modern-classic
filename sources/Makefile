PFA_FILES = \
	cmr10.pfa cmti10.pfa \
	cmmi10.pfa cmsy10.pfa \
	ecrm10.pfa ecti10.pfa \
	tcrm10.pfa tcti10.pfa

UFO_DIRS = \
	ComputerModernClassic-Regular.ufo \
	ComputerModernClassic-Italic.ufo

all: $(PFA_FILES) $(UFO_DIRS)

%.pfa: ./mftrace/mftrace.py
	./mftrace/mftrace.py --potrace $(basename $@)

cmmi10.pfa:
cmr10.pfa:
cmsy10.pfa:
cmti10.pfa:

ecrm10.pfa:
	./mftrace/mftrace.py --potrace \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/base/ec.enc \
	  $(basename $@)
tcrm10.pfa:
	./mftrace/mftrace.py --potrace \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tc.enc \
	  $(basename $@)

ecti10.pfa:
	./mftrace/mftrace.py --potrace \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/base/ec.enc $(basename $@)
tcti10.pfa:
	./mftrace/mftrace.py --potrace \
	  -e /usr/share/texlive/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tc.enc \
	  $(basename $@)

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
