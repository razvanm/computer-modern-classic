import fontforge
import sys

def copy_symbols(src, dest, glyph_names):
    for name in glyph_names:
        g = src[name]
        src.selection.select(name)
        print('Copying "%s" (0x%04x)' % (g.glyphname, g.unicode))
        src.copy()
        c = dest.createChar(g.unicode, g.glyphname)
        dest.selection.select(g.glyphname)
        dest.paste()

cmsy10 = fontforge.open('cmsy10.pfa')
cmmi10 = fontforge.open('cmmi10.pfa')
cmti10 = fontforge.open('cmti10.pfa')
cmr10 = fontforge.open('cmr10.pfa')

f = fontforge.open(sys.argv[1])

space = f.createChar(0x20, 'space')
space.width = 500
space.vwidth = 500

nbspace = f.createChar(0xA0, 'uni00A0')
nbspace.width = 500
nbspace.vwidth = 500

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

copy_symbols(cmsy10, f, [
    'bullet', 'minus', 'multiply', 'divide', 'periodcentered', 'paragraph',
    'section', 'braceleft', 'braceright', 'backslash'])

copy_symbols(cmmi10, f, ['less', 'greater', 'slash'])

if sys.argv[2].endswith('-Regular.ufo'):
    # Copy the POUND SIGN (U+00A3) from cmti10 where it shows up under the
    # 'dollar' name (0x26 is the position in cmti10).
    cmti10.selection.select('dollar')
    cmti10.copy()
    pound_sign = f.createChar(0x00A3, 'poundsign')
    f.selection.select(pound_sign.glyphname)
    f.paste()
    cmti10.close()

if sys.argv[2].endswith('-Italic.ufo'):
    # The "dollar" is actually the pound sign.
    f[0x0024].glyphname = 'poundsign'
    f[0x0024].unicode = 0x00A3

    copy_symbols(cmr10, f, ['dollar'])

f.generate(sys.argv[2])
