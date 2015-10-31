#!/usr/bin/python

import sys

from sense_hat import SenseHat

sense = SenseHat()

O = [0, 0, 0]

for index in range(len(sys.argv)):
	if "--on" == sys.argv[index]:
		O = [0, 100, 0]

led = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(led)
