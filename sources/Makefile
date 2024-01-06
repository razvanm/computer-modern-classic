UFO_DIRS = \
	ComputerModernClassic-Regular.ufo \
	ComputerModernClassic-Italic.ufo

all: $(UFO_DIRS)

REGULAR_FILES = \
	testfont/ecrm10.gf testfont/ecrm10.tfm \
	testfont/tcrm10.gf testfont/tcrm10.tfm \
	testfont/eurorm.gf testfont/eurorm.tfm

ComputerModernClassic-Regular.ufo: ff-gen.py fix-fontinfo.py $(REGULAR_FILES)
	fontforge -quiet -script $< $@ $(REGULAR_FILES)
	./fix-fontinfo.py $@

ITALIC_FILES = \
	  testfont/ecti10.gf testfont/ecti10.tfm \
	  testfont/tcti10.gf testfont/tcti10.tfm \
	  testfont/euroit.gf testfont/euroit.tfm

ComputerModernClassic-Italic.ufo: ff-gen.py fix-fontinfo.py $(ITALIC_FILES)
	fontforge -quiet -script $< $@ $(ITALIC_FILES)
	./fix-fontinfo.py $@

.PHONY: clean
clean:
	rm -rf $(UFO_DIRS)
