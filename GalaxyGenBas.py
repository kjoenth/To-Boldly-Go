#To Boldly Go v0.3.1.2 - Kopernicus Procedural Galaxy Generator!"
#Copyright (C) 2018  Daniel L. & Sean T. Hammond"
#
#This program is free software; you can redistribute it and/or modify"
#it under the terms of the GNU General Public License as published by"
#the Free Software Foundation; either version 2 of the License, or"
#(at your option) any later version."
#
#This program is distributed in the hope that it will be useful,"
#but WITHOUT ANY WARRANTY; without even the implied warranty of"
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
#PGNU General Public License for more details."
#
#You should have received a copy of the GNU General Public License"
#along with this program; if not, write to the Free Software"
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA"

TBG_Version = "0.3.1.2"

import random
import csv
import sys

sys.path.append("Data_Folder")
import makeStarsUtils
import astroUtils

def fileAsString(theFileName):
    ###########################
    #read in string template
    theFile=open("Data_Folder/templates/%s" % (theFileName),'r')
    theFileStr=theFile.read()
    theFile.close
    return theFileStr

def readPlanetTemplates():
    #Redoing csv parse of template file listing
    #Might need reworking for downstream functions
    theFileName = "Data_Folder/TBG_Planet_Templates.csv"
    theData = csv.DictReader(open(theFileName,'r'))
    planetTemplateDict = []
    for aLine in theData:
        planetTemplateDict.append(aLine)
    return planetTemplateDict
    #             INPUT #1, aPlanetStock$, aPlanetName$, aPlanetRadius, aPlanetMass, aPlanetSOI, aDescription$
    #             planetKey$(theIndex) = aPlanetName$
    #             thePlanetRadius(theIndex) = aPlanetRadius
    #             thePlanetMass(theIndex) = aPlanetMass
    #             thePlanetSOI(theIndex) = aPlanetSOI
    #             thePlanetDesc$(theIndex) = aDescription$
    #             thePlanetStock$(theIndex) = aPlanetStock$

def makeStarNameList(numbRequestedStars):
    starNameList = []
    listPrefixes = []
    listSuffixes = []
    #Read in prefixes
    theFileName = "Data_Folder/TBG_Prefixes.txt"
    theData = open(theFileName, 'r')
    for aLine in theData:
        aLine=aLine.rstrip("\n")
        aLine=aLine.rstrip("\r")
        aLine=aLine.rstrip("\r\n")
        listPrefixes.append(aLine)
    theData.close()
    #read in suffixes
    theFileName = "Data_Folder/TBG_Suffixes.txt"
    theData = open(theFileName, 'r')
    for aLine in theData:
        aLine=aLine.rstrip("\n")
        aLine=aLine.rstrip("\r")
        aLine=aLine.rstrip("\r\n")
        listSuffixes.append(aLine)
    theData.close()
    ########################################################
    # pick a random index from the prefix and suffix arrays'
    for i in range(numbRequestedStars):
        PREFIX = random.choice(listPrefixes)
        SUFFIX = random.choice(listSuffixes)
        fullStarName = PREFIX + SUFFIX
        #hard coded avoidance of 'sun' and 'core'
        while fullStarName == "Sun" or fullStarName == "Core":
            SUFFIX = random.choice(listSuffixes)
            fullStarName = fullStarName + "o'" + SUFFIX
        #make sure the star name is not a planet template name
        ####First look and see if the proposed name is in the template name array'
        planetNameList = []
        for aRow in planetTemplateDict:
            planetNameList.append(aRow[' Template name'].strip())
        while fullStarName in planetNameList:
            SUFFIX = random.choice(listSuffixes)
            fullStarName = fullStarName + "o'" + SUFFIX
        #do the same sort of check and make sure the star name hasn't been used already
        while fullStarName in starNameList:
            SUFFIX = random.choice(listSuffixes)
            fullStarName = fullStarName + "a'" + SUFFIX
        starNameList.append(fullStarName)

    return starNameList






################'
#2017-0201 STH
#2018-0930 Reworked as python STH
#Call a subroutine that reads in planet template names, radii, SOI, and descriptions
#Will be used in the functions that make planets
planetTemplateDict = readPlanetTemplates()
###################

