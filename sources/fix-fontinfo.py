#!/usr/bin/env python

import defcon
import sys

f = defcon.Font(sys.argv[1])
italic = 'Italic' in sys.argv[1]

# For for FontBakery:com.google.fonts/check/italic_angle.
f.info.italicAngle = -14.0 if italic else 0

# Fix for FontBakery:com.google.fonts/check/font_copyright.
f.info.copyright = 'Copyright 2023 The Computer Modern Classic Project Authors (https://github.com/razvanm/computer-modern-classic)'

# Fix for FontBakery:com.google.fonts/check/vendor_id.
f.info.openTypeOS2VendorID = 'GOOG'

# Fix for FontBakery:com.google.fonts/check/font_names.
f.info.familyName = 'Computer Modern Classic'
f.info.postscriptFullName = 'Computer Modern Classic'
f.info.styleMapFamilyName = 'Computer Modern Classic'
f.info.styleName = 'Italic' if italic else 'Regular'
# Stripping the ".ufo" ending gives us the font name.
f.info.postscriptFontName = sys.argv[1].split('.')[0]

# Fix FontBakeryCheck:com.google.fonts/check/fstype.
f.info.openTypeOS2Type = []

# Fix for FontBakery:com.google.fonts/check/fsselection.
f.info.styleMapStyleName = 'italic' if italic else 'regular'

# Fix for FontBakery:com.google.fonts/check/os2/use_typo_metrics.
# Reference: https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection
f.info.openTypeOS2Selection = [7]

# Fix for FontBakery:com.google.fonts/check/name/license.
f.info.openTypeNameLicense = 'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL'
f.info.openTypeNameLicenseURL = 'https://openfontlicense.org'

# Fix for FontBakery:com.google.fonts/check/family/win_ascent_and_descent.
f.info.openTypeOS2WinAscent = 969
f.info.openTypeOS2WinDescent = 419

# Fix for com.FontBakery:com.google.fonts/check/vertical_metrics.
# Reference: https://googlefonts.github.io/gf-guide/metrics.html
f.info.openTypeOS2TypoLineGap = 0
f.info.openTypeHheaLineGap = 0
f.info.openTypeHheaAscender = 900
f.info.openTypeHheaDescender = -300

# Fix for FontBakery:com.google.fonts/check/os2_metrics_match_hhea.
f.info.openTypeOS2TypoAscender = f.info.openTypeHheaAscender
f.info.openTypeOS2TypoDescender = f.info.openTypeHheaDescender

f.save(sys.argv[1])
