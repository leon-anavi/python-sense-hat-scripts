# python-sense-hat-text
Command line python tools for:
* printing custom text wuth custom color on Raspberry Pi Sense Hat
* printing temperature and humidity

##Usage


### Text ####

Specify custom text and color, for example:

````
./python-sense-hat-text.py --text "Hello, World!" --color-red 0 --color-green 0 --color-blue 200
```

If not specified the default text is "Hello" and the default color is red.

### Temperature & Humidity ###

Print the current temperature and humidity:

````
./python-sense-hat-temp-hum.py
````
