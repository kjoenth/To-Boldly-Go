#To Boldly Go v0.1 - Kopernicus Procedural Galaxy Generator! 
#Copyright (C) 2016  Daniel L. 
#
#This program is free software; you can redistribute it and/or modify 
#it under the terms of the GNU General Public License as published by 
#the Free Software Foundation; either version 2 of the License, or 
#(at your option) any later version. 
#
#This program is distributed in the hope that it will be useful, 
#but WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
#GNU General Public License for more details. 
#
#You should have received a copy of the GNU General Public License 
#along with this program; if not, write to the Free Software 
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA 

import random
import TBG_utils

global totNumbPlanets
global totNumbMoons

kerbolDesc = "The Sun is the most well known object in the daytime sky. Scientists have noted a particular burning sensation and potential loss of vision if it is stared at for long periods of time. This is especially important to keep in mind considering the effect shiny objects have on the average Kerbal."

interstellarData =\
"""
@Kopernicus:AFTER[Kopernicus]
{
 @Body[Sun]
 {
        cbNameLater = Interstellar Space
        @Properties
        {
         description = Interstellar Space is one of the vastest emptiest regions of the Universe, It takes thousands of years to travel just from one star to another at sublight speeds, And is nearly devoid of matter. There are occasional areas of dense gas however, Which are filled with stars. But we cannot track them due to nebula interference.
         radius = 10000
        }
        @ScaledVersion
        {
        Light
         {
             sunlightColor = 1,1,1,1.0
             sunlightIntensity = 0.55
             scaledSunlightColor = 1,1,1,1.0
             scaledSunlightIntensity = 0.55
             IVASunColor = 1,1,1,1.0
             IVASunIntensity = 0.55
             sunLensFlareColor = 1,1,1,1.0
             luminosity = 0
             ambientLightColor = 0,0,0,1.0
             givesOffLight = False
         }
         Material
         {
             emitColor0 = 0,0,0,1
             emitColor1 = 0,0,0,1
             sunspotColor = 0,0,0,1
             rimColor = 0,0,0,1
         }
         Coronas
            {
            Corona
            {
                rotation = 0
                speed = -1
                updateInterval = 5
                scaleLimitX = 5
                scaleLimitY = 5
                scaleSpeed = 0.007

                Material
                {
                    texture = To_Boldly_Go/Black
                    inverseFade = 2.553731
                }
            }
            Corona
            {
                rotation = 0
                speed = 1
                updateInterval = 5
                scaleLimitX = 5
                scaleLimitY = 5
                scaleSpeed = 0.009

                Material
                {
                      texture = To_Boldly_Go/Black
                      inverseFade = 2.553731
                }
            }
          }
     }
 }
 @Body[Moho]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
 @Body[Eve]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
 @Body[Kerbin]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
 @Body[Duna]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
 @Body[Dres]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
 @Body[Jool]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
 @Body[Eeloo]
 {
     @Orbit
     {
            @referenceBody = Kerbol
     }
 }
}
"""

propertiesTemplate=\
"""
        Properties
        {
            description = %s
            radius = %i
            sphereOfInfluence = %i
        }
"""

orbitTemplate=\
"""
        Orbit
        {
            referenceBody = %s
            color = %%s
            inclination = %i //Orbit inclination relative to referenceBody's equator
            eccentricity = %f //Orbit eccentricity, how elliptical is the orbit
            semiMajorAxis = %i //Average distance to reference body
            //longitudeOfAscendingNode = 0 //Position of ascending node relative to the surface of the reference body
            argumentOfPeriapsis = %i 
            //meanAnomalyAtEpoch = 0
            //epoch = %i //Position of your planet when it is first loaded. Can be used to make trojans
            %%s           
        }
"""

lightTemplate=\
"""
            Light
            {
                sunlightColor = %s
                sunlightIntensity = %f
                scaledSunlightColor = %s
                scaledSunlightIntensity = %f
                IVASuncolor = %s
                IVASunIntensity = %f
                sunLensFlareColor = %s
                ambientLightColor = %s
                sunAU = %i
                luminosity = 0
            }
"""

