# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import board, neopixel
from animations import *

pixel_pin = board.D18
num_pixels = 30

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def kb_interrupt(func):
    def wrapper():
        try:
            func
        except KeyboardInterrupt:
            print('Halted by user.')
            color_chase(BLACK,0.1)
    return wrapper

