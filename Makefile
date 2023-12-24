SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(shell ls documentation/*.py)
DRAWBOT_OUTPUT=$(shell ls documentation/*.py | sed 's/\.py/.png/g')

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

build.stamp: venv .init.stamp sources/config.yaml $(SOURCES)
	. venv/bin/activate; rm -rf fonts/; gftools builder sources/config.yaml && touch build.stamp

.init.stamp: venv
	. venv/bin/activate; python3 scripts/first-run.py

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: venv build.stamp
	. venv/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --full-lists --succinct --badges out/badges --html out/fontbakery/fontbakery-report.html --ghmarkdown out/fontbakery/fontbakery-report.md $(shell find fonts/ttf -type f)  || echo '::warning file=sources/config.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

test-glyph-coverage:
	. venv/bin/activate; \
	fontbakery check-googlefonts --no-colors --full-lists --succinct --checkid com.google.fonts/check/glyph_coverage fonts/ttf/ComputerModernClassic-Regular.ttf | grep 0x > missing-regular && \
	fontbakery check-googlefonts --no-colors --full-lists --succinct --checkid com.google.fonts/check/glyph_coverage fonts/ttf/ComputerModernClassic-Italic.ttf | grep 0x > missing-italic && \
	egrep "$(shell cat GF_Latin_Kernel.nam | cut -d ' ' -f 1 | xargs | tr ' ' '|')" missing-regular > missing-regular.kernel || \
	egrep "$(shell cat GF_Latin_Kernel.nam | cut -d ' ' -f 1 | xargs | tr ' ' '|')" missing-italic > missing-italic.kernel || true

proof: venv build.stamp
	. venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $(shell find fonts/ttf -type f) -o out/proof

out/proof-bitmap/Regular: fonts/ttf/ComputerModernClassic-Regular.ttf sources/render-freetype.py
	mkdir -p $@; ./sources/render-freetype.py -v $< $@

out/proof-bitmap/Italic: fonts/ttf/ComputerModernClassic-Italic.ttf sources/render-freetype.py
	mkdir -p $@; ./sources/render-freetype.py -v $< $@

proof-bitmap: out/proof-bitmap/Regular out/proof-bitmap/Italic

proof-testfont:
	$(MAKE) -C sources/testfont
	mkdir -p out/proof-testfont
	cd sources/testfont && find . -name \*.html \-or -name \*.svg | cpio -pduv ../../out/proof-testfont

images: venv build.stamp $(DRAWBOT_OUTPUT)
	git add documentation/*.png && git commit -m "Rebuild images" documentation/*.png

%.png: %.py build.stamp
	python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" | xargs rm delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update:
	pip install --upgrade $(dependency); pip freeze > requirements.txt
