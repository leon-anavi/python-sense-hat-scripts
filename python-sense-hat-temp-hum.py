#!/usr/bin/python

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature_from_pressure()
temp = round(temp, 1)
print("Temperature: %s C" % temp)

humidity = sense.get_humidity()
humidity = round(humidity, 2)
print("Humidity: %s %%rH" % humidity)
