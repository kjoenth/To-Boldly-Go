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

def fileAsString(theFileName):
    ###########################
    #read in string template
    theFile=open("Data_Folder/templates/%s" % (theFileName),'r')
    theInfoTemp=theFile.read()
    theFile.close
    return theInfoTemp

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
    GTYPE = int(raw_input("Ellipse-0, Disk-1, Cluster-2:")) #Asks the user what kind of galaxy they want.
    #*******************************************************************************
    ADVANCED = raw_input("advanced settings? (y/n):")
    if ADVANCED == "y" :
        #*******************************************************************************
        if GTYPE == 2 :
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
    GTYPE = random.randint(0,2)
    if GTYPE == 2:
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
thePropertiesTemplate = fileAsString("propertiesTmp.txt")
theOrbitTemplate = fileAsString("orbitTmp.txt")
theLightTemplate = fileAsString("lightTmp.txt")
theMaterialTemplate = fileAsString("materialTmp.txt")
theCoronasTemplate = fileAsString("coronaTmp.txt")
theGasGiantTemplate = fileAsString("gasGiantScaledVersionTmp.txt")
theRingsTemplate = fileAsString("ringsTmp.txt")
theOceanTemplate = fileAsString("oceanTmp.txt")
thePlanetTemplate = fileAsString("planetTmp.txt")
theStarTmp = fileAsString("starTmp.txt")
theWikiTemplate = fileAsString("wikiTemplate.html")

###############################
#Template files for integration with other mods
theResearchBodyTemplate = fileAsString("forReserachBodiesTmp.txt")

#blackHole_MassKg = 8.55E37
#blackHole_MassKSP = sol2Kerbol_kg(blackHole_MassKg)
#blackHole_RadiusKSP = 100000

galaxy_RadiusKSP = (6.62251E+17)/6

sphereOfInfluence = galaxy_RadiusKSP - 2E+12

if GTYPE == 0:
    #spherical
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = random.randint(0, 360)
    theArgPeriapsis = random.randint(0, 360)
elif GTYPE == 1:
    #disc
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = random.randint(15, 50)
    theArgPeriapsis = random.randint(0, 360)
else:
    #spherical but smaller
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = random.randint(0, 360)
    theArgPeriapsis = random.randint(0, 360)

#kerbolDistanceToCore = theSemimajorAxis
#coreArgPeriapsis = theArgPeriapsis

theFileName = "galaxyFileTmp"
print "  Reading in %s template..." % (theFileName)
theFile=open("Data_Folder/templates/%s.txt" % (theFileName),'r')
theInfoTemp=theFile.read()
theFile.close

#print theInfoTemp % {"TBG_Version":TBG_Version, "SEED":SEED, "sphereOfInfluence":sphereOfInfluence, "semiMajorAxis":theSemimajorAxis, "theInclination":theInclination, "argumentOfPeriapsis":theArgPeriapsis}


# IF GTYPE = 2 THEN
#     CLUSTERNUM = 0
#     FOR a_Cluster = 1 TO CLUSTER
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
# END IF






# ###########
# ###Make the wiki file
# OPEN "wikiEntry.html" FOR OUTPUT AS #10 #Creates the wiki file

# ###########
# ###Make the researchBodies mod file
# OPEN "TBG-ResearchBodies.cfg" FOR OUTPUT AS #20 #Creates the researchBodies mod file
# #
# #******************************************************************************
# FOR a_Star = 1 TO OSTAR
#     star_MassKg = 3.18168E+31 + (RND(1) * (3.18168E+32 - 3.18168E+31)) ###pick a star mass in the O stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence blue giant star."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     maxPlanets = 0
#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #******************************************************************************
# FOR a_Star = 1 TO BSTAR
#     star_MassKg = 4.17596E+30 + (RND(1) * (3.18168E+31 - 4.17596E+30)) ###pick a star mass in the B stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence blue-white giant star."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)

#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #******************************************************************************
# FOR a_Star = 1 TO ASTAR
#     star_MassKg = 2.78397E+30 + (RND(1) * (4.17596E+30 - 2.78397E+30)) ###pick a star mass in the A stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence white dwarf star, though not a white-dwarf star. It's complicated."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
        
#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #*****************************************************************************
# FOR a_Star = 1 TO FSTAR
#     star_MassKg = 2.06809E+30 + (RND(1) * (2.78397E+30 - 2.06809E+30)) ###pick a star mass in the F stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence yellow-white dwarf star."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
        
#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #*****************************************************************************
# FOR a_Star = 1 TO GSTAR
#     star_MassKg = 1.59084E+30 + (RND(1) * (2.06809E+30 - 1.59084E+30)) ###pick a star mass in the G stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence yellow dwarf star."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
        
#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #*****************************************************************************
# FOR a_Star = 1 TO KSTAR
#     star_MassKg = 8.94848E+29 + (RND(1) * (1.59084E+30 - 8.94848E+29)) ###pick a star mass in the K stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence orange dwarf star."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #*****************************************************************************
# FOR a_Star = 1 TO MSTAR
#     star_MassKg = 1.491825E+29 + (RND(1) * (8.94848E+29 - 1.491825E+29)) ###pick a star mass in the M stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + " is a main sequence red dwarf star."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)

#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT#
# #*****************************************************************************
# FOR a_Star = 1 TO LSTAR
#     star_MassKg = 1.2337E+29 + (RND(1) * (1.491825E29 - 1.2337E+29)) ###pick a star mass in the L stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = star_Name$ + ": not quite a star, too big for a planet. A bug in the code of the universe."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'

#     IF PENABLE$ = "y" THEN
#         # parent name, number of planets (max), minimum distance from star, maximum distance from star
#         star_OrbitalInclination = INT(RND * 360)
#         CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)

#     END IF
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
# NEXT
# #
# #******************************************************************************
# FOR a_Star = 1 TO DWARFSTAR
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
#     IF (GTYPE = 0 OR GTYPE = 1) THEN
#         theReferenceBody$ = "Core"
#         IF GTYPE = 0 THEN theInclination$ = STR$(INT(RND * 360))
#         IF GTYPE = 1 THEN theInclination$ = STR$(INT(RND * 25) + 1)
#         #theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
#         theSemimajorAxis$ = str$(galaxy_RadiusKSP)
#     ELSE
#         theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
#         theInclination$ = STR$(INT(RND * 360))
#         theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
#     END IF
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