materialTemplate=\
"""
            Material
            {
                emitColor0 = %s
                emitColor1 = %s
                sunspotColor = %s
                rimColor = %s
            }
"""

coronasTemplate=\
"""
            Coronas
            {
                Corona
                {
                    rotation = 0
                    speed = -1
                    updateInterval = 5
                    scaleLimitX = 5
                    scaleLimitY = 5
                    scaleSpeed = 0.007
                    Material
                    {
                        texture = To_Boldly_Go/%sCorona
                        inverseFade = 2.553731
                    }
                }
                Corona
                {
                    rotation = 0
                    speed = 1
                    updateInterval = 5
                    scaleLimitX = 5
                    scaleLimitY = 5
                    scaleSpeed = 0.009
                    Material
                    {
                        texture = To_Boldly_Go/%sCorona
                        inverseFade = 2.553731
                    }
                }
            }
"""

starTemplate=\
"""
@Kopernicus
{
    Body
    {
        name = %(theStarName)s
        Template
        {
            name = Sun
        }
        %(theProperties)s
        %(theOrbitData)s
        ScaledVersion
        {
            %(theLightData)s
            %(theMaterialData)s
            %(theCoronasData)s
        }
    }
    %%(planetBodies)s
}
"""

planetBodyTempate=\
"""
    Body
    {
        name = %s %s
        Orbit
        {
            referenceBody = %s
            //color =  //RGB brightness
            inclination = %i //Orbit inclination relative to referenceBody's equator
            eccentricity = %f //Orbit eccentricity, how elliptical is the orbit
            semiMajorAxis = %i //Average distance to reference body
            //longitudeOfAscendingNode = 0 //Position of ascending node relative to the surface of the reference body
            argumentOfPeriapsis = %i 
            //meanAnomalyAtEpoch = 0
            //epoch = %i //Position of your planet when it is first loaded. Can be used to make trojans
            %s
        }
        Template
        {
            name = %s
        }
        %%(ScaledVersion)s
        Properties
        {
            description = %s
            radius = %i 
        }
        %%(theRings)s
    }
"""

ringsTemplate=\
"""
         Rings
         {
             Ring
             {
                 angle = 0
                 outerRadius = 3000
                 innerRadius = 2000
                 texture = To_Boldly_Go/ringtextures/%s.png
                 color = 1.0,0.1,0.1,1.0
                 lockRotation = false
                 unlit = false
             }
          }
"""

gasGiantScaledVersion=\
"""
        ScaledVersion
        {
            Material
            {
                texture = To_Boldly_Go/gastextures/- %s .jpg
            }
        }
"""

def orbitalValues(GTYPE):
    ###fill in orbital data
    if GTYPE == 1 or GTYPE == 2:
        theReferenceBody = "Sun"
        if GTYPE ==1:
            INCLINATION = random.randint(0,360)
        else:
            INCLINATION = random.randint(0, 25) #  int(random.random()*50)-25
        SEMIMAJORAXIS = random.randint(100000000000000, 10000000000000000)


    else:
        theReferenceBody = random.randint(0,CLUSTERNUM)
        INCLINATION = random.randint(0,360)
        SEMIMAJORAXIS = random.randint(0, 10000000000000)     
    ECCENTRICITY = random.random()
    ARGUMENTOFPERIAPSIS = random.randint(0,360)
    #EPOCH = int(random.random()*360)
    EPOCH = 0

    #theColor = "1,0,0,1"
    theOrbitData= orbitTemplate % (theReferenceBody, INCLINATION, ECCENTRICITY, SEMIMAJORAXIS, ARGUMENTOFPERIAPSIS, EPOCH)
    
    return theOrbitData




def generateStarNames(numbNames):
    #takes and integer and produces that number of star names
    f = open("Data_folder/TBG_Prefixes.txt")
    thePrefixes = f.read().splitlines()
    f.close()
    f = open("Data_folder/TBG_Suffixes.txt")
    theSuffixes = f.read().splitlines()
    f.close()

    starNameList=[]
    for starName in range (numbNames):
        PREFIX = random.choice(thePrefixes)
        SUFFIX = random.choice(theSuffixes)
        aStarName=PREFIX+SUFFIX
        starNameList.append(aStarName)
        #should probably have a function in here to make sure the name doesn't appear more than once.
    return starNameList

