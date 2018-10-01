import math

# def AU2km(theAU):
#     AU2km = theAU * 149597871


# def realKM2kerbinKM(realKM):
#     #from discussion with Gregrox on Kopernicus discord
#     #one way to convert to/from kerbin space is:
#     #Earth SMA/Kerbin SMA = 10.9999726
#     realKM2kerbinKM = realKM / 10.9999726

# def kerbinKM2realKM(kerbinKM):
#     #from discussion with Gregrox on Kopernicus discord
#     #one way to convert to/from kerbin space is:
#     #Earth SMA/Kerbin SMA = 10.9999726
#     kerbinKM2realKM = kerbinKM * 10.9999726


# def realKM2Parsec(realKM):
#     #1 km = 3.2407792896664E-14 pc
#     realKM2Parsec = realKM*3.2407792896664E-14


# def solarMass2kg(SM):
#     #use Sol's solar mass and kg mass to convert
#     #Sol is ~1.989e30kg
#     solarMass2kg = 1.98855E30 * SM


def kg2solarMass(the_kg):
    #use Sol's solar mass and kg mass to convert
    #Sol is ~1.989e30kg
    return the_kg / 1.98855E30

def sol2Kerbol_kg(the_kg):
    #The start Kerbol is 113.2393x less massiv than Sol
    return the_kg / 113.2393


# def kerbol2Sol_kg(the_kg):
#     #The start Kerbol is 113.2393x less massiv than Sol
#     kerbol2Sol_kg = the_kg * 113.2393


def sol2Kerbol_km(the_km):
    #The start Kerbol is 2.6594x smaller in radius than Sol
    return the_km / 2.6594


# def kerbol2Sol_km(the_km):
#     #The start Kerbol is 2.6594x smaller in radius than Sol
#     kerbol2Sol_km = the_km * 2.6594


def solarRadius2km(SR):
    #use Sol's solar radius and km radius to convert
    #Sol is ~695700km
    return 695700.0 * SR


# def km2solarRadius(SR):
#     #use Sol's solar radius and km radius to convert
#     #Sol is ~695700km
#     km2solarRadius = SR / 695700.0


def solarRadiusFromSolarMass(SM):
    #need a good reference for this
    if SM <= 1:
        SR = SM**0.5
    else:
        SR = SM**0.8

    return SR


def luminosityFromSolarMass(SM):
    return SM**3.5


def absMagFromLuminosity(theLuminosity):
    #ratioLum = theLuminosity/78.70
    #theLogTen# = log(ratioLum)/log(10.#)
    #return -2.5 * theLogTen#
    return -2.5*math.log10(theLuminosity/78.70)


# def apparentMagFromAbsMag(absMag, theDistance):
#     #the Distance has to be in parsecs
#     apparentMagFromAbsMag=5*LOG(theDistance/10)+absMag


# def solarTemp(SL, SR):
#     #returns star temp in K from solar luminocty and solar mass
#     solarTemp =((SL /(SR ^ 2.0)) ^ 0.25) * 5778


# def starCircumference(radius_km):
#     starCircumference = 2.0 * _PI * radius_km


# def starSurfaceArea(radius_km):
#     starSurfaceArea = 4.0 * _PI *(radius_km ^ 2.0)


# def starVolume(radius_km):
#     #return in m^3
#     radius_m = radius_km * 1000.0
#     starVolume =(4.0 / 3.0) * _PI *(radius_m ^ 3.0)


# def starDensity(mass_kg, radius_km):
#     theVolume = starVolume(radius_km)
#     starDensity = mass_kg / theVolume


# def stdGravitationalParameter(mass_kg):
#     #https://en.wikipedia.org/wiki/Standard_gravitational_parameter
#     G = 6.674E-11
#     stdGravitationalParameter =(mass_kg * G)


# def surfaceGravity(mass_kg, radius_km):
#     #https://en.wikipedia.org/wiki/Surface_gravity
#     G = 6.674E-11
#     surfaceGravity = G *(mass_kg /(radius_km ^ 2.0))


# def escapeVelocity(mass_kg, radius_km):
#     G = 6.674E-11
#     temp = 2.0 * G * mass_kg
#     temp = temp / radius_km
#     escapeVelocity = temp ^ 0.5