#     IF ASTTOG$ = "y" THEN
#         CALL MakeAsteroids(star_Name$, 2)
#     END IF
#     PRINT #1, "}"
#     SOBJECTNUMBER = SOBJECTNUMBER + 1
#     DWARFSTARNUMBER = DWARFSTARNUMBER + 1
# NEXT
# #
# #******************************************************************************

# FOR a_Star = 1 TO BLACKHOLE
#     #'star_MassKg = 4.17596e30 +(RND(1)*(3.18168e31-4.17596e30)) ###pick a star mass in the B stellar class range'
#     #'star_MassKg = 2.78397E30 +(RND(1)*(4.17596E30-2.78397E30)) ###pick a star mass in the A stellar class range'
#     #'star_MassKg = 2.06809E30 +(RND(1)*(2.78397E30-2.06809E30)) ###pick a star mass in the F stellar class range'
#     #'star_MassKg = 1.59084E30 +(RND(1)*(2.06809E30-1.59084E30)) ###pick a star mass in the G stellar class range'
#     #'star_MassKg = 8.94848E29 +(RND(1)*(1.59084E30-8.94848E29)) ###pick a star mass in the K stellar class range'
#     star_MassKg = 1.59084E29 + (RND(1) * (8.94848E29 - 1.59084E29)) ###pick a star mass in the M stellar class range'
#     #'star_MassKg = 2.46740E28 +(RND(1)*(1.59084E29-2.46740E28)) ###pick a star mass in the Y to L stellar class range'
#     #test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
#     #star_MassKg = 1.7565459e28*113.2393
#     #'star_MassKg = RND*(3.18168e31) ###pick a star mass in the Y to L stellar class range'

#     ###########################'
#     ###STH 2017-0209 Do calculations to get star characteristics
#     star_Name$ = starNameList$(SOBJECTNUMBER)
#     star_Description$ = "Dim light, Yet so bright. A lonely outpost in the deep dark night. Travelers come far shall know where they are. A new land, A new star, How much pain and suffering it must have took to go this far. For at " + star_Name$ + " your journey might be done. And you will be free."
#     CALL makeAStar(star_MassKg, star_Name$, star_Description$) #call the subroutinue to make a star'
#     ###These print statements can go away once the starTemplate can be used
#     ###Need to get planet and moon template generation working in basic first
#     ###STH 2017-0127
#     aStarName$ = theStarName$ #Calls the function "theStarName"
#     PRINT #1, "@Kopernicus"
#     PRINT #1, "{"
#     PRINT #1, "    Body"
#     PRINT #1, "    {"
#     PRINT #1, "        name = "; aStarName$
#     PRINT #1, "        Template"
#     PRINT #1, "        {"
#     PRINT #1, "            name = Sun"
#     PRINT #1, "        }"
#     ########################'
#     ###Fill in property data'
#     #'theDescription$ = "BILLYBOB -" + STR$(BLACKHOLENUMBER) + "is a black hole. An infinitely dense singularity encapsulated by the event horizon."
#     theDescription$ = aStarName$ + "is a black hole. An infinitely dense singularity encapsulated by the event horizon."
#     theRadius$ = STR$(INT(RND * 700000) + 300000)
#     theSphereOfInfluence$ = STR$(90118820000.5)
#     theGeeASL$ = STR$(1000000)
#     aPropertiesTemplate$ = thePropertiesTemplate$
#     aPropertiesNode$ = propertyNode$(aPropertiesTemplate$, theDescription$, theRadius$, "", "", theGeeASL$, "", "", "", "", "", theSphereOfInfluence$)
#     PRINT #1, aPropertiesNode$
#     ###End property data'
#     ########################'
#     ########################'
#     ###Fill in orbit data'
#     IF (GTYPE = 0 OR GTYPE = 1) THEN
#         theReferenceBody$ = "Core"
#         IF GTYPE = 0 THEN theInclination$ = STR$(INT(RND * 360))
#         IF GTYPE = 1 THEN theInclination$ = STR$(INT(RND * 25) + 1)
#         #theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
#         theSemimajorAxis = galaxy_RadiusKSP
#     ELSE
#         theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
#         theInclination$ = STR$(INT(RND * 360))
#         theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
#     END IF
#     theArgumentOfPeriapsis$ = STR$(INT(RND * 1000))
#     theMeanAnomalyAtEpoch$ = STR$(0)
#     theEpoch$ = STR$(0)
#     theMode$ = "" #'STR$(0)
#     theColour$ = "0.2,0.2,0.2,1"
#     aOrbitTemp$ = theOrbitTemplate$
#     aOrbitNode$ = orbitNode$(aOrbitTemp$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
#     PRINT #1, aOrbitNode$
#     ###End orbit data'
#     ########################'
#     ###Fill in Ring Data'
#     theAngle$ = "0"
#     theOuterRadius$ = "72000"
#     theInnerRadius$ = "200"
#     theRingTexture$ = "BH_ring"
#     theColour$ = "0.100, 1.000, 1.000, 1.000"
#     theLockRotation$ = "True"
#     theUnlit$ = "True"
#     aRingsTemp$ = theRingsTemplate$
#     aRingsNode$ = ringNode$(aRingsTemp$, theAngle$, theOuterRadius$, theInnerRadius$, theRingTexture$, theColour$, theLockRotation$, theUnlit$)
#     PRINT #1, aRingsNode$
#     ###End ring data'
#     ########################'
#     PRINT #1, "        ScaledVersion"
#     PRINT #1, "        {"
#     ########################'
#     ###Fill in light data'
#     sunlightColor$ = "1.0,1.0,1.0,1.0"
#     sunlightIntensity$ = "0.45"
#     scaledSunlightColor$ = "1.0,1.0,1.0,1.0"
#     scaledSunlightIntensity$ = "0.45"
#     IVASuncolor$ = "1.0, 0.977, 0.896, 1.0"
#     IVASunIntensity$ = "0.34"
#     sunLensFlareColor$ = "0.0, 0.0, 0.0, 1.0"
#     ambientLightColor$ = "0,0,0,1"
#     sunAU$ = "13599840256"
#     luminosity$ = "0"
#     givesOffLight$ = "False"
#     aLightTemp$ = theLightTemplate$
#     aLightNode$ = lightNode$(aLightTemp$, sunlightColor$, sunlightIntensity$, scaledSunlightColor$, scaledSunlightIntensity$, IVASuncolor$, IVASunIntensity$, sunLensFlareColor$, ambientLightColor$, sunAU$, luminosity$, givesOffLight$, "0.0045")
#     PRINT #1, aLightNode$
#     ###End light data'
#     ########################'
#     ########################'
#     ###Fill in material data'
#     emitColorZero$ = "0.0,0.0,0.0,1.0"
#     emitColorOne$ = "0.0,0.0,0.0,1.0"
#     sunspotColor$ = "0.0,0.0,0.0,1.0"
#     rimColor$ = "0.0,0.0,0.0,1.0"
#     rimPower$ = "1.5"
#     rimBlend$ = "1.8"
#     aMaterialTemp$ = theMaterialTemplate$
#     aMaterialNode$ = materialNode$(aMaterialTemp$, emitColorZero$, emitColorOne$, sunspotColor$, rimColor$, rimPower$, rimBlend$)
#     PRINT #1, aMaterialNode$
#     ###End material data'
#     ########################'
#     ########################'
#     ###Fill in coronas data'
#     starColour$ = "BlackHoleCorona"
#     aCoronaTemp$ = theCoronasTemplate$
#     aCoronaNode$ = coronaNode$(aCoronaTemp$, starColour$)
#     PRINT #1, aCoronaNode$
#     ###End coronas data'
#     ########################'
#     PRINT #1, "        }"
#     PRINT #1, "    }"

