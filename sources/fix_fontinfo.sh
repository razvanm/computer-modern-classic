#!/bin/bash

# UFO parsers don't like empty integer values.
cat $1 | sed -e '/<integer></d' > $1.sed
mv $1.sed $1
