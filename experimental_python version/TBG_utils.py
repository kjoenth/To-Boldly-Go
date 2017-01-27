#Constant
G = 6.674e-11

import math

def solarMass2kg(SM):
	#use Sol's solar mass and kg mass to convert
	#Sol is ~1.989e30kg
	return 1.989e30 * SM

def kg2solarMass(the_kg):
	#use Sol's solar mass and kg mass to convert
	#Sol is ~1.989e30kg
	return the_kg/1.989e30

def sol2Kerbol_kg(the_kg):
	#The start Kerbol is 113.2393x less massiv than Sol
	return the_kg/113.2393

def kerbol2Sol_kg(the_kg):
	#The start Kerbol is 113.2393x less massiv than Sol
	return the_kg*113.2393

def sol2Kerbol_km(the_km):
	#The start Kerbol is 2.6594x smaller in radius than Sol
	return the_km/2.6594

def kerbol2Sol_km(the_km):
	#The start Kerbol is 2.6594x smaller in radius than Sol
	return the_km*2.6594

def solarRadius2km(SR):
	#use Sol's solar radius and km radius to convert
	#Sol is ~695700km
	return 695700.0 * SR

def km2solarRadius(SR):
	#use Sol's solar radius and km radius to convert
	#Sol is ~695700km
	return SR/695700.0

def solarRadiusFromSolarMass(SM):
	#need a good reference for this
	if SM < 1:
		SR = SM**0.5
	else:
		SR = SM**0.8 
	return SR

def luminocityFromSolarMass(SM):
	return SM**3.5

def solarTemp(SL, SR):
	#returns star temp in K from solar luminocty and solar mass
	return ((SL/SR**2)**0.25)*5778

def starCircumference(radius_km):
	return 2.0*math.pi*radius_km

def starSurfaceArea(radius_km):
	return 4.0*math.pi*(radius_km**2.0)

def starVolume(radius_km):
	#return in m^3
	radius_m=radius_km * 1000.0
	return (4.0/3.0)*math.pi*(radius_m**3)

def starDensity(mass_kg, radius_km):
	theVolume=starVolume(radius_km)
	return mass_kg/theVolume

def stdGravitationalParameter(mass_kg):
	#https://en.wikipedia.org/wiki/Standard_gravitational_parameter
	return (mass_kg*G)

def surfaceGravity(mass_kg, radius_km):
	#https://en.wikipedia.org/wiki/Surface_gravity
	return G*(mass_kg/(radius_km**2.0))

def escapeVelocity(mass_kg, radius_km):
	temp = 2.0*G*mass_kg
	temp = temp/radius_km
	return temp**0.5

#star colour RGB from temp
def temp2RGB(tmpKelvin):
	#From http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/ Retrieved 2017.0110
	#Start with a temperature, in Kelvin, somewhere between 1000 and 40000.  (Other values may work,
	#but I can't make any promises about the quality of the algorithm's estimates above 40000 K.)
	#Note also that the temperature and color variables need to be declared as floating-point.

	#tmpKelvin = 113017

	#Temperature must fall between 1000 and 40000 degrees
	if tmpKelvin < 1000 : tmpKelvin = 1000
	#if tmpKelvin > 40000 : tmpKelvin = 40000

	#All calculations require tmpKelvin \ 100, so only do the conversion once
	tmpKelvin = tmpKelvin // 100

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
	return [r, g, b]

def hexColour2Fraction(theValue):
	return theValue/255.0