#     IF ASTTOG$ = "y" THEN
#         CALL MakeAsteroids(star_Name$, 2)
#     END IF

#     SOBJECTNUMBER = SOBJECTNUMBER + 1
#     BLACKHOLENUMBER = BLACKHOLENUMBER + 1
# NEXT
# #
# #******************************************************************************

# FOR a_Star = 1 TO ROGUE
#     aStarName$ = theStarName$ #Calls the function "theStarName"
#     PRINT #1, "@Kopernicus"
#     PRINT #1, "{"
#     PRINT #1, "    Body"
#     PRINT #1, "    {"
#     PRINT #1, "         name = "; aStarName$
#     ########################'
#     ###Fill in orbit data'
#     IF (GTYPE = 0 OR GTYPE = 1) THEN
#         theReferenceBody$ = "Sun"
#         IF GTYPE = 0 THEN theInclination$ = STR$(INT(RND * 360))
#         IF GTYPE = 1 THEN theInclination$ = STR$(INT(RND * 25) + 1)
#         #theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
#         theSemimajorAxis = galaxy_RadiusKSP
#     ELSE
#         theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
#         theInclination$ = STR$(INT(RND * 360))
#         theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
#     END IF
#     theArgumentOfPeriapsis$ = STR$(INT(RND * 1000))
#     theMeanAnomalyAtEpoch$ = STR$(0)
#     theEpoch$ = STR$(0)
#     theMode$ = "" #'STR$(0)
#     theColour$ = "1,1,0,1"
#     aOrbitTemp$ = theOrbitTemplate$
#     aOrbitNode$ = orbitNode$(aOrbitTemp$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
#     PRINT #1, aOrbitNode$
#     ###End property data'
#     ########################'

#     PRINT #1, "         Template"
#     PRINT #1, "         {"

        
#     PLANETTYPE = INT(RND * 13)
#     SELECT CASE PLANETTYPE
#         CASE 0
#             PLANETTYPE$ = "Moho"
#         CASE 1
#             PLANETTYPE$ = "Eve"
#         CASE 2
#             PLANETTYPE$ = "Mun"
#         CASE 3
#             PLANETTYPE$ = "Minmus"
#         CASE 4
#             PLANETTYPE$ = "Duna"
#         CASE 5
#             PLANETTYPE$ = "Ike"
#         CASE 6
#             PLANETTYPE$ = "Dres"
#         CASE 7
#             PLANETTYPE$ = "Jool"
#         CASE 8
#             PLANETTYPE$ = "Laythe"
#         CASE 9
#             PLANETTYPE$ = "Vall"
#         CASE 10
#             PLANETTYPE$ = "Tylo"
#         CASE 11
#             PLANETTYPE$ = "Jool"
#         CASE 12
#             PLANETTYPE$ = "Jool"
#         CASE 13
#             PLANETTYPE$ = "Eeloo"
#     END SELECT
#     IF PLANETTYPE$ = "Moho" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Eve" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 1500000) + 300000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Mun" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Minmus" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "                     radius ="; INT(RND * 120000) + 80000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Duna" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 700000) + 270000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Ike" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 250000) + 50000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Dres" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 250000) + 50000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Laythe" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 1000000) + 300000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Vall" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Tylo" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 1500000) + 300000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Bop" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 100000) + 70000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Pol" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 100000) + 70000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Eeloo" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 3)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     IF PLANETTYPE$ = "Jool" THEN
#         PRINT #1, "             name = "; PLANETTYPE$
#         PRINT #1, "         }"

#         PRINT #1, "         ScaledVersion"
#         PRINT #1, "         {"
#         PRINT #1, "             Material"
#         PRINT #1, "             {"
            
#         PRINT #1, "                 texture = To_Boldly_Go/gastextures/-"; INT(RND * 16); ".jpg"
#         PRINT #1, "             }"
#         PRINT #1, "         }"
#         PRINT #1, "         Properties"
#         PRINT #1, "         {"




            
#         PRINT #1, "            radius ="; INT(RND * 10000000) + 700000; ""
#         PRINT #1, "            sphereOfInfluence = 50118820000"

#         PRINT #1, "         }"
            
