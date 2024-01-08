UFO_DIRS = \
	ComputerModernClassic-Regular.ufo \
	ComputerModernClassic-Italic.ufo

all: $(UFO_DIRS)

REGULAR_FILES = \
	ec/ecrm10.gf ec/ecrm10.tfm \
	ec/tcrm10.gf ec/tcrm10.tfm \
	testfont/eurorm.gf testfont/eurorm.tfm

ComputerModernClassic-Regular.ufo: ff-gen.py fix-fontinfo.py $(REGULAR_FILES)
	fontforge -quiet -script $< $@ $(REGULAR_FILES)
	./fix-fontinfo.py $@

ITALIC_FILES = \
	  ec/ecti10.gf ec/ecti10.tfm \
	  ec/tcti10.gf ec/tcti10.tfm \
	  testfont/euroit.gf testfont/euroit.tfm

ComputerModernClassic-Italic.ufo: ff-gen.py fix-fontinfo.py $(ITALIC_FILES)
	fontforge -quiet -script $< $@ $(ITALIC_FILES)
	./fix-fontinfo.py $@

.PHONY: clean
clean:
	rm -rf $(UFO_DIRS)
