#From http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/ Retrieved 2017.0110
#Start with a temperature, in Kelvin, somewhere between 1000 and 40000.  (Other values may work,
#but I can't make any promises about the quality of the algorithm's estimates above 40000 K.)
#Note also that the temperature and color variables need to be declared as floating-point.

import math
tmpKelvin = 113017

#Temperature must fall between 1000 and 40000 degrees
if tmpKelvin < 1000 : tmpKelvin = 1000
#if tmpKelvin > 40000 : tmpKelvin = 40000

#All calculations require tmpKelvin \ 100, so only do the conversion once
tmpKelvin = tmpKelvin // 100
print tmpKelvin 

#Calculate Red:
if tmpKelvin <= 66:
  r = 255
else:
  r = tmpKelvin - 60
  r = 329.698727446 * (r**-0.1332047592)
  if r < 0: r = 0
  if r > 255: r = 255

#Calculate Green:
if tmpKelvin <= 66:
  g = tmpKelvin
  g = 99.4708025861 * math.log(g) - 161.1195681661
  if g < 0 : g = 0
  if g > 255 : g = 255
else:
  g = tmpKelvin - 60
  g = 288.1221695283 * (g**-0.0755148492)
  if g < 0 : g = 0
  if g > 255 : g = 255

#Calculate Blue:
if tmpKelvin >= 66:
  b = 255
else:
  if tmpKelvin <= 19:
    b = 0
  else:
    b = tmpKelvin - 10
    b = 138.5177312231 * math.log(b) - 305.0447927307
    if b < 0: b = 0
    if b > 255: b = 255

print [r, g, b]

#def RGBToHTMLColor(rgb_tuple):
""" convert an (R, G, B) tuple to #RRGGBB """
hexcolor = '#%02x%02x%02x' % (r,g,b)
# that's it! '%02x' means zero-padded, 2-digit hex values
#return hexcolor
print hexcolor