for i in range(2):
    print ""

print "TBG version "+TBG_Version
for i in range(5):
    print ""


print "Please do not use capitalization"
print "for anything other than the Galaxy name."
print ""
GNAME = raw_input("Name your Galaxy:")
CUSTOM = raw_input(" CUSTOM/AUTO(c/a):")

SEED = int(raw_input("Input Seed:")) #asks the user for a random seed.
random.seed(SEED)

SOBJECTNUMBER = 0
OSTAR = 0
BSTAR = 0
ASTAR = 0
FSTAR = 0
GSTAR = 0
KSTAR = 0
MSTAR = 0
LSTAR = 0
DWARFSTAR = 0
CLUSTER = 0

if CUSTOM == "c" :
    AGE = int(raw_input("Galaxy Age (0-5. 1 is recommended):"))
    PENABLE = raw_input("Planets? (y/n):") #Asks the user whether they want to have planets or not
    #*******************************************************************************
    ASTTOG = raw_input("Asteroids? (y/n):") #Asks the user whether they want to have asteroids or not
    #*******************************************************************************
    print "What Galaxy type do you want?:"
    makeStarsUtils.GTYPE = int(raw_input("Ellipse-0, Disk-1, Cluster-2:")) #Asks the user what kind of galaxy they want.
    #*******************************************************************************
    ADVANCED = raw_input("advanced settings? (y/n):")
    if ADVANCED == "y" :
        #*******************************************************************************
        if makeStarsUtils.GTYPE == 2 :
            CLUSTER = raw_input("Clusters:") #Asks the user how many star clusters they want

        print ""
        #*******************************************************************************
        LSTAR = int(raw_input("Brown Dwarves:")) #Asks the user how many brown stars they want to generate.

        #*******************************************************************************
        MSTAR = int(raw_input("Red Dwarves:")) #Asks the user how many red stars they want to generate.

        #*******************************************************************************
        KSTAR = int(raw_input("Orange Dwarves:")) #Asks the user how many orange stars they want to generate.

        #*******************************************************************************
        GSTAR =int(raw_input("Yellow Dwarves:")) #Asks the user how many yellow stars they want to generate.

        #*******************************************************************************
        FSTAR =int(raw_input("Yellow-White Dwarves:")) #Asks the user how many yellow stars they want to generate.

        #*******************************************************************************
        ASTAR = int(raw_input("White Stars:")) #Asks the user how many white stars they want to generate.

        #*******************************************************************************
        BSTAR = int(raw_input("Blue-White Giants:")) #Asks the user how many blue stars they want to generate.

        #*******************************************************************************
        OSTAR = int(raw_input("Blue Giants:")) #Asks the user how many blue stars they want to generate.

        #*******************************************************************************
        DWARFSTAR = int(raw_input("White Dwarves:")) #Asks the user how many white dwarves they want to generate.

        #*******************************************************************************
        #BLACKHOLE = raw_input(" BLACK HOLES:" #Asks the user how many black holes they want to generate.

        #*******************************************************************************
        #ROGUE = raw_input(" ROGUE PLANETS:" #Asks the user how many rogue planets they want to generate.

        #*******************************************************************************
else:
    AGE = random.randint(0,5)
    PENABLE = "y"
    ASTTOG = "y"
    makeStarsUtils.GTYPE = random.randint(0,2)
    if makeStarsUtils.GTYPE == 2:
        CLUSTER =random.randint(1,4)

if AGE == 0:
    LSTAR = random.randint(5,40)
    MSTAR = random.randint(10,20)
    KSTAR = random.randint(15,20)
    GSTAR = random.randint(5,20)
    ASTAR = random.randint(4,15)
    BSTAR = random.randint(1,10)
elif AGE == 1:
    LSTAR = random.randint(5,40)
    MSTAR = random.randint(10,20)
    KSTAR = random.randint(7,15)
    GSTAR = random.randint(5,10)
    ASTAR = random.randint(4,7)
    BSTAR = random.randint(1,4)
    DWARFSTAR = random.randint(1,5)
elif AGE == 2:
    LSTAR = random.randint(5,40)
    MSTAR = random.randint(10,20)
    KSTAR = random.randint(7,12)
    GSTAR = random.randint(1,3)
    DWARFSTAR = random.randint(5,10)