def RGB2HTMLColor(rgb_tuple):
	#convert an [R, G, B] tuple to #RRGGBB 
	hexcolor = '#%02x%02x%02x' % (rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
	# that's it! '%02x' means zero-padded, 2-digit hex values
	return hexcolor

def hillSphere(mass_primary, mass_secondary, eccentricity_secondary, semimajorAxis_secondary):
    #calculate the radius of the Hill sphere
    #https://en.wikipedia.org/wiki/Hill_sphere
    partOne = (semimajorAxis_secondary*(1-eccentricity_secondary))
    partTwo = (mass_secondary/(3*mass_primary))**(1.0/3.0)
    theRadius = partOne*partTwo
    #for unit test later:
    #mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; semi-major axis earth = 149,598,023 km; eccentricity earth = 0.0167086
    #gives a radius of 1471536.617 km
    #mass blackhole @ center of milky way: 8.55E+37 kg
    return theRadius

def rocheLimit(mass_primary, mass_secondary, radius_secondary):
    #calculate the Roche limit around a body
    #this is the minimum distance around a primary that a secondary can maintain cohesion
    #Any closer and you would have a ring instead
    #https://en.wikipedia.org/wiki/Roche_limit
    theDistance = 1.26 * radius_secondary *((mass_primary/mass_secondary)**(1.0/3.0))
    #for unit test later:
    #mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; radius earth = 6378 km
    #gives a radius of 1471536.617 km
    return theDistance

def kspSOI(mass_primary, mass_secondary, semimajorAxis_secondary):
	#http://wiki.kerbalspaceprogram.com/wiki/Sphere_of_influence
	return (semimajorAxis_secondary*((mass_secondary/mass_primary)**(2.0/5.0)))

def siderealRotationalVel(theRadius, rotationalPeriod):
	theVelocity = starCircumference(theRadius)/rotationalPeriod
	return theVelocity

def synchronousOrbit(theRadius, theMass, rotationalPeriod):
	#returns the altitude of geosync orbit above sea level
	tmpOne = (G*theMass*(rotationalPeriod**2))
	tmpTwo = 4.0*(math.pi**2)
	tmpThr = (tmpOne/tmpTwo)**(1.0/3.0)
	theAltitude = tmpThr-theRadius
	return theAltitude 

import unittest

class TestStringMethods(unittest.TestCase):

	#unit tests
	def test_solarMass2kg(self):
		self.assertAlmostEqual(1.7565E+30, solarMass2kg(0.883085767), delta=1e26)

	def test_kg2solarMass(self):
	 	self.assertAlmostEqual(0.883085767, kg2solarMass(1.7565E+30), delta=1e26)

	def test_sol2Kerbol_kg(self):
		self.assertAlmostEqual(3.5323E+26, sol2Kerbol_kg(4.00E+28), delta=1e26)

	def test_kerbol2Sol_kg(self):
		self.assertAlmostEqual(4.00E+28, kerbol2Sol_kg(3.5323E+26), delta=1e26)

	def test_solarRadius2km(self):
		self.assertAlmostEqual(614362.7681, solarRadius2km(0.883085767), 4)

	def test_km2solarRadius(self):
		self.assertAlmostEqual(0.883085767, km2solarRadius(614362.7681), 4)

	def test_solarRadiusFromSolarMass(self):
		self.assertAlmostEqual(1.3, solarRadiusFromSolarMass(1.4), 1)

	def test_solarRadiusFromSolarMass(self):
		self.assertAlmostEqual(0.9, solarRadiusFromSolarMass(0.8), 1)

	def test_luminocityFromSolarMass(self):
		self.assertAlmostEqual(3.2, luminocityFromSolarMass(1.4), 1)

	def test_solarTemp(self):
		SL = luminocityFromSolarMass(1.4)
		SR = solarRadiusFromSolarMass(1.4)
		self.assertAlmostEqual(1.25, solarTemp(SL, SR), 1)

	def test_temp2RGB(self):
		self.assertAlmostEqual(130.19338965804405, temp2RGB(6500)[0], 4)
		self.assertAlmostEqual(170.1426595731383, temp2RGB(6500)[1], 4)
		self.assertAlmostEqual(255.0, temp2RGB(6500)[2], 4)

	def test_hexColour2Fraction(self):
		self.assertAlmostEqual(0.5098, hexColour2Fraction(130.0), 4)

	def test_starCircumference(self):
		self.assertAlmostEqual(1643681.2763581797, starCircumference(261600), 4)

	def test_starSurfaceArea(self):
		self.assertAlmostEqual(859974043790.5996, starSurfaceArea(261600), 1)

	def test_starVolume(self):
		self.assertAlmostEqual(7.498973661854028e+25, starVolume(261600), 1)

	def test_starDensity(self):
		self.assertAlmostEqual(234.23817434314282, starDensity(1.7565459e28, 261600), 4)

	def test_stdGravitationalParameter(self):
		self.assertAlmostEqual(1.1723328e18, stdGravitationalParameter(1.7565459e28), delta=1e26)

	def test_surfaceGravity(self):
		#radius should be in meters
		r = 261600*1000
		self.assertAlmostEqual(17.1, surfaceGravity(1.7565459e28, r), 1)

	def test_escapeVelocity(self):
		self.assertAlmostEqual(94672.01, escapeVelocity(1.7565459e28, 261600), delta=1e26)

if __name__ == '__main__':
    unittest.main()