UFO_DIRS = \
	ComputerModernClassic-Regular.ufo \
	ComputerModernClassic-Italic.ufo

all: $(UFO_DIRS)

ComputerModernClassic-Regular.ufo: ff-gen.py fix-fontinfo.py
	fontforge -quiet -script $< $@ \
	  testfont/ecrm10.gf testfont/ecrm10.tfm \
	  testfont/tcrm10.gf testfont/tcrm10.tfm \
	  testfont/eurorm.gf testfont/eurorm.tfm
	./fix-fontinfo.py $@

ComputerModernClassic-Italic.ufo: ff-gen.py fix-fontinfo.py
	fontforge -quiet -script $< $@ \
	  testfont/ecti10.gf testfont/ecti10.tfm \
	  testfont/tcti10.gf testfont/tcti10.tfm \
	  testfont/euroit.gf testfont/euroit.tfm
	./fix-fontinfo.py $@