def readPlanetTemplates():
    #this is an embarassing mess
    #the idea is to read in planet radius AND 1 or more descriptions
    #if more than one description, random choose in later implementation
    f = open("Data_folder/TBG_Planet_Templates.txt")
    thePlanetTemplates = f.read().splitlines()
    f.close()
    planetDict={}
    for x in thePlanetTemplates:
        theListItems= x.split('\t')
        planetDict[theListItems[0]]=[int(theListItems[1]), int(theListItems[2]), theListItems[3:]]
    #print sorted(planetDict, key=lambda k: planetDict[k][0])
    #print planetDict.keys().index("Jool")
    return planetDict


def checkIfInt(theValue):
    try:
        int(theValue)
        return True
    except ValueError:
        return False

def makeABody(theParentName, PNM, planetTemplateName, planetDescription, planetRadius, parentRadius, parentSOI):
    #!!!!!!!!!!!!!
    #IMPORTANT: If a body is placed outside the primary's SOI, it will not actually orbit
    #!!!!!!!!!!!!!
    minDistFromParent=parentRadius+planetRadius+100000
    maxDistFromParent=parentSOI-planetRadius-100000
    INCLINATION = random.randint(0,10) # too extreme for me random.randint(0,360)
    ECCENTRICITY = random.randint(0,10)/100 #too much eccentricity will make orbits cross without complicated math checks
    #SEMIMAJORAXIS = random.randint(0,10000000000)+10000000 
    #limit max SEMIMAJORAXIS based on parent's SOI
    SEMIMAJORAXIS = random.randint(minDistFromParent,maxDistFromParent)
    ARGUMENTOFPERIAPSIS = 0 #random.randint(0,1000)
    #EPOCH = random.randint(0,360)
    EPOCH = 0
    #this could be expanded to deal with multiple possible descriptions
    #planetDescription = thePlanetDict[planetTemplateName][1][0]
    planetDescription = planetDescription % {"sN":theParentName, "rN":PNM}
    ########
    #I am deviating a bit from the original code when generating the radii
    #the original code had custom values for each planet. For example, planets 
    #based on Eeloo would have radii calculated as radius = INT(RND * 300000) + 70000
    #having custom values is a pain, and since I already am importing template
    #planet radii for later determination of possible moons, I'm going with a gausian
    #curve there the mean is the provided radius. For the std dev, I looked at all the 
    # "+x" values used in the orginal code, divided the real radius by that modifier, 
    #and then took that average. Its 2.65. Using that, I can say average =radius and
    #std dev=radius/2.65.
    #########
    #avgRadius=thePlanetDict[planetTemplateName][0]
    stdDev=planetRadius/2.65
    theRadius=int(random.gauss(planetRadius,stdDev))
    if planetTemplateName=="Jool":
        theScaledVersion=gasGiantScaledVersion % (random.randint(0,16))
    else: 
        theScaledVersion=""
    thePlanetBody = planetBodyTempate % (theParentName, PNM, theParentName, INCLINATION, ECCENTRICITY, SEMIMAJORAXIS, ARGUMENTOFPERIAPSIS, EPOCH, "", planetTemplateName, planetDescription, theRadius)
    #thePlanetBody = thePlanetBody % {"ScaledVersion":theScaledVersion}
    if (theRadius>0 and random.random()<=0.25): #25% chance of having a ring
        theRingData = ringsTemplate % (random.randint(1,3))
    else:
        theRingData = ""
    thePlanetBody = thePlanetBody % {"ScaledVersion":theScaledVersion, "theRings":theRingData}
    return thePlanetBody