#         RINGS = INT(RND * 1)
#         IF RINGS = 0 THEN
#             PRINT #1, "         Rings"
#             PRINT #1, "         {"
#             PRINT #1, "             Ring"
#             PRINT #1, "             {"
#             PRINT #1, "                 angle = 0"
#             PRINT #1, "                 outerRadius = 3000"
#             PRINT #1, "                 innerRadius = 2000"
                
#             PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
#             PRINT #1, "                 color = 1.0,1,1,1.0"
#             PRINT #1, "                 lockRotation = false"
#             PRINT #1, "                 unlit = false"
#             PRINT #1, "             }"
#             PRINT #1, "          }"
#         END IF
#         PRINT #1, "    }"
#         PRINT #1, "}"
#     END IF
#     POBJECTNUMBER = POBJECTNUMBER + 1
# NEXT



# tempVar$ = forResearchBodies$(theResearchBodyTemplate$, "", discoveryText$, ignoreLevels$, localizationText$ )
# print #20, tempVar$#

#################
#Make output files
#################
#galaxy.cfg
#wikiEntry.html
#TBG-ResearchBodies.cfg
#GalaxyGen_Info-%galaxyName.txt
#This would probably be better as a list that is looped over
theWriteFile=open('galaxy.cfg', 'w')
theWriteFile.close()
theWriteFile=open('wikiEntry.html', 'w')
theWriteFile.close()
theWriteFile=open('TBG-ResearchBodies.cfg', 'w')
theWriteFile.close()
theWriteFile=open('GalaxyGen_Info-%sgalaxyName.txt', 'w')
theWriteFile.close()


# #******************************************************************************
print "  Reading in GalaxyGen_Info template..."
theFile=open('Data_Folder/templates/Info_template.txt','r')
theInfoTemp=theFile.read()
theFile.close


print theInfoTemp % {"GNAME":GNAME, "TBG_Version":TBG_Version, "CUSTOM":CUSTOM, "SEED":SEED, "GTYPE":GTYPE, 
    "AGE":AGE, "CLUSTERNUM":0, "PENABLE":PENABLE, "ASTTOG":ASTTOG, "LSTAR":LSTAR, "MSTAR":MSTAR, "KSTAR":KSTAR, 
    "GSTAR":GSTAR, "FSTAR":FSTAR, "ASTAR":ASTAR, "BSTAR":BSTAR, "OSTAR":OSTAR, "DWARFSTAR":DWARFSTAR}


# IF AGAIN$ = "n" THEN
#     GOTO 888
# END IF
# SYSTEM

# 777 PRINT

























# SUB makeStarNameList (numbRequestedStars)
#     ###########################
#     #read in star name prefixes
#     REDIM arrayPrefixes$(0)
#     theFileName$ = "Data_Folder/TBG_Prefixes.txt"
#     IF _FILEEXISTS(theFileName$) THEN
#         OPEN theFileName$ FOR INPUT AS #2
#         filecount% = 0
#         DO UNTIL EOF(2)
#             LINE INPUT #2, file$ 'read entire text file line
#             arrayPrefixes$(filecount%) = file$
#             filecount% = filecount% + 1
#             REDIM _PRESERVE arrayPrefixes$(filecount%)
#         LOOP
#         CLOSE #2
#     END IF
#     ###########################
#     #read in star name suffixes
#     REDIM arraySuffixes$(0)
#     theFileName$ = "Data_Folder/TBG_Suffixes.txt"
#     IF _FILEEXISTS(theFileName$) THEN
#         OPEN theFileName$ FOR INPUT AS #2
#         filecount% = 0
#         DO UNTIL EOF(2)
#             LINE INPUT #2, file$ 'read entire text file line
#             arraySuffixes$(filecount%) = file$
#             filecount% = filecount% + 1
#             REDIM _PRESERVE arraySuffixes$(filecount%)
#         LOOP
#         CLOSE #2
#     END IF
#     ########################################################
#     # pick a random index from the prefix and suffix arrays'
#     # the equiv in python would be:
#     # PREFIX = random.choice(thePrefixes)
#     # SUFFIX = random.choice(theSuffixes)
#     FOR i = 0 TO numbRequestedStars
#         lengArrayPrefixes% = UBOUND(arrayPrefixes$)
#         lengArraySuffixes% = UBOUND(arraySuffixes$)
#         indexPrefixes% = INT(RND * lengArrayPrefixes%)
#         indexSuffixes% = INT(RND * lengArraySuffixes%)
#         PREFIX$ = arrayPrefixes$(indexPrefixes%)
#         SUFFIX$ = arraySuffixes$(indexSuffixes%)
#         ##############################################
#         # combine the prefix and suffix to make a name
#         fullStarName$ = PREFIX$ + SUFFIX$
#         #hard coded avoidance of 'sun' and 'core'
#         IF fullStarName$ = "Sun" OR fullStarName$ = "Core" THEN
#             indexSuffixes% = INT(RND * lengArraySuffixes%)
#             SUFFIX$ = arraySuffixes$(indexSuffixes%)
#             fullStarName$ = fullStarName$ + "o'" + SUFFIX$
#         END IF
#         #I guess qbasic doesn't have a way of boolean testing to see if a value is in an array?
#         ####First look and see if the proposed name is in the template name array'
#         FOR j = 1 TO UBOUND(planetKey$)
#             DO UNTIL fullStarName$ <> planetKey$(j)
#                 indexSuffixes% = INT(RND * lengArraySuffixes%)
#                 SUFFIX$ = arraySuffixes$(indexSuffixes%)
#                 fullStarName$ = fullStarName$ + "o'" + SUFFIX$
#             LOOP
#         NEXT
#         #do the same sort of check and make sure the star name hasn't been used already
#         FOR j = 1 TO UBOUND(starNameList$)
#             DO UNTIL fullStarName$ <> starNameList$(j)
#                 indexSuffixes% = INT(RND * lengArraySuffixes%)
#                 SUFFIX$ = arraySuffixes$(indexSuffixes%)
#                 fullStarName$ = fullStarName$ + "a'" + SUFFIX$
#             LOOP
#         NEXT
#         starNameList$(i) = fullStarName$
#     NEXT
# END SUB

