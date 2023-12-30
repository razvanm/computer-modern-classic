import fontTools.agl

# These comes from /usr/share/texlive/texmf-dist/fonts/enc/dvips/base/ec.enc.
# Reference: https://github.com/charlesmchen/typefacet/blob/master/data/Adobe%20Glyph%20List/aglfn13.txt
GLYPHS = ['grave', 'acute', 'circumflex', 'tilde', 'dieresis', 'hungarumlaut', 'ring', 'caron', 'breve', 'macron', 'dotaccent', 'cedilla', 'ogonek', 'quotesinglbase', 'guilsinglleft', 'guilsinglright', 'quotedblleft', 'quotedblright', 'quotedblbase', 'guillemotleft', 'guillemotright', 'endash', 'emdash', 'cwm', 'perthousandzero', 'dotlessi', 'dotlessj', 'ff', 'fi', 'fl', 'ffi', 'ffl', 'visiblespace', 'exclam', 'quotedbl', 'numbersign', 'dollar', 'percent', 'ampersand', 'quoteright', 'parenleft', 'parenright', 'asterisk', 'plus', 'comma', 'hyphen', 'period', 'slash', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'colon', 'semicolon', 'less', 'equal', 'greater', 'question', 'at', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore', 'quoteleft', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'braceleft', 'bar', 'braceright', 'asciitilde', 'hyphen', 'Abreve', 'Aogonek', 'Cacute', 'Ccaron', 'Dcaron', 'Ecaron', 'Eogonek', 'Gbreve', 'Lacute', 'Lcaron', 'Lslash', 'Nacute', 'Ncaron', 'Eng', 'Ohungarumlaut', 'Racute', 'Rcaron', 'Sacute', 'Scaron', 'Scedilla', 'Tcaron', 'Tcedilla', 'Uhungarumlaut', 'Uring', 'Ydieresis', 'Zacute', 'Zcaron', 'Zdotaccent', 'IJ', 'Idotaccent', 'dcroat', 'section', 'abreve', 'aogonek', 'cacute', 'ccaron', 'dcaron', 'ecaron', 'eogonek', 'gbreve', 'lacute', 'lcaron', 'lslash', 'nacute', 'ncaron', 'eng', 'ohungarumlaut', 'racute', 'rcaron', 'sacute', 'scaron', 'scedilla', 'tcaron', 'tcedilla', 'uhungarumlaut', 'uring', 'ydieresis', 'zacute', 'zcaron', 'zdotaccent', 'ij', 'exclamdown', 'questiondown', 'sterling', 'Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis', 'Aring', 'AE', 'Ccedilla', 'Egrave', 'Eacute', 'Ecircumflex', 'Edieresis', 'Igrave', 'Iacute', 'Icircumflex', 'Idieresis', 'Eth', 'Ntilde', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde', 'Odieresis', 'OE', 'Oslash', 'Ugrave', 'Uacute', 'Ucircumflex', 'Udieresis', 'Yacute', 'Thorn', 'Germandbls', 'agrave', 'aacute', 'acircumflex', 'atilde', 'adieresis', 'aring', 'ae', 'ccedilla', 'egrave', 'eacute', 'ecircumflex', 'edieresis', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'eth', 'ntilde', 'ograve', 'oacute', 'ocircumflex', 'otilde', 'odieresis', 'oe', 'oslash', 'ugrave', 'uacute', 'ucircumflex', 'udieresis', 'yacute', 'thorn', 'germandbls']

# These are missing from AGL.
AGL_MISSING = {
    'dotlessj': 0x237,
    'cwm': 0x200B,
    'visiblespace': 0x2423,
    'ff': 0xFB00,
    'fi': 0xFB01,
    'fl': 0xFB02,
    'ffi': 0xFB03,
    'ffl': 0xFB04,
    'tcedilla': 0x163,
    'Tcedilla': 0x162,
    'Germandbls': 0x1E9E,
}

# This character doesn't have a unicode counterpart.
NO_UNICODE = set(['perthousandzero'])

print('NAME_UNICODE = [', end='')
for i in range(len(GLYPHS)):
    uni = 0
    if GLYPHS[i] in NO_UNICODE:
        pass
    elif GLYPHS[i] in AGL_MISSING:
        uni = AGL_MISSING[GLYPHS[i]]
    else:
        uni = fontTools.agl.AGL2UV[GLYPHS[i]]
    print("('%s', %d)," % (GLYPHS[i], uni), end='')
print(']')