def PENABLEISYES(parentRadius, parentSOI):
    global totNumbPlanets
    global totNumbMoons
    planetTxt=""
    maxPlanets = random.randint(1,5) #how many planets in this system? Max of 5
    PlanetNumb = 1
    for aPlanet in range(maxPlanets):
        if PlanetNumb == 1: PNM = "I"
        if PlanetNumb == 2: PNM = "II"
        if PlanetNumb == 3: PNM = "III"
        if PlanetNumb == 4: PNM = "IV"
        if PlanetNumb == 5: PNM = "V"
        planetTemplateName = random.choice(thePlanetDict.keys())
        planetRadius = thePlanetDict[planetTemplateName][0]
        planetSOI = thePlanetDict[planetTemplateName][1]
        planetDescription = thePlanetDict[planetTemplateName][2][0]    
        planetBody=makeABody(theStarName, PNM, planetTemplateName, planetDescription, planetRadius, parentRadius, parentSOI) #this will be the same routine used to make both planets and moons
        #print planetBody
        planetTxt=planetTxt+planetBody
        if planetTemplateName!="Gilly":
            maxMoons=random.randint(1,4)
            moonNumb=1
            theParentName=theStarName+" "+PNM
            for aMoon in range(maxMoons):
                # if moonNumb == 1: PNM = "a"
                # if moonNumb == 2: PNM = "b"
                # if moonNumb == 3: PNM = "c"
                # if moonNumb == 4: PNM = "d"
                # if moonNumb == 5: PNM = "e"
                PNM=str(moonNumb)
                sortedPlanetKeys=sorted(thePlanetDict, key=lambda k: thePlanetDict[k][0])
                if planetTemplateName=="Jool":
                    del sortedPlanetKeys[-1]
                else:
                    sortedPlanetKeys=['Gilly']
                #we can be way smarter about this
                #can sort the planet templates my radius
                #and then pick only bodies 40% size of parent
                #as potential moons
                moonTemplateName=random.choice(sortedPlanetKeys)
                moonRadius = thePlanetDict[moonTemplateName][0]
                moonDescription = thePlanetDict[moonTemplateName][2][0]

                #print theParentName
                #print PNM

                moonBody=makeABody(theParentName, PNM, moonTemplateName, moonDescription, moonRadius, planetRadius, planetSOI) #this will be the same routine used to make both planets and moons
                #print moonBody
                planetTxt=planetTxt+moonBody
                moonNumb=moonNumb+1
                totNumbMoons=totNumbMoons+1
        PlanetNumb=PlanetNumb+1
        totNumbPlanets=totNumbPlanets+1
    return planetTxt



BROWNSTARNUMBER = 1
REDSTARNUMBER = 1
YELLOWSTARNUMBER = 1
WHITESTARNUMBER = 1
BLUESTARNUMBER = 1
DWARFSTARNUMBER = 1
NEUTRONSTARNUMBER = 1
BLACKHOLENUMBER = 1
CLUSTERCORENUMBER = 1
CORESTARNUMBER = 1

saveDataFile =open("galaxy.cfg", 'w') #Creates the galaxy file
saveDataFile.close()

REDSTAR = ''
KSTAR = ''
YELLOWSTAR = ''
BLUESTAR = ''
WHITESTAR = ''
BROWNSTAR = ''
DWARFSTAR = ''
BLACKHOLE = ''
ROGUE = ''

theTotalFileText=""

CLUSTERNUM = 0
PENABLE = raw_input("Planets? (y/n):") #Asks the user whether they want to have planets or not
if PENABLE == "y":
    thePlanetDict=readPlanetTemplates()
    #print thePlanetDict
#ASTTOG = raw_input( " ASTEROIDS (y/n):") #Asks the user whether they want to have asteroids or not

print "Galaxy Type:"
GTYPE = 4
while GTYPE>3:
    GTYPE = input(" ELLIPSE, DISK (1,2): ") #Asks the user what kind of galaxy they want.

if GTYPE == 3:
    CLUSTER = raw_input( " # CLUSTERS: ",) #Asks the user how many star clusters they want

while checkIfInt(REDSTAR)==False:
    REDSTAR = raw_input( " # RED STARS: ") #Asks the user how many red stars they want to generate.