elif AGE == 3:
    LSTAR = random.randint(5,30)
    MSTAR = random.randint(10,20)
    KSTAR = random.randint(3,7)
    DWARFSTAR = random.randint(10,30)
elif AGE == 4:
    LSTAR = random.randint(5,20)
    MSTAR = random.randint(1,3)
    DWARFSTAR = random.randint(10,40)
else:
    LSTAR = random.randint(1,15)
    DWARFSTAR = random.randint(10,60)


numbRequestedStars = OSTAR + BSTAR + ASTAR + FSTAR + GSTAR + KSTAR + MSTAR + LSTAR + DWARFSTAR + CLUSTER

starNameList = makeStarNameList(numbRequestedStars)



#############################
###Read in the string templates
makeStarsUtils.thePropertiesTemplate = fileAsString("propertiesTmp.txt")
makeStarsUtils.theOrbitTemplate = fileAsString("orbitTmp.txt")
makeStarsUtils.theLightTemplate = fileAsString("lightTmp.txt")
makeStarsUtils.theMaterialTemplate = fileAsString("materialTmp.txt")
makeStarsUtils.theCoronasTemplate = fileAsString("coronaTmp.txt")
makeStarsUtils.theGasGiantTemplate = fileAsString("gasGiantScaledVersionTmp.txt")
makeStarsUtils.theRingsTemplate = fileAsString("ringsTmp.txt")
makeStarsUtils.theOceanTemplate = fileAsString("oceanTmp.txt")
makeStarsUtils.thePlanetTemplate = fileAsString("planetTmp.txt")
makeStarsUtils.theStarTemplate = fileAsString("starTmp.txt")
makeStarsUtils.theGalaxyTemplate = fileAsString("galaxyFileTmp.txt")
makeStarsUtils.theWikiTemplate = fileAsString("wikiTemplate.html")

theInfoTemp = fileAsString("Info_template.txt")



###############################
#Template files for integration with other mods
makeStarsUtils.theResearchBodyTemplate = fileAsString("forReserachBodiesTmp.txt")



galaxy_RadiusKSP=makeStarsUtils.galaxy_RadiusKSP
core_sphereOfInfluence=galaxy_RadiusKSP - 2E+12

if makeStarsUtils.GTYPE == 0:
    #spherical
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = random.randint(0, 360)
    theArgPeriapsis = random.randint(0, 360)
elif makeStarsUtils.GTYPE == 1:
    #disc
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = random.randint(15, 50)
    theArgPeriapsis = random.randint(0, 360)
else:
    #spherical but smaller
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = random.randint(0, 360)
    theArgPeriapsis = random.randint(0, 360)

makeStarsUtils.kerbolDistanceToCore = theSemimajorAxis
makeStarsUtils.coreArgPeriapsis = theArgPeriapsis

#THIS NEEDS TO BE ABSTRACTED AS A TEMPLATE
if makeStarsUtils.GTYPE == 2:
    makeStarsUtils.CLUSTERNUM = 0
#     for a_Cluster = 1 TO CLUSTER
#         theArgPeriapsis = INT(RND * 360)

#         PRINT #1, "@Kopernicus"
#         PRINT #1, "{"
#         PRINT #1, "    Body"
#         PRINT #1, "    {"
#         #'CLS
#         aName$ = starNameList$(CLUSTERNUM)
#         #'aName$ = theStarName$(numbRequestedStars) #Calls the function "theStarName"
#         PRINT #1, "        name = "; CLUSTERNUM; ""
#         PRINT #1, "        cbNameLater = "; aName$; " Galaxy"
#         PRINT #1, "        Template"
#         PRINT #1, "        {"
#         PRINT #1, "            name = Sun"
#         PRINT #1, "        }"
#         #'theDescription$ = aName$
#         #'theStarRadius = 10000
#         #'theStarSphereOfInfluence = 90118820000 'this is very small for a black hole I think. STH
#         #'aPropertiesTemplate$ = thePropertiesTemplate$
#         #'aPropertiesNode$ = propertyNode$(aPropertiesTemplate$, theDescription$, STR$(theStarRadius), "", "", "", "", "", "", "", "", STR$(theStarSphereOfInfluence))
#         PRINT #1, "        Properties"
#         PRINT #1, "        {"
#         PRINT #1, "            description = "; aName$; " Galaxy"
#         #'PRINT #1, "            sphereOfInfluence = 46992481203007510000" 220118820000
#         #it appears that giving a big SOI to CORE breaks the ability to orbit the stock Sun
#         # STH 2017-0320'
#         #'PRINT #1, "            sphereOfInfluence = 220118820000"
#         PRINT #1, "            sphereOfInfluence ="; (galaxy_RadiusKSP - 2E+12) / CLUSTER
#         PRINT #1, "        }"

