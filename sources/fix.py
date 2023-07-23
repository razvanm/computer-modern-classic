import fontforge
import sys

def copy_symbol(src, dest, src_glyph_name, dest_glyph_name, dest_glyph_unicode):
    print('Copying "%s" to "%s" (U+%04x)...' % (
        src_glyph_name, dest_glyph_name, dest_glyph_unicode))
    g = src[src_glyph_name]
    src.selection.select(src_glyph_name)
    src.copy()
    c = dest.createChar(dest_glyph_unicode, dest_glyph_name)
    dest.selection.select(dest_glyph_name)
    dest.paste()

def copy_symbols(src, dest, glyph_names):
    for name in glyph_names:
        g = src[name]
        copy_symbol(src, dest, g.glyphname, g.glyphname, g.unicode)

cmsy10 = fontforge.open('cmsy10.pfa')
cmmi10 = fontforge.open('cmmi10.pfa')
cmti10 = fontforge.open('cmti10.pfa')
cmr10 = fontforge.open('cmr10.pfa')
ecrm10 = fontforge.open('ecrm10.pfa')
tcrm10 = fontforge.open('tcrm10.pfa')
ecti10 = fontforge.open('ecti10.pfa')
tcti10 = fontforge.open('tcti10.pfa')
# Some useful information about euro symbol: https://texfaq.org/FAQ-euro
eurorm = fontforge.open('eurorm.pfa')
euroit = fontforge.open('euroit.pfa')

f = fontforge.open(sys.argv[1])

space = f.createChar(0x20, 'space')
space.width = 500
space.vwidth = 500

nbspace = f.createChar(0xA0, 'uni00A0')
nbspace.width = 500
nbspace.vwidth = 500

# Create "ellipsis" (U+2026) by making a copy of the "period".
period = f['period']
ellipsis = f.createChar(0x2026, 'ellipsis')
ellipsis.addReference('period')
(_, _, xoffset, _) = period.boundingBox()
ellipsis.addReference('period', psMat.translate(xoffset, 0))
ellipsis.addReference('period', psMat.translate(2*xoffset, 0))
ellipsis.width = round(period.width + 2*xoffset)

# Make the CIRCUMFLEX ACCENT (U+005E) a copy of "circumflex" (U+02C6,
# 0x5E in cmr10).
f['circumflex'].altuni = (0x005E,)

# Make the TILDE (U+007E) a copy of "tilde" (U+02DC, 0x7E in cmr10).
f['tilde'].altuni = (0x7E,)

# Make the APOSTROPHE (U+0027) a copy of "acute" (U+00B4, 0x13 in cmr10).
f['acute'].altuni = (0x0027,)

# Make the QUOTATION MARK (U+0022) a copy of "hungarumlat" (U+02DD,
# 0x7D in cmr10).
f['hungarumlaut'].altuni = (0x0022,)

# Make the DEGREE SIGN (U+00B0) a copy of "ring" (U+02DA, 0x17 in cmr10).
f['ring'].altuni = (0x00B0,)

EC_COMMON = ['quotedbl', 'less', 'equal', 'greater', 'backslash',
             'underscore', 'braceleft', 'bar', 'braceright',
             'section']

TC_COMMON = ['quotesingle', 'angleleft', 'minus', 'angleright',
             'perthousand', 'bullet', 'trademark', 'uni2031', 'cent',
             'yen', 'copyright', 'registered', 'degree',
             'plusminus', 'paragraph', 'periodcentered',
             'multiply', 'divide']

if sys.argv[2].endswith('-Regular.ufo'):
    copy_symbols(ecrm10, f, EC_COMMON + ['sterling'])
    copy_symbols(tcrm10, f, TC_COMMON)
    copy_symbol(eurorm, f, 'E', 'euro', 0x20AC)

if sys.argv[2].endswith('-Italic.ufo'):
    # The "dollar" is actually the pound sign.
    f[0x0024].glyphname = 'poundsign'
    f[0x0024].unicode = 0x00A3

    copy_symbols(ecti10, f, EC_COMMON + ['dollar'])
    copy_symbols(tcti10, f, TC_COMMON)
    copy_symbol(euroit, f, 'E', 'euro', 0x20AC)

f.generate(sys.argv[2])
