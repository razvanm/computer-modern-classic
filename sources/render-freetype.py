#!/usr/bin/env python

"""Produce B/W images for all the glyphs in a font using FreeType."""

import argparse
import os.path

import freetype
from PIL import Image


def single_glyph(font, glyph_unicode):
  """Render a single glyph."""

  font.load_char(
      glyph_unicode, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_TARGET_MONO
  )
  bitmap = font.glyph.bitmap
  if args.verbose:
    print('\tglyph unicode:', glyph_unicode)
    print('\twidth:', bitmap.width)
    print('\trows:', bitmap.rows)
    print('\tpitch:', bitmap.pitch)
    print('\tpixel_mode:', bitmap.pixel_mode)
    print('\tbuffer size:', len(bitmap.buffer))

  img = Image.new('1', (bitmap.width, bitmap.rows))
  (x, y) = (0, 0)
  i = 0
  for b in bitmap.buffer:
    for _ in range(8):
      # Note that 1 indicates white.
      bit = 1 if b & 0x80 else 0
      if x < bitmap.width:
        img.putpixel((x, y), bit)
      b = b << 1
      x += 1
    i += 1
    if i % bitmap.pitch == 0:
      x = 0
      y += 1

  if args.verbose:
    print('\tBbox:', img.getbbox())
  return img.crop(img.getbbox())


def main():
  font = freetype.Face(args.font_file)
  font.set_char_size(args.size)
  for c, i in font.get_chars():
    glyph_name = font.get_glyph_name(i).decode('utf-8')
    print('%d: %s U+%04X' % (i, glyph_name, c))
    img = single_glyph(font, c)
    img.save(
        os.path.join(
            args.output_dir, '%03d.%s.U+%04X.png' % (i, glyph_name, c)
        )
    )

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Render all the glyphs in B/W to a file.'
  )
  parser.add_argument('-v', '--verbose', action='store_true')
  parser.add_argument('--size', help='Size of the glyph', default=1000*64)
  parser.add_argument('font_file', help='Font file (typically, a .ttf file)')
  parser.add_argument('output_dir', help='Output directory')
  args = parser.parse_args()
  main()
