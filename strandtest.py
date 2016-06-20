#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

numpixels = 8

datapin   = 23
clockpin  = 24
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()
strip.setBrightness(64)
strip.clear()
strip.show()

colours = [0x00FF00, 0xFF0000, 0x0000FF, 0xFFFFFF]

for i in range(len(colours)):
    for j in range(8):
        strip.setPixelColor(j, colours[i]) # Turn on 'head' pixel
    strip.show()                     # Refresh strip
    time.sleep(2)             # Pause 20 milliseconds (~50 fps)

strip.clear()
strip.show()
