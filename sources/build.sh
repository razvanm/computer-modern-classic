#!/bin/bash

# UFO parsers don't like empty integer values.
function fix_fontinfo() {
  cat $1 \
    | sed \
      -e '/<integer></d' \
      > $1.sed
  mv $1.sed $1
}

set -x
cd "$(dirname "$0")"

# Math symbols.
mftrace --potrace cmsy10

# Math italic symbols.
mftrace --potrace cmmi10

mftrace --potrace cmr10
fontforge -quiet -script fix.py \
  cmr10.pfa \
  ComputerModernClassic-Regular.ufo
fix_fontinfo ComputerModernClassic-Regular.ufo/fontinfo.plist
./fix-fontinfo.py ComputerModernClassic-Regular.ufo

mftrace --potrace cmti10
fontforge -quiet -script fix.py \
  cmti10.pfa \
  ComputerModernClassic-Italic.ufo
fix_fontinfo ComputerModernClassic-Italic.ufo/fontinfo.plist
./fix-fontinfo.py ComputerModernClassic-Italic.ufo