#         PRINT #1, "        Orbit"
#         PRINT #1, "        {"
#         PRINT #1, "            referenceBody = Core"
#         PRINT #1, "            semiMajorAxis ="; RND(1) * (theSemimajorAxis)
        
#         PRINT #1, "            inclination ="; theInclination
        
#         PRINT #1, "            argumentOfPeriapsis ="; theArgPeriapsis; ""
#         PRINT #1, "            mode = 0"
#         PRINT #1, "            color = 0.2,0.2,0.2,1"
#         PRINT #1, "        }"
#         PRINT #1, "        ScaledVersion"
#         PRINT #1, "        {"
#         PRINT #1, "        Light"
#         PRINT #1, "         {"
#         PRINT #1, "             sunlightColor = 1,1,1,1.0"
#         PRINT #1, "             sunlightIntensity = 0.55"
#         PRINT #1, "             scaledSunlightColor = 1,1,1,1.0"
#         PRINT #1, "             scaledSunlightIntensity = 0.55"
#         PRINT #1, "             IVASunColor = 1,1,1,1.0"
#         PRINT #1, "             IVASunIntensity = 0.55"
#         PRINT #1, "             sunLensFlareColor = 1,1,1,1.0"
#         PRINT #1, "             luminosity = 0"
#         PRINT #1, "             ambientLightColor = 0,0,0,1.0"
#         PRINT #1, "             givesOffLight = False"
#         PRINT #1, "         }"
#         PRINT #1, "         Material"
#         PRINT #1, "         {"
#         PRINT #1, "             emitColor0 = 0,0,0,1"
#         PRINT #1, "             emitColor1 = 0,0,0,1"
#         PRINT #1, "             sunspotColor = 0,0,0,1"
#         PRINT #1, "             rimColor = 0,0,0,1"
#         PRINT #1, "         }"
#         PRINT #1, "         Coronas"
#         PRINT #1, "         {"
#         PRINT #1, "            Corona"
#         PRINT #1, "            {"
#         PRINT #1, "                rotation = 0"
#         PRINT #1, "                speed = -1"
#         PRINT #1, "                updateInterval = 5"
#         PRINT #1, "                scaleLimitX = 5"
#         PRINT #1, "                scaleLimitY = 5"
#         PRINT #1, "                scaleSpeed = 0.007"
#         PRINT #1, ""
#         PRINT #1, "                Material"
#         PRINT #1, "                {"
#         PRINT #1, "                    texture = To_Boldly_Go/coronae/BlackCorona"
#         PRINT #1, "                    inverseFade = 2.553731"
#         PRINT #1, "                }"
#         PRINT #1, "            }"
#         PRINT #1, "            Corona"
#         PRINT #1, "            {"
#         PRINT #1, "                rotation = 0"
#         PRINT #1, "                speed = 1"
#         PRINT #1, "                updateInterval = 5"
#         PRINT #1, "                scaleLimitX = 5"
#         PRINT #1, "                scaleLimitY = 5"
#         PRINT #1, "                scaleSpeed = 0.009"
#         PRINT #1, ""
#         PRINT #1, "                Material"
#         PRINT #1, "                {"
#         PRINT #1, "                      texture = To_Boldly_Go/coronae/BlackCorona"
#         PRINT #1, "                      inverseFade = 2.553731"
#         PRINT #1, "                }"
#         PRINT #1, "            }"
#         PRINT #1, "            }"
#         PRINT #1, "        }"
#         PRINT #1, "    }"
#         PRINT #1, "}"
#         CLUSTERNUM = CLUSTERNUM + 1
#     NEXT
# 
##################
#Fill in basic galaxy data in galaxyFileTmp.txt
makeStarsUtils.theGalaxyText = makeStarsUtils.theGalaxyTemplate % {'TBG_Version':TBG_Version,'SEED':SEED, 'sphereOfInfluence':core_sphereOfInfluence, 'semiMajorAxis':theSemimajorAxis, 
    'theInclination':theInclination, 'argumentOfPeriapsis':theArgPeriapsis}