# FUNCTION fileAsString$ (fileName$)
#     ###########################
#     #read in string template
#     theFileName$ = "Data_Folder/templates/" + fileName$
#     wholeTxt$ = ""
#     IF _FILEEXISTS(theFileName$) THEN
#         OPEN theFileName$ FOR INPUT AS #3
#         DO UNTIL EOF(3)
#             LINE INPUT #3, fileLine$ 'read entire text file line
#             wholeTxt$ = wholeTxt$ + fileLine$ + CHR$(10)
#         LOOP
#         CLOSE #3
#     END IF
#     fileAsString$ = wholeTxt$
# END FUNCTION

# ################################################
# ########http://www.qb64.net/wiki/index.php/LEFT$
# FUNCTION ReplaceStr$ (text$, old$, new$)
#     DO
#         find = INSTR(start + 1, text$, old$) #'find location of a word in text
#         IF find THEN
#             count = count + 1
#             first$ = LEFT$(text$, find - 1) #'text before word including spaces
#             last$ = RIGHT$(text$, LEN(text$) - (find + LEN(old$) - 1)) #'text after word
#             text$ = first$ + new$ + last$
#         END IF
#         start = find
#     LOOP WHILE find
#     #'Replace = count 'function returns the number of replaced words. Comment out in SUB
#     #'Replace = text$
#     ReplaceStr$ = text$
# END FUNCTION

# FUNCTION propertyNode$ (aTemplate$, theDescription$, theRadius$, theMass$, theGravParam$, theGeeASL$, theDoesRotate$, theRotationPeriod$, theInitialRotation$, theIsTidallyLocked$, theIsHomeWord$, theSOI$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     ###########################'
#     ##Uncomment properties if data is present
#     IF theDescription$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%description =", "%description =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theDescription)s", theDescription$)
#     END IF
#     #STH 2018-0516. More dogshit code. 
#     #Why doesn't "IF (theRadius$ <> "" THEN IF val(theRadius$) <> 0) THEN" work?
#     IF theRadius$ <> "" THEN IF val(theRadius$) > 0 THEN
#             aTemplate$ = ReplaceStr(aTemplate$, "//%radius =", "%radius =")
#             aTemplate$ = ReplaceStr(aTemplate$, "%(theRadius)s", str$(val(theRadius$)+1))
#     END IF 
#     END IF
#     IF theMass$ <> "" THEN IF val(theMass$) > 0 THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%mass =", "%mass =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theMass)s", theMass$)
#     END IF
#     END IF
#     IF theGravParam$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%gravParameter =", "%gravParameter =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theGravParameter)s", theGravParam$)
#     END IF
#     IF theGeeASL$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%geeASL =", "%geeASL =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theGeeASL)s", theGeeASL$)
#     END IF
#     IF theDoesRotate$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%rotates =", "%rotates =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(doesRotate)s", theDoesRotate$)
#     END IF
#     IF theRotationPeriod$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%rotationPeriod =", "%rotationPeriod =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(rotationPeriod)s", theRotationPeriod$)
#     END IF
#     IF theInitialRotation$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%initialRotation =", "%initialRotation =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(initialRotation)s", theInitialRotation$)
#     END IF
#     IF theIsTidallyLocked$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%tidallyLocked =", "%tidallyLocked =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(isTidallyLocked)s", theIsTidallyLocked$)
#     END IF
#     IF theIsHomeWord$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%isHomeWorld =", "%isHomeWorld =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(isHomeWorld)s", theIsHomeWord$)
#     END IF
#     IF theSOI$ <> "" THEN IF val(theSOI$) > 0 THEN 
#         aTemplate$ = ReplaceStr(aTemplate$, "//%sphereOfInfluence =", "%sphereOfInfluence =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theSphereOfInfluence)s", theSOI$)
#     END IF
#     END if
#     ###########################'
#     propertyNode$ = aTemplate$
# END FUNCTION

# FUNCTION orbitNode$ (aTemplate$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     IF theReferenceBody$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%referenceBody =", "%referenceBody =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theReferenceBody)s", theReferenceBody$)
#     END IF
#     IF theColour$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%color =", "%color =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theColour)s", theColour$)
#     END IF
#     IF theMode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%mode =", "%mode =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theMode)s", theMode$)
#     END IF
#     IF theInclination$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%inclination =", "%inclination =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theInclination)s", theInclination$)
#     END IF
#     IF theEccentricity$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%eccentricity =", "%eccentricity =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theEccentricity)s", theEccentricity$)
#     END IF
#     IF theSemiMajorAxis$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%semiMajorAxis =", "%semiMajorAxis =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theSemiMajorAxis)s", theSemiMajorAxis$)
#     END IF
#     IF theLongitudeOfAscendingNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%longitudeOfAscendingNode =", "%longitudeOfAscendingNode =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theLongitudeOfAscendingNode)s ", theLongitudeOfAscendingNode$)
#     END IF
#     IF theArgumentOfPeriapsis$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%argumentOfPeriapsis =", "%argumentOfPeriapsis =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theArgumentOfPeriapsis)s", theArgumentOfPeriapsis$)
#     END IF
#     IF theMeanAnomalyAtEpoch$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%meanAnomalyAtEpoch =", "%meanAnomalyAtEpoch =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theMeanAnomalyAtEpoch)s", theMeanAnomalyAtEpoch$)
#     END IF
#     IF theEpoch$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%epoch =", "%epoch =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theEpoch)s", theEpoch$)
#     END IF
#     orbitNode$ = aTemplate$
# END FUNCTION