# def hillSphere(mass_primary, mass_secondary, eccentricity_secondary, semimajorAxis_secondary):
#     #calculate the radius of the Hill sphere
#     #https://en.wikipedia.org/wiki/Hill_sphere
#     partOne =(semimajorAxis_secondary *(1.0 - eccentricity_secondary))
#     partTwo =(mass_secondary /(3.0 * mass_primary)) ^(1.0 / 3.0)
#     theRadius = partOne * partTwo
#     #for unit test later:
#     #mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; semi-major axis earth = 149,598,023 km; eccentricity earth = 0.0167086
#     #gives a radius of 1471536.617 km
#     #mass blackhole @ center of milky way: 8.55E+37 kg
#     hillSphere = theRadius


# def simpleRocheLimit(mass_primary):
#     #If the orbiting body does not have a mass or radius provided
#     #the standard roche limit calc can't be used'
#     #use this dogshit instead.
#     #returns units in km
#     simpleRocheLimit =(7.52E-24)*mass_primary


# def rocheLimit(mass_primary, mass_secondary, radius_primary, radius_secondary):
#     #calculate the Roche limit around a body
#     #this is the minimum distance around a primary that a secondary can maintain cohesion
#     #Any closer and you would have a ring instead
#     #https://en.wikipedia.org/wiki/Roche_limit
#     densityPrimary = starDensity(mass_primary, radius_primary/1000.0) #mass in kg, radius in km so divide by 1000
#     densitySecondary = starDensity(mass_secondary, radius_secondary/1000.0) #mass in kg, radius in km so divide by 1000
#     theDistance = 1.26 * radius_primary*((densityPrimary/densitySecondary)^(1.0/3.0))
#     #for unit test later:
#     #mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; radius earth = 6378 km
#     #gives a radius of 556,396.86 km
#     rocheLimit = theDistance


# def kspSOI(mass_primary, mass_secondary, semimajorAxis_secondary):
#     #http://wiki.kerbalspaceprogram.com/wiki/Sphere_of_influence
#     kspSOI =(semimajorAxis_secondary *((mass_secondary / mass_primary) ^(2.0 / 5.0)))


# def solFrostLine(luminocity):
#     #https://en.wikipedia.org/wiki/Frost_line_(astrophysics):
#     solFrostLine = 4.85 *(luminocity ^ 0.5) #returns units in AU

# def siderealRotationalVel(theRadius, rotationalPeriod):
#     theVelocity = starCircumference(theRadius) / rotationalPeriod
#     siderealRotationalVel = theVelocity


# def synchronousOrbit(theRadius, theMass, rotationalPeriod):
#     #returns the altitude of geosync orbit above sea level
#     G = 6.674E-11
#     tmpOne =(G * theMass *(rotationalPeriod ^ 2.0))
#     tmpTwo = 4.0 *(_PI ^ 2.0)
#     tmpThr =(tmpOne / tmpTwo) ^(1.0 / 3.0)
#     theAltitude = tmpThr - theRadius
#     synchronousOrbit = theAltitude


def pol2cartY(rho, theta):
    #theta is in degrees
    return rho * math.sin(math.radians(theta))

def pol2cartX(rho, theta):
    #theta is in degrees
    return rho * math.cos(math.radians(theta))


def theStarDistance(x1,x2,y1,y2):
    theStarDistance =(((x2-x1)**2)+((y2-y1)**2))**0.5
    return theStarDistance

# #star colour RGB from temp
# def temp2RGB(tmpKelvin):
#     #temps in kelvins
#     #line equations derived using blackbody values from
#     #http://www.vendian.org/mncharity/dir3/blackbody/UnstableURLs/bbr_color.html

#     if tmpKelvin<1900 then b = 0
#     if tmpKelvin>=1900 and tmpKelvin<=6600 then
#         b = int(-1479.374+(196.95357*log(tmpKelvin)))
#     end if
#     if tmpKelvin<=6600 then 
#         r = 255  
#         g = int(2.71828^(5.7834281-(1686.3889*(1.0/tmpKelvin))))
#     end if
#     if tmpKelvin>6600 then
#         r = int(1.0/(0.0066897-(18.585712*(1.0/tmpKelvin))))
#         g = int(1.0/(0.0057629-(11.79832*(1.0/tmpKelvin))))
#         b = 255
#     end if
#     REDgb = r
#     rGREENb = g
#     rgBLUE = b