##################

###########FOR TESTING
makeStarsUtils.GTYPE = 1





#******************************************************************************
for a_Star in range(OSTAR):
    star_MassKg = random.randint(3.18168E+31, 3.18168E+32) ###pick a star mass in the O stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence blue giant star." % (star_Name)

    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    #maxPlanets = 0
    # if PENABLE == "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#******************************************************************************
for a_Star in range(BSTAR):
    star_MassKg = random.randint(4.17596E+30,3.18168E+31) ###pick a star mass in the B stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence blue-white giant star." % (star_Name)
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)    
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#******************************************************************************
for a_Star in range(ASTAR):
    star_MassKg = random.randint(2.78397E+30,4.17596E+30) ###pick a star mass in the A stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence white dwarf star, though not a white-dwarf star. It's complicated." % (star_Name)
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#*****************************************************************************
for a_Star in range(FSTAR):
    star_MassKg = random.randint(2.06809E+30, 2.78397E+30) ###pick a star mass in the F stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence yellow-white dwarf star." % (star_Name)
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)  
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#*****************************************************************************
for a_Star in range(GSTAR):
    star_MassKg = random.randint(1.59084E+30, 2.06809E+30) ###pick a star mass in the G stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence yellow dwarf star." % (star_Name)
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#*****************************************************************************
for a_Star in range(KSTAR):
    star_MassKg = random.randint(8.94848E+29, 1.59084E+30) ###pick a star mass in the K stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence orange dwarf star." % (star_Name)
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#*****************************************************************************
for a_Star in range(MSTAR):
    star_MassKg = random.randint(1.491825E+29, 8.94848E+29) ###pick a star mass in the M stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s is a main sequence red dwarf star." % (star_Name)
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#*****************************************************************************
for a_Star in range(LSTAR):
    star_MassKg = random.randint(1.2337E+29, 1.491825E29) ###pick a star mass in the L stellar class range'
    #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    #star_MassKg = 1.7565459e28*113.2393

    ###########################'
    ###STH 2017-0209 Do calculations to get star characteristics
    star_Name = starNameList[SOBJECTNUMBER]
    #description could be fancier and include mass and other info
    star_Description = "%s: not quite a star, too big for a planet. A bug in the code of the universe."
    makeStarsUtils.makeAStar(star_MassKg, star_Name, star_Description) #call the subroutinue to make a star'

    # if PENABLE$ = "y":
    #     # parent name, number of planets (max), minimum distance from star, maximum distance from star
    #     star_OrbitalInclination = INT(RND * 360)
    #     CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    SOBJECTNUMBER = SOBJECTNUMBER + 1