REDSTAR = int(REDSTAR)

while checkIfInt(KSTAR)==False:
    KSTAR = raw_input( " # ORANGE STARS: ") #Asks the user how many orange stars they want to generate.
KSTAR = int(KSTAR)

while checkIfInt(YELLOWSTAR)==False:
    YELLOWSTAR = raw_input( " # YELLOW STARS: ") #Asks the user how many yellow stars they want to generate.
YELLOWSTAR = int(YELLOWSTAR)

while checkIfInt(WHITESTAR)==False:
    WHITESTAR = raw_input( " # WHITE STARS: ") #Asks the user how many white stars they want to generate.
WHITESTAR = int(WHITESTAR)

while checkIfInt(BLUESTAR)==False:
    BLUESTAR = raw_input( " # BLUE STARS: ") #Asks the user how many blue stars they want to generate.
BLUESTAR = int(BLUESTAR)

while checkIfInt(BROWNSTAR)==False:
    BROWNSTAR = raw_input( " # BROWN STARS: ") #Asks the user how many brown stars they want to generate.
BROWNSTAR = int(BROWNSTAR)

while checkIfInt(DWARFSTAR)==False:
    DWARFSTAR = raw_input( " # DWARF STARS: ") #Asks the user how many white dwarves they want to generate.
DWARFSTAR = int(DWARFSTAR)

while checkIfInt(BLACKHOLE)==False:
    BLACKHOLE = raw_input( " # BLACK HOLES: ") #Asks the user how many black holes they want to generate.
BLACKHOLE = int(BLACKHOLE)

while checkIfInt(ROGUE)==False:
    ROGUE = raw_input( " # ROGUE PLANETS: ") #Asks the user how many rogue planets they want to generate.
ROGUE = int(ROGUE)




starNameList = generateStarNames(REDSTAR+KSTAR+YELLOWSTAR+WHITESTAR+BLUESTAR+BROWNSTAR+DWARFSTAR)
#print starNameList

f = open("Data_folder/TBG_Descriptions.txt")
theDescriptions = f.read().splitlines()
f.close()

########################
#######First make Kerbol
theDescription=kerbolDesc
theRadius = 261600000
theSphereOfInfluence = 220118820000
theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
#print theProperties

###fill in orbital data
theColor = "1,1,0,1" #Yellow
theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
#print theOrbitData

###fill in light data
thesunlightColor = "1,1,1,1.0"
thesunlightIntensity = 0.55
thescaledSunlightColor = "1,1,1,1.0"
thescaledSunlightIntensity = 0.55
theIVASuncolor = "1,1,1,1.0"
theIVASunIntensity = 0.55
thesunLensFlareColor = "1,1,1,1.0"
theambientLightColor = "0,0,0,1"
thesunAU = 13599840
theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
#print theLightData

###no material data for Kerbol
theMaterialData = ""