# FUNCTION lightNode$ (aTemplate$, sunlightColor$, sunlightIntensity$, scaledSunlightColor$, scaledSunlightIntensity$, IVASuncolor$, IVASunIntensity$, sunLensFlareColor$, ambientLightColor$, sunAU$, luminosity$, givesOffLight$, skyBrightness$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     IF sunlightColor$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//sunlightColor =", "sunlightColor =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theSunlightColor)s", sunlightColor$)
#     END IF
#     IF sunlightIntensity$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//sunlightIntensity =", "sunlightIntensity =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theSunlightIntensity)s", sunlightIntensity$)
#     END IF
#     IF scaledSunlightColor$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//scaledSunlightColor =", "scaledSunlightColor =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theScaledSunlightColor)s", scaledSunlightColor$)
#     END IF
#     IF scaledSunlightIntensity$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//scaledSunlightIntensity =", "scaledSunlightIntensity =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theScaledSunlightIntensity)s", scaledSunlightIntensity$)
#     END IF
#     IF IVASuncolor$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//IVASuncolor =", "IVASuncolor =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theIVASuncolor)s", IVASuncolor$)
#     END IF
#     IF IVASunIntensity$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//IVASunIntensity =", "IVASunIntensity =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theIVASunIntensity)s", IVASunIntensity$)
#     END IF
#     IF sunLensFlareColor$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//sunLensFlareColor =", "sunLensFlareColor =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theSunLensFlareColor)s", sunLensFlareColor$)
#     END IF
#     IF ambientLightColor$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//ambientLightColor =", "ambientLightColor =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theAmbientLightColor)s", ambientLightColor$)
#     END IF
#     IF sunAU$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//sunAU =", "sunAU =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theSunAU)s", sunAU$)
#     END IF
#     IF luminosity$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//luminosity =", "luminosity =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theLuminosity)s", luminosity$)
#     END IF
#     IF givesOffLight$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//givesOffLight =", "givesOffLight =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theGivesOffLight)s", givesOffLight$)
#     END IF
#     IF givesOffLight$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//key = 0", "key = 0")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(skyBrightness)s", skyBrightness$)
#     END IF
#     lightNode$ = aTemplate$
# END FUNCTION

# FUNCTION materialNode$ (aTemplate$, emitColorZero$, emitColorOne$, sunspotColor$, rimColor$, rimPower$, rimBlend$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theEmitColor0)s", emitColorZero$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theEmitColor1)s", emitColorOne$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSunspotColor)s", sunspotColor$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theRimColor)s", rimColor$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theRimPower)s", rimPower$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theRimBlend)s", rimBlend$)
#     materialNode$ = aTemplate$
# END FUNCTION

# FUNCTION coronaNode$ (aTemplate$, starColour$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theTexture)s", starColour$)
#     coronaNode$ = aTemplate$
# END FUNCTION

# FUNCTION ringNode$ (aTemplate$, theAngle$, theOuterRadius$, theInnerRadius$, theRingTexture$, theColour$, theLockRotation$, theUnlit$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     IF theAngle$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//angle =", "angle =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theAngle)s", theAngle$)
#     END IF
#     IF theOuterRadius$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//outerRadius =", "outerRadius =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theOuterRadius)s", theOuterRadius$)
#     END IF
#     IF theInnerRadius$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//innerRadius =", "innerRadius =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theInnerRadius)s", theInnerRadius$)
#     END IF
#     IF theRingTexture$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//texture =", "texture =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theRingTexture)s", theRingTexture$)
#     END IF
#     IF theColour$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//color =", "color =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theColour)s", theColour$)
#     END IF
#     IF theLockRotation$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//lockRotation =", "lockRotation =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theLockRotation)s", theLockRotation$)
#     END IF
#     IF theUnlit$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//unlit =", "unlit =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theUnlit)s", theUnlit$)
#     END IF
#     ringNode$ = aTemplate$
# END FUNCTION

# SUB readPlanetTemplates ()
#     ####2017.0201--STH
#     #This is a mess. I want something like python's dictionary
#     #Played with a multidimensional array, but can't redim it?
#     #Ended up using an array for each colum read in from the CSV
#     #Terrible technique, but I just want it to work at this point
#     ###################'
#     theFileName$ = "Data_Folder/TBG_Planet_Templates.csv"
#     theIndex = 0
#     IF _FILEEXISTS(theFileName$) THEN
#         OPEN theFileName$ FOR INPUT AS #1
#         'read through the file and get the number of lines'
#         DO UNTIL EOF(1)
#             REDIM _PRESERVE planetKey$(theIndex)
#             REDIM _PRESERVE thePlanetRadius(theIndex)
#             REDIM _PRESERVE thePlanetMass(theIndex)
#             REDIM _PRESERVE thePlanetSOI(theIndex)
#             REDIM _PRESERVE thePlanetDesc$(theIndex)
#             REDIM _PRESERVE thePlanetStock$(theIndex)
#             INPUT #1, aPlanetStock$, aPlanetName$, aPlanetRadius, aPlanetMass, aPlanetSOI, aDescription$
#             planetKey$(theIndex) = aPlanetName$
#             thePlanetRadius(theIndex) = aPlanetRadius
#             thePlanetMass(theIndex) = aPlanetMass
#             thePlanetSOI(theIndex) = aPlanetSOI
#             thePlanetDesc$(theIndex) = aDescription$
#             thePlanetStock$(theIndex) = aPlanetStock$
#             theIndex = theIndex + 1
#         LOOP
#         CLOSE #1
#     END IF
# END SUB

# FUNCTION AU2km (theAU)
#     AU2km = theAU * 149597871
# END FUNCTION

# FUNCTION realKM2kerbinKM (realKM)
#     #from discussion with Gregrox on Kopernicus discord
#     #one way to convert to/from kerbin space is:
#     #Earth SMA/Kerbin SMA = 10.9999726
#     realKM2kerbinKM = realKM / 10.9999726
# END FUNCTION

# FUNCTION kerbinKM2realKM (kerbinKM)
#     #from discussion with Gregrox on Kopernicus discord
#     #one way to convert to/from kerbin space is:
#     #Earth SMA/Kerbin SMA = 10.9999726
#     kerbinKM2realKM = kerbinKM * 10.9999726
# END FUNCTION

# FUNCTION realKM2Parsec (realKM)
#     #1 km = 3.2407792896664E-14 pc
#     realKM2Parsec = realKM*3.2407792896664E-14
# END FUNCTION

# FUNCTION solarMass2kg (SM)
#     #use Sol's solar mass and kg mass to convert
#     #Sol is ~1.989e30kg
#     solarMass2kg = 1.98855E30 * SM
# END FUNCTION

