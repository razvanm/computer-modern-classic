import fontTools.agl

# These come from /usr/share/texlive/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tc.enc
# Reference: https://github.com/charlesmchen/typefacet/blob/master/data/Adobe%20Glyph%20List/aglfn13.txt
GLYPHS = ['grave.uc', 'acute.uc', 'circumflex', 'tilde.uc', 'dieresis.var', 'hungarumlaut.uc', 'ring.uc', 'caron', 'breve', 'macron', 'dotaccent', 'cedilla', 'ogonek', 'quotesinglbase', '.notdef', '.notdef', '.notdef', '.notdef', 'quotedblbase', '.notdef', '.notdef', 'twelveudash', 'threequartersemdash', '.notdef', 'arrowleft', 'arrowright', 'uni0361.alt', 'uni0361', 'uni2040.alt', 'uni2040', '.notdef', '.notdef', 'uni2422', '.notdef', '.notdef', '.notdef', 'dollar', '.notdef', '.notdef', 'quotesingle', '.notdef', '.notdef', 'asteriskmath', '.notdef', 'comma', 'uniFE66', 'period', 'fraction', 'zerooldstyle', 'oneoldstyle', 'twooldstyle', 'threeoldstyle', 'fouroldstyle', 'fiveoldstyle', 'sixoldstyle', 'sevenoldstyle', 'eightoldstyle', 'nineoldstyle', '.notdef', '.notdef', 'angleleft', 'minus', 'angleright', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', 'uni2127', '.notdef', 'circle', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', 'uni2126', '.notdef', '.notdef', '.notdef', 'uni301A', '.notdef', 'uni301B', 'arrowup', 'arrowdown', 'grave.ts1', '.notdef', 'uni22C6', 'uni26AE', 'uni271D', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', 'leaf', 'uni26AD', 'musicalnote', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', 'tildelow', 'hyphendbl', 'breve.ts1', 'caron.ts1', 'hungarumlaut.ts1', 'dblgrave.ts1', 'dagger', 'daggerdbl', 'uni2016', 'perthousand', 'bullet', 'uni2103', 'dollaroldstyle', 'centoldstyle', 'f', 'colonmonetary', 'uni20A9', 'uni20A6', 'uni20B2', 'peso', 'lira', 'uni211E', 'uni203D', 'uni2E18', 'dong', 'trademark', 'uni2031', 'uni2029', 'uni0E3F', 'uni2116', 'uni2052', 'estimated', 'openbullet', 'uni2120', 'uni2045', 'uni2046', 'cent', 'sterling', 'currency', 'yen', 'brokenbar', 'section', 'dieresis.ts1', 'copyright', 'ordfeminine', 'copyleft', 'logicalnot', 'uni2117', 'registered', 'macron.uc', 'degree', 'plusminus', 'twosuperior', 'threesuperior', 'acute.ts1', 'uni00B5', 'paragraph', 'periodcentered', 'uni203B', 'onesuperior', 'ordmasculine', 'radical', 'onequarter', 'onehalf', 'threequarters', 'Euro.old', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', 'multiply', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', 'divide', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef', '.notdef',]

# These are glyphs that already in the EC font.
SKIP = set(['.notdef', 'grave.uc', 'acute.uc', 'circumflex', 'tilde.uc', 'dieresis.var', 'hungarumlaut.uc', 'ring.uc', 'caron', 'breve', 'macron', 'dotaccent', 'cedilla', 'ogonek', 'quotesinglbase', 'quotedblbase', 'twelveudash', 'threequartersemdash', 'dollar', 'comma', 'period', 'tildelow', 'hyphendbl', 'f', 'macron.uc', 'sterling', 'section', 'Euro.old'])

# Paragraph Separator is suppose to be empty and FontBakery enforces this.
# Reference: https://www.compart.com/en/unicode/U+2029
INCORRECT = set(['uni2029'])

# These are missing from AGL.
AGL_MISSING = {
    'peso': 0x20B1,
    'copyleft': 0x1F12F,
    'twosuperior': 0x00B2,  # TODO: check if this is correct
    'threesuperior': 0x00B3,  # TODO: check if this is correct
    'onesuperior': 0x00B9,  # TODO: check if this is correct
    'tildelow': 0x02F7,  # TODO: check if this is correct
    'leaf': -1,
}

print('TC_NAME_UNICODE = [', end='')
for i in range(len(GLYPHS)):
    name = GLYPHS[i]
    uni = -1
    if name in SKIP or name in INCORRECT:
        name = '.notdef'
    elif name.endswith('.ts1'):
        name = '.notdef'
    elif name.endswith('.alt') or name.endswith('oldstyle'):
        pass
    elif name.startswith('uni'):
        uni = int(name[3:], base=16)
    elif name in AGL_MISSING:
        uni = AGL_MISSING[GLYPHS[i]]
    else:
        uni = fontTools.agl.AGL2UV[GLYPHS[i]]
    uni = '0x%X' % (uni) if uni != -1 else '-1'
    print("('%s', %s)," % (name, uni), end='')
print(']')