#
# #******************************************************************************
# for a_Star = 1 TO DWARFSTAR
#     ###These print statements can go away once the starTemplate can be used
#     ###Need to get planet and moon template generation working in basic first
#     ###STH 2017-0127
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     PRINT #1, "@Kopernicus"
#     PRINT #1, "{"
#     PRINT #1, "    //https://github.com/Kopernicus/Kopernicus/wiki/Syntax-for-stars"
#     PRINT #1, "    Body"
#     PRINT #1, "    {"
#     PRINT #1, "        %name = "; star_Name$
#     PRINT #1, "        Template"
#     PRINT #1, "        {"
#     PRINT #1, "            name = Sun"
#     PRINT #1, "        }"
#     ########################'
#     ###Fill in property data'
#     star_Description$ = star_Name$ + " is a white dwarf stellar core remnant."
#     star_RadiusKSP = INT(RND * 700000) + 300000
#     star_SOI = 90118820000
#     aPropertiesTemplate$ = thePropertiesTemplate$
#     aPropertiesNode$ = propertyNode$(aPropertiesTemplate$, star_Description$, STR$(star_RadiusKSP), "", "", "", "", "", "", "", "", STR$(star_SOI))
#     PRINT #1, aPropertiesNode$
#     ###End property data'
#     ########################'
#     ########################'
#     ###Fill in orbit data'
#     if (makeStarsUtils.GTYPE = 0 OR makeStarsUtils.GTYPE = 1):
#         theReferenceBody$ = "Core"
#         if makeStarsUtils.GTYPE = 0: theInclination$ = STR$(INT(RND * 360))
#         if makeStarsUtils.GTYPE = 1: theInclination$ = STR$(INT(RND * 25) + 1)
#         #theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
#         theSemimajorAxis$ = str$(galaxy_RadiusKSP)
#     ELSE
#         theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
#         theInclination$ = STR$(INT(RND * 360))
#         theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
#     
#     theArgumentOfPeriapsis$ = STR$(INT(RND * 1000))
#     theMeanAnomalyAtEpoch$ = STR$(0)
#     theEpoch$ = STR$(0)
#     theMode$ = STR$(0)
#     theColour$ = "1,1,1,1"
#     aOrbitTemp$ = theOrbitTemplate$
#     aOrbitNode$ = orbitNode$(aOrbitTemp$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
#     PRINT #1, aOrbitNode$
#     ###End orbit data'
#     ########################'
#     PRINT #1, "        ScaledVersion"
#     PRINT #1, "        {"
#     ########################'
#     ###Fill in light data'
#     sunlightColor$ = "1.0,1.0,1.0,1.0"
#     sunlightIntensity$ = "0.5"
#     scaledSunlightColor$ = "1.0,1.0,1.0,1.0"
#     scaledSunlightIntensity$ = "0.20"
#     IVASuncolor$ = "1.0,1.0,1.0,1.0"
#     IVASunIntensity$ = "0.5"
#     #'sunLensFlareColor$ = "0.2303371,0.4494382,1,1.0"
#     sunLensFlareColor$ = "1.0,1.0,1.0,1.0,1.0"
#     ambientLightColor$ = "0,0,0,1"
#     sunAU$ = "135998402"
#     luminosity$ = "0"
#     givesOffLight$ = "True"
#     aLightTemp$ = theLightTemplate$
#     aLightNode$ = lightNode$(aLightTemp$, sunlightColor$, sunlightIntensity$, scaledSunlightColor$, scaledSunlightIntensity$, IVASuncolor$, IVASunIntensity$, sunLensFlareColor$, ambientLightColor$, sunAU$, luminosity$, givesOffLight$, " 0.0045")
#     PRINT #1, aLightNode$
#     ###End light data'
#     ########################'
#     ########################'
#     ###Fill in material data'
#     emitColorZero$ = "1.0,1.0,1.0,1.0"
#     emitColorOne$ = "1.0,1.0,1.0,1.0"
#     sunspotColor$ = "1.0,1.0,1.0,1.0"
#     rimColor$ = "0.7,0.7,0.7,1.0"
#     rimPower$ = "1"
#     rimBlend$ = "1"
#     aMaterialTemp$ = theMaterialTemplate$
#     aMaterialNode$ = materialNode$(aMaterialTemp$, emitColorZero$, emitColorOne$, sunspotColor$, rimColor$, rimPower$, rimBlend$)
#     PRINT #1, aMaterialNode$
#     ###End material data'
#     ########################'
#     ########################'
#     ###Fill in coronas data'
#     starColour$ = "White"
#     aCoronaTemp$ = theCoronasTemplate$
#     aCoronaNode$ = coronaNode$(aCoronaTemp$, starColour$)
#     PRINT #1, aCoronaNode$
#     ###End coronas data'
#     ########################'
#     PRINT #1, "        }"
#     PRINT #1, "    }"

#     if ASTTOG$ = "y":
#         CALL MakeAsteroids(star_Name$, 2)
#     
#     PRINT #1, "}"
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
#     DWARFSTARNUMBER = DWARFSTARNUMBER + 1
# NEXT
# #
# #******************************************************************************







# tempVar$ = forResearchBodies$(theResearchBodyTemplate$, "", discoveryText$, ignoreLevels$, localizationText$ )
# print #20, tempVar$#

