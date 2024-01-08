## FontBakery report

fontbakery version: 0.10.8

<details><summary><b>[2] Experimental checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Shapes languages in all GF glyphsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyphsets/shape_languages">com.google.fonts/check/glyphsets/shape_languages</a>)</summary><div>


* 🔥 **FAIL** GF_Latin_Core glyphset:

| Language | FAIL messages |
| :--- | :--- |
| mt_Latn (Maltese) | Some base glyphs were missing: għ, ħ |
|  ^  | Shaper produced a .notdef |
| ro_Latn (Romanian) | in Romanian, S-cedilla should become S-comma-accent; both buffers returned Scedilla=0+555 |

 [code: failed-language-shaping]
* ⚠ **WARN** GF_Latin_Core glyphset:

| Language | FAIL messages |
| :--- | :--- |
| nb_Latn (Norwegian Bokmål) | No exemplar glyphs were defined for language Norwegian Bokmål |

 [code: warning-language-shaping]
</div></details><details><summary>🔥 <b>FAIL:</b> Shapes languages in all GF glyphsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyphsets/shape_languages">com.google.fonts/check/glyphsets/shape_languages</a>)</summary><div>


* 🔥 **FAIL** GF_Latin_Core glyphset:

| Language | FAIL messages |
| :--- | :--- |
| mt_Latn (Maltese) | Some base glyphs were missing: għ, ħ |
|  ^  | Shaper produced a .notdef |
| ro_Latn (Romanian) | in Romanian, S-cedilla should become S-comma-accent; both buffers returned Scedilla=0+562 |

 [code: failed-language-shaping]
* ⚠ **WARN** GF_Latin_Core glyphset:

| Language | FAIL messages |
| :--- | :--- |
| nb_Latn (Norwegian Bokmål) | No exemplar glyphs were defined for language Norwegian Bokmål |

 [code: warning-language-shaping]