###no cornona data for Kerbol
theCoronasData = ""
tmp = starTemplate % {"theStarName":"Kerbol\n        cbNameLater = Sun", "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
tmp = tmp % {"planetBodies":""} #the kerbol planets are taken care of in the next section
theTotalFileText=theTotalFileText+tmp
tmp=""
##############################

##############################
###Make "interstellar space"
tmp = interstellarData
#print tmp
theTotalFileText=theTotalFileText+tmp
tmp=""
##############################



###DEATH TO CHOOSING STAR TYPES!
######pick a star mass in a normal distribution
#starMassKg = abs(random.normalvariate(6e30, 3e31))
starMassKg = abs(random.normalvariate(6e30, 3e30))
print starMassKg, "kg"

starMassKSP = TBG_utils.sol2Kerbol_kg(starMassKg)
print starMassKSP, "kg that will appear in game"

starMassSolar = TBG_utils.kg2solarMass(starMassKg)
print starMassSolar, "solar masses"

starRadiusSolar = TBG_utils.solarRadiusFromSolarMass(starMassSolar)
print starRadiusSolar, "solar radii"

starRadiusKm = TBG_utils.solarRadius2km(starRadiusSolar)
print starRadiusKm,"km"

starRadiusKSP = TBG_utils.sol2Kerbol_km(starRadiusKm)
print starRadiusKSP, "km that will appear in game"

starLum = TBG_utils.luminocityFromSolarMass(starMassSolar)
print starLum

starTempK = TBG_utils.solarTemp(starLum,starRadiusSolar)
print starTempK, "k"

starRGBColour = TBG_utils.temp2RGB(starTempK)
print starRGBColour

starCircumference = TBG_utils.starCircumference(starRadiusKm)
starSurfaceArea = TBG_utils.starSurfaceArea(starRadiusKm)
starVolume = TBG_utils.starVolume(starRadiusKm)
starDensity = TBG_utils.starDensity(starMassKSP,starRadiusKSP)
stdGravitationalParameter = TBG_utils.stdGravitationalParameter(starMassKSP)
surfaceGravity = TBG_utils.surfaceGravity(starMassKSP,starRadiusKSP)
escapeVelocity = TBG_utils.escapeVelocity(starMassKSP,starRadiusKSP)


##############################
###Make red stars
starsInt=0
numbRedStars=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(REDSTAR):
    ##RED STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    # theMassKg = random.randint(1.2000e+29, 1.2000e+32)
    # theMassKg = abs(random.normalvariate(6e30, 3e31))
    # print theMassKg, "kg"

    # theMassSolar = TBG_utils.kg2solarMass(theMassKg)
    # print theMassSolar, "solar masses"

    # solarRadius=TBG_utils.solarRadiusFromSolarMass(theMassSolar)
    # print solarRadius, "solar radii"

    # print TBG_utils.solarRadius2km(solarRadius),"km"

    # theLum = TBG_utils.luminocityFromSolarMass(theMassSolar)
    # print theLum

    # tempK = TBG_utils.solarTemp(theLum,solarRadius)
    # print tempK, "k"

    # starRGBColour = TBG_utils.temp2RGB(tempK)
    # print starRGBColour

    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 90118820000
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "1,0,0,1" #RED
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "1.0,0.188,0.00,1.0"
    thesunlightIntensity = 0.50
    thescaledSunlightColor = "1.0,0.188,0.00,1.0"
    thescaledSunlightIntensity = 0.30
    theIVASuncolor = "1.0,0.188,0.00,1.0"
    theIVASunIntensity = 1.0
    thesunLensFlareColor = "0.3,0,0,1.0"
    theambientLightColor = "0,0,0,1"
    thesunAU = 13599840

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "0.6,0.3,0.0,1.0"
    theemitColor1 = "0.9,0.1,0.0,1.0"
    thesunspotColor = "1.0,0,0,1.0"
    therimColor = "0.68,0.05,0.05,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("Red", "Red")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbRedStars=numbRedStars+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make red stars
##############################
print "\nnumber red stars made: "+str(numbRedStars)
print "   number of planets made: "+str(totNumbPlanets)
print "   number of moons made: "+str(totNumbMoons)
##############################
###Make orange stars
numbKStars=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(KSTAR):
    ##Orange STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 150118820000
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "1,0.5,0,1" #Orange
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "1.0,0.7,0.00,1.0"
    thesunlightIntensity = 0.50
    thescaledSunlightColor = "1.0,0.7,0.00,1.0"
    thescaledSunlightIntensity = 1.00
    theIVASuncolor = "1.0,0.7,0.00,1.0"
    theIVASunIntensity = 1.0
    thesunLensFlareColor = "1,0.5,0,1.0"
    theambientLightColor = "0,0,0,1"
    thesunAU = 113599840

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "1,1,0.0,1.0"
    theemitColor1 = "1,0.5,0.0,1.0"
    thesunspotColor = "1.0,0,0,1.0"
    therimColor = "0.9833707,0.6516854,0.05,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("K", "K")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbKStars=numbKStars+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make orange stars
##############################
print "\nnumber orange stars made: "+str(numbKStars)
print "number of planets made: "+str(totNumbPlanets)
print "number of moons made: "+str(totNumbMoons)
##############################
###Make yellow stars
numbYELLOWSTARs=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(YELLOWSTAR):
    ##yellow STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 220118820000
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "1,1,0,1" #Yellow
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "1,1,1,1.0"
    thesunlightIntensity = 0.55
    thescaledSunlightColor = "1,1,1,1.0"
    thescaledSunlightIntensity = 0.55
    theIVASuncolor = "1,1,1,1.0"
    theIVASunIntensity = 0.55
    thesunLensFlareColor = "1,1,1,1.0"
    theambientLightColor = "0,0,0,1"
    thesunAU = 113599840

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "1,1,0.0,1.0"
    theemitColor1 = "1,0.5,0.0,1.0"
    thesunspotColor = "1.0,0,0,1.0"
    therimColor = "0.9833707,0.6516854,0.05,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("Yellow", "Yellow")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbYELLOWSTARs=numbYELLOWSTARs+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make yellow stars
##############################
print "\nnumber yellow stars made: "+str(numbYELLOWSTARs)
print "number of planets made: "+str(totNumbPlanets)
print "number of moons made: "+str(totNumbMoons)
##############################
###Make white stars
numbWHITESTARs=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(WHITESTAR):
    ##white STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 330118820000
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "1,1,1,1" #white
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "1.0,1.0,1.0,1.0"
    thesunlightIntensity = 1.80
    thescaledSunlightColor = "1.0,1.0,1.0,1.0"
    thescaledSunlightIntensity = 0.80
    theIVASuncolor = "1.0,1.0,1.0,1.0"
    theIVASunIntensity = 2.00
    thesunLensFlareColor = "0.2303371,0.4494382,1,1.0"
    theambientLightColor = "0,0,0,1"
    thesunAU = 135998402566

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "0.2640449,0.258427,0.2752809,1.0"
    theemitColor1 = "0.6516854,0.6460674,0.6573034,1.0"
    thesunspotColor = "0,0,0,1.0"
    therimColor = "0.6011236,0.5955056,0.6292135,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("White", "White")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbWHITESTARs=numbWHITESTARs+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make white stars
##############################
print "\nnumber white stars made: "+str(numbWHITESTARs)
print "number of planets made: "+str(totNumbPlanets)
print "number of moons made: "+str(totNumbMoons)
##############################
###Make blue stars
numbBLUESTARs=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(BLUESTAR):
    ##blue STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 500118820000
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "0,0,1,1" #blue
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "0.0,0.15,0.6,1.0"
    thesunlightIntensity = 3.00
    thescaledSunlightColor = "0.0,0.15,0.6,1.0"
    thescaledSunlightIntensity = 3.00
    theIVASuncolor = "0.0,0.15,0.6,1.0"
    theIVASunIntensity = 3.00
    thesunLensFlareColor = "0,0.5,1,1.0"
    theambientLightColor = "0,0,0,1"
    thesunAU = 1359984025666

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "0.2,0.99,0.99,1.0"
    theemitColor1 = "0.139,0.061,1.0,1.0"
    thesunspotColor = "0,0,0,1.0"
    therimColor = "0.0,0.636,1.0,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("Blue", "Blue")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbBLUESTARs=numbBLUESTARs+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make blue stars
##############################
print "\nnumber blue stars made: "+str(numbBLUESTARs)
print "number of planets made: "+str(totNumbPlanets)
print "number of moons made: "+str(totNumbMoons)
##############################
###Make brown stars
numbBROWNSTARs=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(BROWNSTAR):
    ##brown STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 50118820000
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "0.7,0.53,0.28,1.0" #brown
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "0.7,0.53,0.28,1.0"
    thesunlightIntensity = 0.10
    thescaledSunlightColor = "0.7,0.53,0.28,1.0"
    thescaledSunlightIntensity = 0.20
    theIVASuncolor = "0.7,0.53,0.28,1.0"
    theIVASunIntensity = 0.10
    thesunLensFlareColor = "0.7,0.53,0.28,1.0" #I think this is the glow seen around the colour ball in map views. STH 2017.0106
    theambientLightColor = "0,0,0,1"
    thesunAU = 135998402

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "0.7,0.53,0.28,1.0"
    theemitColor1 = "0.7,0.53,0.28,1.0"
    thesunspotColor = "0.0,0,0,1.0"
    therimColor = "0.7,0.53,0.28,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("Black", "Black")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbBROWNSTARs=numbBROWNSTARs+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make brown stars
##############################
print "\nnumber brown stars made: "+str(numbBROWNSTARs)
print "number of planets made: "+str(totNumbPlanets)
print "number of moons made: "+str(totNumbMoons)
##############################
###Make dwarf stars
numbDWARFSTARs=0
totNumbPlanets=0
totNumbMoons=0
for aStar in range(DWARFSTAR):
    ##dwarf STARS
    ###Fill in property data
    theDescription=random.choice(theDescriptions) % (starNameList[0])
    theRadius = random.randint(15000000, 30000000) 
    theSphereOfInfluence = 90118820001
    theProperties=propertiesTemplate % (theDescription, theRadius, theSphereOfInfluence)
    #print theProperties

    ###fill in orbital data
    theColor = "1,1,1,1" #white
    theOrbitData = orbitalValues(GTYPE) % (theColor, "mode = 0")
    #print theOrbitData

    ###fill in light data
    thesunlightColor = "1.0,1.0,1.0,1.0"
    thesunlightIntensity = 0.50
    thescaledSunlightColor = "1.0,1.0,1.0,1.0"
    thescaledSunlightIntensity = 0.20
    theIVASuncolor = "1.0,1.0,1.0,1.0"
    theIVASunIntensity = 0.50
    thesunLensFlareColor = "0,0,0,1.0"
    theambientLightColor = "0,0,0,1"
    thesunAU = 113599840

    theLightData = lightTemplate % (thesunlightColor, thesunlightIntensity, thescaledSunlightColor, thescaledSunlightIntensity, theIVASuncolor, theIVASunIntensity, thesunLensFlareColor, theambientLightColor, thesunAU)
    #print theLightData

    ###fill in the material
    theemitColor0 = "1.0,1.0,1.0,1.0"
    theemitColor1 = "1.0,1.0,1.0,1.0"
    thesunspotColor = "1.0,1.0,1.0,1.0"
    therimColor = "0.7,0.7,0.7,1.0"
    theMaterialData= materialTemplate % (theemitColor0, theemitColor1, thesunspotColor, therimColor)

    #print theMaterialData

    ###fill in the corona data

    theCoronasData= coronasTemplate % ("Black", "Black")
    #print theCoronasData
    theStarName = starNameList[starsInt]
    starSystemData = starTemplate % {"theStarName":theStarName, "theProperties": theProperties, "theOrbitData": theOrbitData, "theLightData": theLightData, "theMaterialData": theMaterialData, "theCoronasData": theCoronasData }
    #print tmp
    #theTotalFileText=theTotalFileText+tmp
    #tmp=""
    if PENABLE == "y":
        thePlanetBodiesData=PENABLEISYES(theRadius,theSphereOfInfluence)
    else:
        thePlanetBodiesData=""
    tmp = starSystemData % {"planetBodies":thePlanetBodiesData}
    theTotalFileText=theTotalFileText+tmp
    tmp=""
    numbDWARFSTARs=numbDWARFSTARs+1
    ####clear up some memory
    theLightData=""
    theMaterialData=""
    theCoronasData=""
    starSystemData=""
    thePlanetBodiesData=""
    starsInt=starsInt+1
###End make dwarf stars
##############################
print "\nnumber dwarf stars made: "+str(numbDWARFSTARs)
print "number of planets made: "+str(totNumbPlanets)
print "number of moons made: "+str(totNumbMoons)




#print theTotalFileText

##############################
###Write data to file
with open("galaxy.cfg", 'a') as saveDataFile: #Open up the file to write to. 'a' means it will append to end
    saveDataFile.write(theTotalFileText)









    


