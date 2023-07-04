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

f = fontforge.open(sys.argv[1])

space = f.createChar(0x20, 'space')
space.width = 500
space.vwidth = 500

nbspace = f.createChar(0xA0, 'uni00A0')
nbspace.width = 500
nbspace.vwidth = 500

if sys.argv[2].endswith('-Regular.ufo'):
    copy_symbols(fontforge.open('cmsy10.pfa'), f, [
        'bullet', 'minus', 'multiply', 'divide', 'periodcentered',
        'paragraph', 'section', 'braceleft', 'braceright'])

    copy_symbols(fontforge.open('cmmi10.pfa'), f, [
        'less', 'greater', 'slash'])

f.generate(sys.argv[2])