#################
#Make output files
#################
#galaxy.cfg
#wikiEntry.html
#TBG-ResearchBodies.cfg
#GalaxyGen_Info-galaxyName.txt


theFile=open('galaxy.cfg', 'w')
theFile.write(makeStarsUtils.theGalaxyText)
theFile.close()
###########
###Make the wiki file
theFile=open('wikiEntry.html', 'w')
theFile.write(makeStarsUtils.theWikiText)
theFile.close()

theFile=open('TBG-ResearchBodies.cfg', 'w')
theFile.close()
###########
###Make the info file 
theFile=open('GalaxyGen_Info-%s.txt' % (GNAME), 'w')
tempVar = theInfoTemp % {"GNAME":GNAME, "TBG_Version":TBG_Version, "CUSTOM":CUSTOM, "SEED":SEED, "GTYPE":makeStarsUtils.GTYPE, 
    "AGE":AGE, "CLUSTERNUM":makeStarsUtils.CLUSTERNUM, "PENABLE":PENABLE, "ASTTOG":ASTTOG, "LSTAR":LSTAR, "MSTAR":MSTAR, "KSTAR":KSTAR, 
    "GSTAR":GSTAR, "FSTAR":FSTAR, "ASTAR":ASTAR, "BSTAR":BSTAR, "OSTAR":OSTAR, "DWARFSTAR":DWARFSTAR}
theFile.write(tempVar)
theFile.close()

print tempVar
# ################################################

# FUNCTION ringNode$ (aTemplate$, theAngle$, theOuterRadius$, theInnerRadius$, theRingTexture$, theColour$, theLockRotation$, theUnlit$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     if theAngle$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//angle =", "angle =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theAngle)s", theAngle$)
#     
#     if theOuterRadius$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//outerRadius =", "outerRadius =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theOuterRadius)s", theOuterRadius$)
#     
#     if theInnerRadius$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//innerRadius =", "innerRadius =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theInnerRadius)s", theInnerRadius$)
#     
#     if theRingTexture$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//texture =", "texture =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theRingTexture)s", theRingTexture$)
#     
#     if theColour$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//color =", "color =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theColour)s", theColour$)
#     
#     if theLockRotation$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//lockRotation =", "lockRotation =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theLockRotation)s", theLockRotation$)
#     
#     if theUnlit$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//unlit =", "unlit =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theUnlit)s", theUnlit$)
#     
#     ringNode$ = aTemplate$
# END FUNCTION

# FUNCTION planetTempSubstitution$ (aTemplate$, aBodyNode$, aName$, aTemplateNode$, aPropertiesNode$, aOrbitNode$, aScaledVerionNode$, aRingNode$, aAtmosphereNode$, aPQSNode$, aOceanNode$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     ###########################'
#     if aBodyNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theBodyData)s", aBodyNode$)
#     
#     if aName$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%name =", "%name =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theName)s", aName$)
#     
#     if aTemplateNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theTemplateData)s", aTemplateNode$)
#     
#     if aPropertiesNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theProperties)s", aPropertiesNode$)
#     
#     if aOrbitNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theOrbitData)s", aOrbitNode$)
#     
#     if aRingNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theRingData)s", aRingNode$)
#     
#     if aScaledVerionNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(ScaledVersion)s", aScaledVerionNode$)
#     
#     if aAtmosphereNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theAtmosphere)s", aAtmosphereNode$)
#     
#     if aPQSNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(thePQS)s", aPQSNode$)
#     
#     if aOceanNode$ <> "":
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theOcean)s", aOceanNode$)
#     

#     ###########################'
#     planetTempSubstitution$ = aTemplate$
# END FUNCTION



# FUNCTION forResearchBodies$ (aTemplate$, ignoreStrings$, onDiscoveryStrings$, onIgnoreLevelStrings$, localizationTextUS$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     ###########################'
#     aTemplate$ = ReplaceStr(aTemplate$, "%(ignoreStrings)s", ignoreStrings$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(onDiscoveryStrings)s", onDiscoveryStrings$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(onIgnoreLevelStrings)s", onIgnoreLevelStrings$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(localizationText)s", localizationTextUS$)
#     ###########################'
#     forResearchBodies$ = aTemplate$
# END FUNCTION

    