# FUNCTION kg2solarMass (the_kg)
#     #use Sol's solar mass and kg mass to convert
#     #Sol is ~1.989e30kg
#     kg2solarMass = the_kg / 1.98855E30
# END FUNCTION

# FUNCTION sol2Kerbol_kg (the_kg)
#     #The start Kerbol is 113.2393x less massiv than Sol
#     sol2Kerbol_kg = the_kg / 113.2393
# END FUNCTION

# FUNCTION kerbol2Sol_kg (the_kg)
#     #The start Kerbol is 113.2393x less massiv than Sol
#     kerbol2Sol_kg = the_kg * 113.2393
# END FUNCTION

# FUNCTION sol2Kerbol_km (the_km)
#     #The start Kerbol is 2.6594x smaller in radius than Sol
#     sol2Kerbol_km = the_km / 2.6594
# END FUNCTION

# FUNCTION kerbol2Sol_km (the_km)
#     #The start Kerbol is 2.6594x smaller in radius than Sol
#     kerbol2Sol_km = the_km * 2.6594
# END FUNCTION

# FUNCTION solarRadius2km (SR)
#     #use Sol's solar radius and km radius to convert
#     #Sol is ~695700km
#     solarRadius2km = 695700.0 * SR
# END FUNCTION

# FUNCTION km2solarRadius (SR)
#     #use Sol's solar radius and km radius to convert
#     #Sol is ~695700km
#     km2solarRadius = SR / 695700.0
# END FUNCTION

# FUNCTION solarRadiusFromSolarMass (SM)
#     #need a good reference for this
#     IF SM < 1 THEN
#         SR = SM ^ 0.5
#     ELSE
#         SR = SM ^ 0.8
#     END IF
#     solarRadiusFromSolarMass = SR
# END FUNCTION

# FUNCTION luminosityFromSolarMass (SM)
#     luminosityFromSolarMass = SM ^ 3.5
# END FUNCTION

# FUNCTION absMagFromLuminosity(theLuminosity)
#     ratioLum = theLuminosity/78.70
#     theLogTen# = log(ratioLum)/log(10.#)
#     absMagFromLuminosity = -2.5 * theLogTen#
# END FUNCTION

# FUNCTION apparentMagFromAbsMag(absMag, theDistance)
#     #the Distance has to be in parsecs
#     apparentMagFromAbsMag=5*LOG(theDistance/10)+absMag
# ENd FUNCTION

# FUNCTION solarTemp (SL, SR)
#     #returns star temp in K from solar luminocty and solar mass
#     solarTemp = ((SL / (SR ^ 2.0)) ^ 0.25) * 5778
# END FUNCTION

# FUNCTION starCircumference (radius_km)
#     starCircumference = 2.0 * _PI * radius_km
# END FUNCTION

# FUNCTION starSurfaceArea (radius_km)
#     starSurfaceArea = 4.0 * _PI * (radius_km ^ 2.0)
# END FUNCTION

# FUNCTION starVolume (radius_km)
#     #return in m^3
#     radius_m = radius_km * 1000.0
#     starVolume = (4.0 / 3.0) * _PI * (radius_m ^ 3.0)
# END FUNCTION

# FUNCTION starDensity (mass_kg, radius_km)
#     theVolume = starVolume(radius_km)
#     starDensity = mass_kg / theVolume
# END FUNCTION

# FUNCTION stdGravitationalParameter (mass_kg)
#     #https://en.wikipedia.org/wiki/Standard_gravitational_parameter
#     G = 6.674E-11
#     stdGravitationalParameter = (mass_kg * G)
# END FUNCTION

# FUNCTION surfaceGravity (mass_kg, radius_km)
#     #https://en.wikipedia.org/wiki/Surface_gravity
#     G = 6.674E-11
#     surfaceGravity = G * (mass_kg / (radius_km ^ 2.0))
# END FUNCTION

# FUNCTION escapeVelocity (mass_kg, radius_km)
#     G = 6.674E-11
#     temp = 2.0 * G * mass_kg
#     temp = temp / radius_km
#     escapeVelocity = temp ^ 0.5
# END FUNCTION

# FUNCTION hillSphere (mass_primary, mass_secondary, eccentricity_secondary, semimajorAxis_secondary)
#     #calculate the radius of the Hill sphere
#     #https://en.wikipedia.org/wiki/Hill_sphere
#     partOne = (semimajorAxis_secondary * (1.0 - eccentricity_secondary))
#     partTwo = (mass_secondary / (3.0 * mass_primary)) ^ (1.0 / 3.0)
#     theRadius = partOne * partTwo
#     #for unit test later:
#     #mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; semi-major axis earth = 149,598,023 km; eccentricity earth = 0.0167086
#     #gives a radius of 1471536.617 km
#     #mass blackhole @ center of milky way: 8.55E+37 kg
#     hillSphere = theRadius
# END FUNCTION

# FUNCTION simpleRocheLimit (mass_primary)
#     #If the orbiting body does not have a mass or radius provided
#     #the standard roche limit calc can't be used'
#     #use this dogshit instead.
#     #returns units in km
#     simpleRocheLimit = (7.52E-24)*mass_primary
# END FUNCTION

# FUNCTION rocheLimit (mass_primary, mass_secondary, radius_primary, radius_secondary)
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
# END FUNCTION

# FUNCTION kspSOI (mass_primary, mass_secondary, semimajorAxis_secondary)
#     #http://wiki.kerbalspaceprogram.com/wiki/Sphere_of_influence
#     kspSOI = (semimajorAxis_secondary * ((mass_secondary / mass_primary) ^ (2.0 / 5.0)))
# END FUNCTION

# FUNCTION solFrostLine (luminocity)
#     #https://en.wikipedia.org/wiki/Frost_line_(astrophysics)
#     solFrostLine = 4.85 * (luminocity ^ 0.5) #returns units in AU
# END FUNCTION

# FUNCTION siderealRotationalVel (theRadius, rotationalPeriod)
#     theVelocity = starCircumference(theRadius) / rotationalPeriod
#     siderealRotationalVel = theVelocity
# END FUNCTION