</div></details><br></div></details><details><summary><b>[14] ComputerModernClassic-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0110 (LATIN CAPITAL LETTER D WITH STROKE)


	- 0x0126 (LATIN CAPITAL LETTER H WITH STROKE)


	- 0x0127 (LATIN SMALL LETTER H WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02C7 CARON: try adding one of: tifinagh, yi, canadian-aboriginal
 * U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
 * U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
 * U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: tai-le, old-permic, syriac, math, coptic, malayalam, canadian-aboriginal, tifinagh
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
 * U+030C COMBINING CARON: try adding one of: tai-le, cherokee
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic
 * U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition
 * U+203B REFERENCE MARK: not included in any glyphset definition
 * U+203D INTERROBANG: not included in any glyphset definition
 * U+2040 CHARACTER TIE: not included in any glyphset definition
 * U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition
 * U+2103 DEGREE CELSIUS: not included in any glyphset definition
 * U+2116 NUMERO SIGN: try adding cyrillic
 * U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition
 * U+211E PRESCRIPTION TAKE: not included in any glyphset definition
 * U+2120 SERVICE MARK: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+2127 INVERTED OHM SIGN: not included in any glyphset definition
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
 * U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
 * U+2217 ASTERISK OPERATOR: try adding math
 * U+221A SQUARE ROOT: try adding math
 * U+22C6 STAR OPERATOR: try adding one of: math, symbols
 * U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols
 * U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols
 * U+2422 BLANK SYMBOL: try adding symbols
 * U+2423 OPEN BOX: try adding symbols
 * U+25CB WHITE CIRCLE: try adding symbols
 * U+25E6 WHITE BULLET: try adding symbols
 * U+266A EIGHTH NOTE: try adding one of: symbols, music
 * U+26AD MARRIAGE SYMBOL: try adding symbols
 * U+26AE DIVORCE SYMBOL: try adding symbols
 * U+271D LATIN CROSS: try adding one of: emoji, symbols
 * U+2E18 INVERTED INTERROBANG: not included in any glyphset definition
 * U+301A LEFT WHITE SQUARE BRACKET: try adding one of: phags-pa, yi
 * U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: phags-pa, yi
 * U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition
 * U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition
 * U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition
 * U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition
 * U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition
 * U+FE66 SMALL EQUALS SIGN: not included in any glyphset definition
 * U+1F12F COPYLEFT SYMBOL: try adding symbols

Or you can add the above codepoints to one of the subsets supported by the font: `latin`, `latin-ext` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- comma + comma

	- endash + hyphen

	- exclam + quoteleft

	- f + f

	- f + i

	- i + l

	- ff + i

	- greater + greater

	- hyphen + hyphen

	- hyphen + hyphen.char

	- less + less

	- question + quoteleft

	- quoteleft + quoteleft

	- quoteright + quoteright [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 31 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** Name ID 6 'ComputerModernClassic-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms [code: nameid6-too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- centoldstyle

	- dollaroldstyle

	- eightoldstyle

	- fiveoldstyle

	- fouroldstyle

	- leaf

	- nineoldstyle

	- oneoldstyle

	- perthousandzero

	- sevenoldstyle

	- sixoldstyle

	- threeoldstyle

	- twooldstyle

	- uni0361.alt

	- uni2040.alt

	- zerooldstyle
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: threesuperior	Contours detected: 2	Expected: 1

	- Glyph name: onesuperior	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Germandbls	Contours detected: 2	Expected: 1

	- Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni203D	Contours detected: 3	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: uni203D	Contours detected: 3	Expected: 2

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 777 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 666:
logicalnot
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acutecomb (U+0301), gravecomb (U+0300), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0326 (U+0326), uni0327 (U+0327) and uni0328 (U+0328) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0361 (U+0361) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* B (U+0042): L<<453.0,1.0>--<241.0,0.0>>

	* Eth (U+00D0): L<<230.0,313.0>--<231.0,186.0>>

	* Lslash (U+0141): L<<129.0,342.0>--<128.0,481.0>>

	* N (U+004E): L<<172.0,605.0>--<171.0,348.0>>

	* Nacute (U+0143): L<<172.0,605.0>--<171.0,348.0>>

	* Ncaron (U+0147): L<<172.0,605.0>--<171.0,348.0>>

	* Ncedilla (U+0145): L<<172.0,605.0>--<171.0,348.0>>

	* Ntilde (U+00D1): L<<172.0,605.0>--<171.0,348.0>>

	* P (U+0050): L<<233.0,301.0>--<234.0,182.0>>

	* R (U+0052): L<<230.0,323.0>--<231.0,193.0>>

	* Racute (U+0154): L<<230.0,323.0>--<231.0,193.0>>

	* Rcaron (U+0158): L<<230.0,323.0>--<231.0,193.0>>

	* Z (U+005A): L<<303.0,0.0>--<63.0,1.0>>

	* Zacute (U+0179): L<<303.0,0.0>--<63.0,1.0>>

	* Zcaron (U+017D): L<<303.0,0.0>--<63.0,1.0>>

	* Zdotaccent (U+017B): L<<303.0,0.0>--<63.0,1.0>>

	* a (U+0061): L<<402.0,195.0>--<403.0,69.0>>

	* aacute (U+00E1): L<<402.0,195.0>--<403.0,69.0>>

	* abreve (U+0103): L<<402.0,195.0>--<403.0,69.0>>

	* acircumflex (U+00E2): L<<402.0,195.0>--<403.0,69.0>>

	* adieresis (U+00E4): L<<402.0,195.0>--<403.0,69.0>>

	* agrave (U+00E0): L<<402.0,195.0>--<403.0,69.0>>

	* amacron (U+0101): L<<402.0,195.0>--<403.0,69.0>>

	* aogonek (U+0105): L<<402.0,195.0>--<403.0,69.0>>

	* aring (U+00E5): L<<402.0,195.0>--<403.0,69.0>>

	* arrowleft (U+2190): L<<163.0,271.0>--<546.0,270.0>>

	* arrowright (U+2192): L<<452.0,270.0>--<835.0,271.0>>

	* atilde (U+00E3): L<<402.0,195.0>--<403.0,69.0>>

	* braceleft (U+007B): L<<291.0,136.0>--<292.0,2.0>>

	* braceleft (U+007B): L<<292.0,498.0>--<291.0,364.0>>

	* braceright (U+007D): L<<208.0,2.0>--<209.0,136.0>>

	* braceright (U+007D): L<<209.0,364.0>--<208.0,498.0>>

	* ff (U+FB00): L<<179.0,224.0>--<180.0,61.0>>

	* ff (U+FB00): L<<375.0,61.0>--<376.0,224.0>>

	* ffi (U+FB03): L<<179.0,224.0>--<180.0,61.0>>

	* ffi (U+FB03): L<<375.0,61.0>--<376.0,224.0>>

	* ffl (U+FB04): L<<179.0,224.0>--<180.0,61.0>>

	* ffl (U+FB04): L<<375.0,61.0>--<376.0,224.0>>

	* fi (U+FB01): L<<179.0,224.0>--<180.0,61.0>>

	* fl (U+FB02): L<<179.0,224.0>--<180.0,61.0>>

	* fl (U+FB02): L<<375.0,61.0>--<376.0,224.0>>

	* four (U+0034): L<<378.0,440.0>--<379.0,209.0>>

	* ij (U+0133): L<<197.0,251.0>--<198.0,61.0>>

	* k (U+006B): L<<179.0,695.0>--<180.0,233.0>>

	* kcedilla (U+0137): L<<179.0,695.0>--<180.0,233.0>>

	* lslash (U+0142): L<<132.0,351.0>--<131.0,478.0>>

	* lslash (U+0142): L<<212.0,360.0>--<213.0,210.0>>

	* m (U+006D): L<<741.0,195.0>--<742.0,61.0>>

	* musicalnote (U+266A): L<<387.0,497.0>--<386.0,317.0>>

	* thorn (U+00FE): L<<179.0,547.0>--<180.0,390.0>>

	* trademark (U+2122): L<<409.0,655.0>--<408.0,511.0>>

	* u (U+0075): L<<186.0,442.0>--<187.0,263.0>>

	* uacute (U+00FA): L<<186.0,442.0>--<187.0,263.0>>

	* ucircumflex (U+00FB): L<<186.0,442.0>--<187.0,263.0>>

	* udieresis (U+00FC): L<<186.0,442.0>--<187.0,263.0>>

	* ugrave (U+00F9): L<<186.0,442.0>--<187.0,263.0>>

	* uhungarumlaut (U+0171): L<<186.0,442.0>--<187.0,263.0>>

	* umacron (U+016B): L<<186.0,442.0>--<187.0,263.0>>

	* uni00B5 (U+00B5): L<<186.0,442.0>--<187.0,263.0>>

	* uni2045 (U+2045): L<<153.0,495.0>--<154.0,366.0>>

	* uni2045 (U+2045): L<<154.0,134.0>--<153.0,6.0>>

	* uni2116 (U+2116): L<<466.0,251.0>--<467.0,400.0>>

	* uni211E (U+211E): L<<230.0,323.0>--<231.0,191.0>>

	* uni2120 (U+2120): L<<409.0,655.0>--<408.0,511.0>>

	* uni2422 (U+2422): L<<179.0,695.0>--<180.0,570.0>>

	* uogonek (U+0173): L<<186.0,442.0>--<187.0,263.0>>

	* uring (U+016F): L<<186.0,442.0>--<187.0,263.0>>

	* z (U+007A): L<<210.0,0.0>--<35.0,1.0>>

	* z (U+007A): L<<223.0,431.0>--<392.0,430.0>>

	* zacute (U+017A): L<<210.0,0.0>--<35.0,1.0>>

	* zacute (U+017A): L<<223.0,431.0>--<392.0,430.0>>

	* zcaron (U+017E): L<<210.0,0.0>--<35.0,1.0>>

	* zcaron (U+017E): L<<223.0,431.0>--<392.0,430.0>>

	* zdotaccent (U+017C): L<<210.0,0.0>--<35.0,1.0>>

	* zdotaccent (U+017C): L<<223.0,431.0>--<392.0,430.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters _should_ disappear in other cases, for example: ĩ ĭ i̇ ǐ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ ĵ j̆ j̇ j̊

Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers). 

Your font does *not* cover the following languages that require the soft-dotted feature: Aghem (Latn, 38,843 speakers), Navajo (Latn, 166,319 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Basaa (Latn, 332,940 speakers), Belarusian (Cyrl, 10,064,517 speakers), Igbo (Latn, 27,823,640 speakers). [code: soft-dotted]
</div></details><br></div></details><details><summary><b>[14] ComputerModernClassic-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0110 (LATIN CAPITAL LETTER D WITH STROKE)


	- 0x0126 (LATIN CAPITAL LETTER H WITH STROKE)


	- 0x0127 (LATIN SMALL LETTER H WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02C7 CARON: try adding one of: tifinagh, yi, canadian-aboriginal
 * U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
 * U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
 * U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: tai-le, old-permic, syriac, math, coptic, malayalam, canadian-aboriginal, tifinagh
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
 * U+030C COMBINING CARON: try adding one of: tai-le, cherokee
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic
 * U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition
 * U+203B REFERENCE MARK: not included in any glyphset definition
 * U+203D INTERROBANG: not included in any glyphset definition
 * U+2040 CHARACTER TIE: not included in any glyphset definition
 * U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition
 * U+2103 DEGREE CELSIUS: not included in any glyphset definition
 * U+2116 NUMERO SIGN: try adding cyrillic
 * U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition
 * U+211E PRESCRIPTION TAKE: not included in any glyphset definition
 * U+2120 SERVICE MARK: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+2127 INVERTED OHM SIGN: not included in any glyphset definition
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
 * U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
 * U+2217 ASTERISK OPERATOR: try adding math
 * U+221A SQUARE ROOT: try adding math
 * U+22C6 STAR OPERATOR: try adding one of: math, symbols
 * U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols
 * U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols
 * U+2422 BLANK SYMBOL: try adding symbols
 * U+2423 OPEN BOX: try adding symbols
 * U+25CB WHITE CIRCLE: try adding symbols
 * U+25E6 WHITE BULLET: try adding symbols
 * U+266A EIGHTH NOTE: try adding one of: symbols, music
 * U+26AD MARRIAGE SYMBOL: try adding symbols
 * U+26AE DIVORCE SYMBOL: try adding symbols
 * U+271D LATIN CROSS: try adding one of: emoji, symbols
 * U+2E18 INVERTED INTERROBANG: not included in any glyphset definition
 * U+301A LEFT WHITE SQUARE BRACKET: try adding one of: phags-pa, yi
 * U+301B RIGHT WHITE SQUARE BRACKET: try adding one of: phags-pa, yi
 * U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition
 * U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition
 * U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition
 * U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition
 * U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition
 * U+FE66 SMALL EQUALS SIGN: not included in any glyphset definition
 * U+1F12F COPYLEFT SYMBOL: try adding symbols

Or you can add the above codepoints to one of the subsets supported by the font: `latin`, `latin-ext` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- comma + comma

	- endash + hyphen

	- exclam + quoteleft

	- f + f

	- f + i

	- i + l

	- ff + i

	- greater + greater

	- hyphen + hyphen

	- hyphen + hyphen.char

	- less + less

	- question + quoteleft

	- quoteleft + quoteleft

	- quoteright + quoteright [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 31 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** Name ID 6 'ComputerModernClassic-Italic' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms [code: nameid6-too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- centoldstyle

	- dollaroldstyle

	- eightoldstyle

	- fiveoldstyle

	- fouroldstyle

	- leaf

	- nineoldstyle

	- oneoldstyle

	- perthousandzero

	- sevenoldstyle

	- sixoldstyle

	- threeoldstyle

	- twooldstyle

	- uni0361.alt

	- uni2040.alt

	- zerooldstyle
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: threesuperior	Contours detected: 2	Expected: 1

	- Glyph name: onesuperior	Contours detected: 2	Expected: 1

	- Glyph name: onequarter	Contours detected: 5	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 4	Expected: 3

	- Glyph name: threequarters	Contours detected: 5	Expected: 3 or 4

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Germandbls	Contours detected: 2	Expected: 1

	- Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni203D	Contours detected: 4	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2

	- Glyph name: fl	Contours detected: 3	Expected: 1 or 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

	- Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 3	Expected: 2

	- Glyph name: lira	Contours detected: 2	Expected: 1

	- Glyph name: onehalf	Contours detected: 4	Expected: 3

	- Glyph name: onequarter	Contours detected: 5	Expected: 3 or 4

	- Glyph name: threequarters	Contours detected: 5	Expected: 3 or 4

	- Glyph name: uni203D	Contours detected: 4	Expected: 2

	- Glyph name: uni26AE	Contours detected: 5	Expected: 3

	- Glyph name: uni2E18	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 766 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 664:
logicalnot
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 acutecomb (U+0301), gravecomb (U+0300), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0326 (U+0326), uni0327 (U+0327) and uni0328 (U+0328) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0361 (U+0361) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* A (U+0041): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Aacute (U+00C1): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Abreve (U+0102): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Acircumflex (U+00C2): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Adieresis (U+00C4): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Agrave (U+00C0): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Amacron (U+0100): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Aogonek (U+0104): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Aring (U+00C5): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Atilde (U+00C3): L<<506.0,211.0>--<399.0,211.0>> -> L<<399.0,211.0>--<291.0,211.0>>

	* Euro (U+20AC): L<<159.0,312.0>--<196.0,312.0>> -> L<<196.0,312.0>--<233.0,312.0>>

	* Euro (U+20AC): L<<188.0,431.0>--<230.0,431.0>> -> L<<230.0,431.0>--<271.0,432.0>>

	* Euro (U+20AC): L<<728.0,312.0>--<708.0,282.0>> -> L<<708.0,282.0>--<688.0,252.0>>

	* Euro (U+20AC): L<<767.0,372.0>--<539.0,372.0>> -> L<<539.0,372.0>--<310.0,372.0>>

	* Euro (U+20AC): L<<913.0,591.0>--<895.0,564.0>> -> L<<895.0,564.0>--<877.0,538.0>>

	* Scedilla (U+015E): L<<341.0,-18.0>--<338.0,-30.0>> -> L<<338.0,-30.0>--<335.0,-41.0>>

	* at (U+0040): L<<552.0,256.0>--<575.0,349.0>> -> L<<575.0,349.0>--<599.0,443.0>>

	* cent (U+00A2): L<<405.0,408.0>--<357.0,218.0>> -> L<<357.0,218.0>--<310.0,29.0>>

	* g (U+0067): L<<348.0,123.0>--<373.0,223.0>> -> L<<373.0,223.0>--<398.0,323.0>>

	* gbreve (U+011F): L<<348.0,123.0>--<373.0,223.0>> -> L<<373.0,223.0>--<398.0,323.0>>

	* gcedilla (U+0123): L<<348.0,123.0>--<373.0,223.0>> -> L<<373.0,223.0>--<398.0,323.0>>

	* gdotaccent (U+0121): L<<348.0,123.0>--<373.0,223.0>> -> L<<373.0,223.0>--<398.0,323.0>>

	* lira (U+20A4): L<<505.0,356.0>--<457.0,356.0>> -> L<<457.0,356.0>--<409.0,356.0>>

	* plus (U+002B): L<<153.0,269.0>--<292.0,269.0>> -> L<<292.0,269.0>--<431.0,269.0>>

	* plusminus (U+00B1): L<<377.0,61.0>--<408.0,184.0>> -> L<<408.0,184.0>--<438.0,307.0>>

	* uni0E3F (U+0E3F): L<<373.0,45.0>--<410.0,191.0>> -> L<<410.0,191.0>--<446.0,337.0>>

	* uni203D (U+203D): L<<397.0,334.0>--<382.0,287.0>> -> L<<382.0,287.0>--<366.0,239.0>>

	* uni20A6 (U+20A6): L<<151.0,435.0>--<208.0,436.0>> -> L<<208.0,436.0>--<266.0,436.0>>

	* uni20A6 (U+20A6): L<<424.0,399.0>--<365.0,399.0>> -> L<<365.0,399.0>--<305.0,399.0>>

	* uni20A6 (U+20A6): L<<509.0,436.0>--<590.0,436.0>> -> L<<590.0,436.0>--<671.0,436.0>>

	* uni20A9 (U+20A9): L<<1002.0,399.0>--<956.0,399.0>> -> L<<956.0,399.0>--<910.0,399.0>>

	* uni20A9 (U+20A9): L<<550.0,436.0>--<582.0,494.0>> -> L<<582.0,494.0>--<613.0,553.0>>

	* uni20A9 (U+20A9): L<<577.0,399.0>--<535.0,320.0>> -> L<<535.0,320.0>--<492.0,242.0>>

	* uni20A9 (U+20A9): L<<619.0,399.0>--<598.0,399.0>> -> L<<598.0,399.0>--<577.0,399.0>>

	* uni20A9 (U+20A9): L<<714.0,436.0>--<799.0,436.0>> -> L<<799.0,436.0>--<884.0,436.0>>

	* uni20A9 (U+20A9): L<<953.0,205.0>--<879.0,205.0>> -> L<<879.0,205.0>--<805.0,205.0>>

	* uni2422 (U+2422): L<<188.0,503.0>--<202.0,558.0>> -> L<<202.0,558.0>--<216.0,613.0>>

	* yen (U+00A5): L<<355.0,399.0>--<277.0,399.0>> -> L<<277.0,399.0>--<198.0,399.0>>

	* yen (U+00A5): L<<449.0,436.0>--<506.0,436.0>> -> L<<506.0,436.0>--<564.0,436.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters _should_ disappear in other cases, for example: ĩ ĭ i̇ ǐ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ ĵ j̆ j̇ j̊

Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers). 

Your font does *not* cover the following languages that require the soft-dotted feature: Aghem (Latn, 38,843 speakers), Navajo (Latn, 166,319 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Basaa (Latn, 332,940 speakers), Belarusian (Cyrl, 10,064,517 speakers), Igbo (Latn, 27,823,640 speakers). [code: soft-dotted]
</div></details><br></div></details>

### Summary

| 💔 ERROR | ☠ FATAL | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 4 | 26 | 244 | 13 | 205 |
| 0% | 0% | 1% | 5% | 50% | 3% | 42% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
