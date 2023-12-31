# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image1.py --output documentation/image1.png

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 2048, 128, 1
FONT_PATH = "fonts/ttf/ComputerModernClassic-Italic.ttf"
FONT_LICENSE = "OFL v1.1"
AUXILIARY_FONT = "Helvetica"
AUXILIARY_FONT_SIZE = 48
GLYPH_SIZE = 128
GRID_VIEW = True # Change this to "True" for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Constants that are worked out dynamically
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)


# Draws a grid
def grid():
    stroke(0, 0, 0, 0.10)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, MARGIN
    INCREMENT_X, INCREMENT_Y = MARGIN, MARGIN
    for x in range(19):
        polygon((MARGIN + STEP_X, MARGIN * 2), (MARGIN + STEP_X, HEIGHT - MARGIN * 2))
        STEP_X += INCREMENT_X
    for y in range(19):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    # Use the background color from Knuth's web page: #F8F4E7.
    fill(0xF8/256.0, 0xF4/256.0, 0xE7/256.0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
def draw_main_text():
    fill(0)
    stroke(None)
    font(FONT_PATH)
    fontSize(GLYPH_SIZE*0.8)
    x = MARGIN
    y = HEIGHT - MARGIN * 2 - GLYPH_SIZE
    for (unicode, name) in ttFont.getBestCmap().items():
        text(chr(unicode), (x+GLYPH_SIZE/2, y), align="center")
        x += GLYPH_SIZE
        if (x + GLYPH_SIZE) > (WIDTH - MARGIN):
            y -= GLYPH_SIZE
            x = MARGIN

# Divider lines
def draw_divider_lines():
    stroke(0)
    strokeWidth(4)
    lineCap("round")
    line((MARGIN, HEIGHT - MARGIN), (WIDTH - MARGIN, HEIGHT - MARGIN))
    line((MARGIN, MARGIN + (MARGIN / 2)), (WIDTH - MARGIN, MARGIN + (MARGIN / 2)))
    stroke(None)


# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text():
    # Setup
    font(AUXILIARY_FONT)
    fontSize(AUXILIARY_FONT_SIZE)
    POS_TOP_LEFT = (MARGIN, HEIGHT - MARGIN * 1.5)
    POS_TOP_RIGHT = (WIDTH - MARGIN, HEIGHT - MARGIN * 1.5)
    POS_BOTTOM_LEFT = (MARGIN, MARGIN)
    POS_BOTTOM_RIGHT = (WIDTH - MARGIN * 0.95, MARGIN)
    URL_AND_HASH = MY_URL + "at commit " + MY_HASH
    URL_AND_HASH = URL_AND_HASH.replace("\n", " ")
    # Draw Text
    text(FONT_NAME, POS_TOP_LEFT, align="left")
    text(FONT_VERSION, POS_TOP_RIGHT, align="right")
    text(URL_AND_HASH, POS_BOTTOM_LEFT, align="left")
    text(FONT_LICENSE, POS_BOTTOM_RIGHT, align="right")


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    draw_divider_lines()
    draw_auxiliary_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