# FUNCTION synchronousOrbit (theRadius, theMass, rotationalPeriod)
#     #returns the altitude of geosync orbit above sea level
#     G = 6.674E-11
#     tmpOne = (G * theMass * (rotationalPeriod ^ 2.0))
#     tmpTwo = 4.0 * (_PI ^ 2.0)
#     tmpThr = (tmpOne / tmpTwo) ^ (1.0 / 3.0)
#     theAltitude = tmpThr - theRadius
#     synchronousOrbit = theAltitude
# END FUNCTION

# #I miss python
# FUNCTION pol2cartY(rho, theta)
#     #theta is in degrees
#     pol2cartY = rho * sin(theta*0.017453)
# END FUNCTION
# FUNCTION pol2cartX(rho, theta)
#     #theta is in degrees
#     pol2cartX = rho * cos(theta*0.017453)
# END FUNCTION

# FUNCTION theStarDistance (x1,x2,y1,y2)
#     theStarDistance = (((x2-x1)^2)+((y2-y1)^2))^0.5
# END FUNCTION

# #star colour RGB from temp
# SUB temp2RGB (tmpKelvin):
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
# END SUB




# FUNCTION starTempSubstitution$ (aTemplate$, aName$, aPropertiesNode$, aOrbitNode$, aRingNode$, aLightNode$, aMaterialNode$, aCoronaNode$, aSolarPowerCurve$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     ###########################'
#     IF aName$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%name =", "%name =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theName)s", aName$)
#     END IF
#     IF aPropertiesNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theProperties)s", aPropertiesNode$)
#     END IF
#     IF aOrbitNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theOrbitData)s", aOrbitNode$)
#     END IF
#     IF aRingNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theRingData)s", aRingNode$)
#     END IF
#     IF aLightNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theLightData)s", aLightNode$)
#     END IF
#     IF aMaterialNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theMaterialData)s", aMaterialNode$)
#     END IF
#     IF aCoronaNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theCoronasData)s", aCoronaNode$)
#     END IF
#     IF aSolarPowerCurve$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theSolarPowerCurve)s", aSolarPowerCurve$)
#     END IF

#     ###########################'
#     starTempSubstitution$ = aTemplate$
# END FUNCTION

# FUNCTION planetTempSubstitution$ (aTemplate$, aBodyNode$, aName$, aTemplateNode$, aPropertiesNode$, aOrbitNode$, aScaledVerionNode$, aRingNode$, aAtmosphereNode$, aPQSNode$, aOceanNode$)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     ###########################'
#     IF aBodyNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theBodyData)s", aBodyNode$)
#     END IF
#     IF aName$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%name =", "%name =")
#         aTemplate$ = ReplaceStr(aTemplate$, "%(theName)s", aName$)
#     END IF
#     IF aTemplateNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theTemplateData)s", aTemplateNode$)
#     END IF
#     IF aPropertiesNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theProperties)s", aPropertiesNode$)
#     END IF
#     IF aOrbitNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theOrbitData)s", aOrbitNode$)
#     END IF
#     IF aRingNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theRingData)s", aRingNode$)
#     END IF
#     IF aScaledVerionNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(ScaledVersion)s", aScaledVerionNode$)
#     END IF
#     IF aAtmosphereNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theAtmosphere)s", aAtmosphereNode$)
#     END IF
#     IF aPQSNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(thePQS)s", aPQSNode$)
#     END IF
#     IF aOceanNode$ <> "" THEN
#         aTemplate$ = ReplaceStr(aTemplate$, "//%(theOcean)s", aOceanNode$)
#     END IF

#     ###########################'
#     planetTempSubstitution$ = aTemplate$
# END FUNCTION

# FUNCTION wikiEntry$ (aTemplate$, star_HTMLColour$, star_Name$, star_RadiusKSP, star_Circumference, star_SurfaceArea, star_MassKSP, star_stdGravitationalParameter, star_Density, star_surfaceGravity, star_escapeVelocity, star_RotationalPeriod, star_siderealRotationalVel, star_theSynchronousOrbit, star_SOI, star_FrostLine, star_TempK, star_Lum, star_AbsMag, star_semimajorAxis, star_distToKerbol, star_ApparentMag)
#     #####STH 2017-0124. QBasic doesn't have string formatting like python.
#     #####Replicated that function with string replacement function.
#     ###########################'
#     aTemplate$ = ReplaceStr(aTemplate$, "%(htmlColour)s", star_HTMLColour$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(starName)s", star_Name$)
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theRadius)i", STR$(star_RadiusKSP))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theCircumfrence)g", STR$(star_Circumference))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSurfaceArea)g", STR$(star_SurfaceArea))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theMass)g", STR$(star_MassKSP))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theStdGrav)g", STR$(star_stdGravitationalParameter))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theDensity)g", STR$(star_Density))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSurfaceGravity)g", STR$(star_surfaceGravity))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theEscapeVelocity)g", STR$(star_escapeVelocity))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theRotationPeriod)g", STR$(star_RotationalPeriod))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSideralVelocity)g", STR$(star_siderealRotationalVel))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSynchronousOrbit)f", STR$(star_theSynchronousOrbit))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSOI)g", STR$(star_SOI))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theFrostLine)g", STR$(star_FrostLine))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theTemp)g", STR$(star_TempK))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theLuminosity)g", STR$(star_Lum))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theAbsMagnitude)g", STR$(star_AbsMag))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theApparentMagnitude)g", STR$(star_ApparentMag))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theSMA)i", STR$(star_semimajorAxis))
#     aTemplate$ = ReplaceStr(aTemplate$, "%(theDistToKerbol)i", STR$(star_distToKerbol))
#     ###########################'
#     wikiEntry$ = aTemplate$
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
# #
# #$INCLUDE: 'Source\MakeAsteroids.bm'#
# #$INCLUDE: 'Source\MakeMoons.bm'#
# #$INCLUDE: 'Source\MakePlanets.bm'#
# #$INCLUDE: 'Source\MakeStars.bm'
    
