'To Boldly Go v0.3.1.3.1b - Kopernicus Procedural Galaxy Generator!"
'Copyright (C) 2018  Daniel L. & Sean T. Hammond"
'
'This program is free software; you can redistribute it and/or modify"
'it under the terms of the GNU General Public License as published by"
'the Free Software Foundation; either version 2 of the License, or"
'(at your option) any later version."
'PRINT
'This program is distributed in the hope that it will be useful,"
'but WITHOUT ANY WARRANTY; without even the implied warranty of"
'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
'PGNU General Public License for more details."
'
'You should have received a copy of the GNU General Public License"
'along with this program; if not, write to the Free Software"
'Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA"

TBG_Version$ = "0.3.1.3.1b"
_TITLE "To Boldly Go version " + TBG_Version$

i& = _LOADIMAGE("Data_Folder/Galaxy-icon.png", 32) '<<<<<<< use your image file name here
IF i& < -1 THEN
    _ICON i&
    _FREEIMAGE i& ' release image handle after setting icon
END IF

888 PRINT
CLS

'################'
'#2017-0201 STH
'#Call a subroutine that reads in planet template names, radii, SOI, and descriptions
'#Will be used in the functions that make planets
REDIM SHARED planetKey$(-1)
REDIM SHARED thePlanetRadius(-1)
REDIM SHARED thePlanetMass(-1)
REDIM SHARED thePlanetSOI(-1)
REDIM SHARED thePlanetDesc$(-1)
REDIM SHARED thePlanetStock$(-1)
readPlanetTemplates
'###################

DIM SHARED SOBJECTNUMBER AS INTEGER
DIM SHARED POBJECTNUMBER AS INTEGER
DIM SHARED MOBJECTNUMBER AS INTEGER
DIM SHARED AOBJECTNUMBER AS INTEGER
DIM SHARED ASTTOG$

DIM SHARED discoveryText$ 
DIM SHARED ignoreBodies$ 
DIM SHARED ignoreLevels$ 
DIM SHARED localizationText$


'BROWNSTARNUMBER = 1
'REDSTARNUMBER = 1
'KSTARNUMBER = 1
'YELLOWSTARNUMBER = 1
'WHITESTARNUMBER = 1
'BLUESTARNUMBER = 1'
DWARFSTARNUMBER = 1
NEUTRONSTARNUMBER = 1
BLACKHOLENUMBER = 1
CLUSTERCORENUMBER = 1
CORESTARNUMBER = 1

DIM SHARED GTYPE AS INTEGER
CLS 'clears the screen
OPEN "galaxy.cfg" FOR OUTPUT AS #1 'Creates the config file

'*******************************************************************************
'*******************************************************************************
DIM Backdrop AS LONG
SCREEN _NEWIMAGE(700, 518, 32)
Backdrop = _LOADIMAGE("Data_folder/Background2.png")
_PUTIMAGE (0, 0), Backdrop

_FONT _LOADFONT("Data_folder/Commodore_Rounded_v1.2.ttf", 15, "MONOSPACE") 'select monospace font
_PRINTMODE _KEEPBACKGROUND
'*******************************************************************************
'*******************************************************************************

PRINT ""

778 PRINT
'_FONT _LOADFONT("Data_folder/DejaVuSans.ttf", 15, "MONOSPACE") 'select monospace font
'_PRINTMODE _KEEPBACKGROUND


IF PTOGGLE = 1 THEN
    PENABLE$ = "y"
END IF

IF ATOGGLE = 1 THEN
    ASTTOG$ = "y"
END IF

'COLOR _RGB(255, 255, 255), _RGB(0, 0, 0)
COLOR _RGB(88, 139, 175), _RGB(0, 0, 0)

FOR i = 1 TO 2
    PRINT ""
NEXT
PRINT "TBG version "+TBG_Version$
FOR i = 1 TO 5
    PRINT ""
NEXT
PRINT "Please do not use capitalization"
PRINT "for anything other than the Galaxy name."
PRINT ""
INPUT "Name your Galaxy:", GNAME$
2222 INPUT " (CUSTOM/AUTO)(c/a):", CUSTOM$

INPUT " Input Seed:", SEED 'asks the user for a random seed.
RANDOMIZE SEED

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

IF CUSTOM$ = "c" THEN
    INPUT "Galaxy Age (0-5. 1 is recommended):", AGE
    INPUT "Planets? (y/n):", PENABLE$ 'Asks the user whether they want to have planets or not
    '*******************************************************************************
    INPUT "Asteroids? (y/n):", ASTTOG$ 'Asks the user whether they want to have asteroids or not
    '*******************************************************************************
    PRINT "What Galaxy type do you want?:"
    999 INPUT "Ellipse-0, Disk-1, Cluster-2:", GTYPE 'Asks the user what kind of galaxy they want.
    IF GTYPE > 2 THEN
        GOTO 999
    END IF
    '*******************************************************************************
    INPUT "advanced settings? (y/n):", ADVANCED$

    IF ADVANCED$ = "y" THEN
        '*******************************************************************************
        IF GTYPE = 2 THEN
            INPUT "Clusters:", CLUSTER 'Asks the user how many star clusters they want
        END IF
        PRINT ""
        '*******************************************************************************
        INPUT "Brown Dwarves:", LSTAR 'Asks the user how many brown stars they want to generate.
        LSTAR = LSTAR + 0
        '*******************************************************************************
        INPUT "Red Dwarves:", MSTAR 'Asks the user how many red stars they want to generate.
        MSTAR = MSTAR + 0
        '*******************************************************************************
        INPUT "Orange Dwarves:", KSTAR 'Asks the user how many orange stars they want to generate.
        KSTAR = KSTAR + 0
        '*******************************************************************************
        INPUT "Yellow Dwarves:", GSTAR 'Asks the user how many yellow stars they want to generate.
        GSTAR = GSTAR + 0
        '*******************************************************************************
        INPUT "Yellow-White Dwarves:", FSTAR 'Asks the user how many yellow stars they want to generate.
        FSTAR = FSTAR + 0
        '*******************************************************************************
        INPUT "White Stars:", ASTAR 'Asks the user how many white stars they want to generate.
        ASTAR = ASTAR + 0
        '*******************************************************************************
        INPUT "Blue-White Giants:", BSTAR 'Asks the user how many blue stars they want to generate.
        BSTAR = BSTAR + 0
        '*******************************************************************************
        INPUT "Blue Giants:", OSTAR 'Asks the user how many blue stars they want to generate.
        OSTAR = OSTAR + 0
        '*******************************************************************************
        INPUT "White Dwarves:", DWARFSTAR 'Asks the user how many white dwarves they want to generate.
        DWARFSTAR = DWARFSTAR + 0
        '*******************************************************************************
        'INPUT " BLACK HOLES:", BLACKHOLE 'Asks the user how many black holes they want to generate.
        'BLACKHOLE = BLACKHOLE + 0
        '*******************************************************************************
        'INPUT " ROGUE PLANETS:", ROGUE 'Asks the user how many rogue planets they want to generate.
        'ROGUE = ROGUE + 0
        '*******************************************************************************
        CLS
        _PUTIMAGE (0, 0), Backdrop
        FOR i = 1 TO 11
            PRINT ""
        NEXT
    ELSE
        'AGE = INT(RND * 5)
        'GTYPE = INT(RND * 2)
        IF GTYPE = 2 THEN
            CLUSTER = INT(RND * 4) + 1
            ''    GTYPE = GTYPE + 1
            'ELSE
            ''    GTYPE = GTYPE + 1
        END IF
        SELECT CASE AGE
            CASE 0
                MSTAR = INT(RND * 20) + 10
                KSTAR = INT(RND * 15) + 20
                GSTAR = INT(RND * 20) + 5
                ASTAR = INT(RND * 15) + 4
                BSTAR = INT(RND * 10) + 1
                LSTAR = INT(RND * 40) + 5
            CASE 1
                MSTAR = INT(RND * 20) + 10
                KSTAR = INT(RND * 15) + 7
                GSTAR = INT(RND * 10) + 5
                ASTAR = INT(RND * 7) + 4
                BSTAR = INT(RND * 4) + 1
                LSTAR = INT(RND * 40) + 5
                DWARFSTAR = INT(RND * 5)
            CASE 2
                MSTAR = INT(RND * 20) + 10
                KSTAR = INT(RND * 12) + 7
                GSTAR = INT(RND * 3) + 1
                LSTAR = INT(RND * 40) + 5
                DWARFSTAR = INT(RND * 10) + 5
            CASE 3
                MSTAR = INT(RND * 10) + 10
                KSTAR = INT(RND * 7) + 3
                LSTAR = INT(RND * 30) + 5
                DWARFSTAR = INT(RND * 30) + 10
            CASE 4
                MSTAR = INT(RND * 3)
                LSTAR = INT(RND * 20) + 5
                DWARFSTAR = INT(RND * 40) + 10
            CASE 5
                LSTAR = INT(RND * 15)
                DWARFSTAR = INT(RND * 60) + 10
        END SELECT
    END IF
ELSE
    IF CUSTOM$ = "a" THEN
        AGE = INT(RND * 5)
        GTYPE = INT(RND * 2)
        IF GTYPE = 2 THEN
            CLUSTER = INT(RND * 4) + 1
            ''    GTYPE = GTYPE + 1
            'ELSE
            ''    GTYPE = GTYPE + 1
        END IF
        'IF GTYPE = 0 THEN
        'GTYPE = 1
        'END IF
        PENABLE$ = "y"
        ASTTOG$ = "y"

        SELECT CASE AGE
            CASE 0
                MSTAR = INT(RND * 20) + 10
                KSTAR = INT(RND * 15) + 20
                GSTAR = INT(RND * 20) + 5
                ASTAR = INT(RND * 15) + 4
                BSTAR = INT(RND * 10) + 1
                LSTAR = INT(RND * 40) + 5
            CASE 1
                MSTAR = INT(RND * 20) + 10
                KSTAR = INT(RND * 15) + 7
                GSTAR = INT(RND * 10) + 5
                ASTAR = INT(RND * 7) + 4
                BSTAR = INT(RND * 4) + 1
                LSTAR = INT(RND * 40) + 5
                DWARFSTAR = INT(RND * 5)
            CASE 2
                MSTAR = INT(RND * 20) + 10
                KSTAR = INT(RND * 12) + 7
                GSTAR = INT(RND * 3) + 1
                LSTAR = INT(RND * 40) + 5
                DWARFSTAR = INT(RND * 10) + 5
            CASE 3
                MSTAR = INT(RND * 10) + 10
                KSTAR = INT(RND * 7) + 3
                LSTAR = INT(RND * 30) + 5
                DWARFSTAR = INT(RND * 30) + 10
            CASE 4
                MSTAR = INT(RND * 3)
                LSTAR = INT(RND * 20) + 5
                DWARFSTAR = INT(RND * 40) + 10
            CASE 5
                LSTAR = INT(RND * 15)
                DWARFSTAR = INT(RND * 60) + 10
        END SELECT
        'BLACKHOLE = INT(RND * 3)
        'ROGUE = INT(RND * 10)
    ELSE
        GOTO 2222
    END IF
END IF

numbRequestedStars = OSTAR + BSTAR + ASTAR + FSTAR + GSTAR + KSTAR + MSTAR + LSTAR + DWARFSTAR + CLUSTER
DIM SHARED starNameList$(0 TO numbRequestedStars)
CALL makeStarNameList(numbRequestedStars)
'################################
'#Make the cfg header text
'###Insert 10 empty lines
FOR i = 1 TO 10
    PRINT #1, ""
NEXT
PRINT #1, "// WARNING! SPOILERS!"
PRINT #1, "// This file contains spoilers. If you don't want to have your surprises ruined, you should stop reading now."
'###Insert 34 empty lines'
FOR i = 1 TO 34
    PRINT #1, ""
NEXT
PRINT #1, "// Seriously, it's a lot more fun to find this stuff out in the game."
PRINT #1, "// Last chance to turn back."
'###Insert 28 empty lines'
FOR i = 1 TO 28
    PRINT #1, ""
NEXT
PRINT #1, "// I did warn you."
'###Insert 6 empty lines'
FOR i = 1 TO 6
    PRINT #1, ""
NEXT

PRINT #1, "//Generated by To Boldly Go, version " + TBG_Version$
PRINT #1, "//Seed: " + STR$(SEED)
'#End the cfg header text'
'#############################
'###Read in the string templates
DIM SHARED thePropertiesTemplate$, theOrbitTemplate$, theLightTemplate$, theMaterialTemplate$, theCoronasTemplate$
DIM SHARED theGasGiantTemplate$, theRingsTemplate$, theOceanTemplate$, thePlanetTemplate$, theStarTmp$, theWikiTemplate$, thePQSTemplate$
DIM SHARED theCity2Template$, theDebugTemplate$, theScaledVersionTemplate$
thePropertiesTemplate$ = fileAsString("propertiesTmp.txt")
theOrbitTemplate$ = fileAsString("orbitTmp.txt")
theLightTemplate$ = fileAsString("lightTmp.txt")
theMaterialTemplate$ = fileAsString("materialTmp.txt")
theCoronasTemplate$ = fileAsString("coronaTmp.txt")
theGasGiantTemplate$ = fileAsString("gasGiantScaledVersionTmp.txt")
theRingsTemplate$ = fileAsString("ringsTmp.txt")
theOceanTemplate$ = fileAsString("oceanTmp.txt")
theScaledVersionTemplate$ = fileAsString("scaledVersionTmp.txt")
thePQSTemplate$ = fileAsString("pqsTmp.txt")
theCity2Template$ = fileAsString("city2Tmp.txt")
theDebugTemplate$ = fileAsString("debugTmp.txt")
thePlanetTemplate$ = fileAsString("planetTmp.txt")
theStarTmp$ = fileAsString("starTmp.txt")
theWikiTemplate$ = fileAsString("wikiTemplate.html")

'###############################
'#Template files for integration with other mods
DIM SHARED theResearchBodyTemplate$
theResearchBodyTemplate$ = fileAsString("forReserachBodiesTmp.txt")

DIM SHARED blackHole_MassKSP
DIM SHARED blackHole_RadiusKSP
DIM SHARED galaxy_RadiusKSP

DIM SHARED REDgb AS INTEGER
DIM SHARED rGREENb AS INTEGER
DIM SHARED rgBLUE AS INTEGER

blackHole_MassKg = 8.55E37
blackHole_MassKSP = sol2Kerbol_kg(blackHole_MassKg)
blackHole_RadiusKSP = 100000

galaxy_RadiusKSP = (6.62251E+17)/6

'################################
PRINT #1, "@Kopernicus"
PRINT #1, "{"
PRINT #1, "    Body"
PRINT #1, "    {"
PRINT #1, "        name = Core"
PRINT #1, "        Template"
PRINT #1, "        {"
PRINT #1, "            name = Sun"
PRINT #1, "        }"
PRINT #1, "        Properties"
PRINT #1, "        {"
PRINT #1, "            description = The Kraken's Lair"
'PRINT #1, "            sphereOfInfluence = 46992481203007510000" 220118820000
'#it appears that giving a big SOI to CORE breaks the ability to orbit the stock Sun
'# STH 2017-0320'
'PRINT #1, "            sphereOfInfluence = 220118820000"
PRINT #1, "            sphereOfInfluence ="; galaxy_RadiusKSP - 2E+12; ""
PRINT #1, "        }"
PRINT #1, "        Orbit"
PRINT #1, "        {"
PRINT #1, "            referenceBody = Sun"

IF GTYPE = 0 THEN
    '#spherical
    '#theSemimajorAxis =  INT(RND * 1D+16) + 100000000000000
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = INT(RND * 360)
    theArgPeriapsis = INT(RND * 360)
END IF

IF GTYPE = 1 THEN
    '#disc
    '#theSemimajorAxis =  INT(RND * 1D+16) + 100000000000000
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = INT(RND * 50) - 25
    theArgPeriapsis = INT(RND * 360)
END IF

IF GTYPE = 2 THEN
    '#spherical but smaller
    '#theSemimajorAxis = INT(RND * 10000000000000) + 10000000000
    theSemimajorAxis = galaxy_RadiusKSP
    theInclination = INT(RND * 360)
    theArgPeriapsis = INT(RND * 360)
END IF

DIM SHARED KerbolDistanceToCore
KerbolDistanceToCore = theSemimajorAxis
DIM SHARED CoreArgPeriapsis
CoreArgPeriapsis = theArgPeriapsis

PRINT #1, "            semiMajorAxis ="; theSemimajorAxis; ""
PRINT #1, "            inclination ="; theInclination; ""
PRINT #1, "            argumentOfPeriapsis ="; theArgPeriapsis; ""
PRINT #1, "            mode = 0"
PRINT #1, "            color = 0.2,0.2,0.2,1"
PRINT #1, "        }"
PRINT #1, "        ScaledVersion"
PRINT #1, "        {"
PRINT #1, "            Light"
PRINT #1, "            {"
PRINT #1, "                sunlightColor = 0,0,0,0.0"
PRINT #1, "                sunlightIntensity = 0"
PRINT #1, "                scaledSunlightColor = 0,0,0,0.0"
PRINT #1, "                scaledSunlightIntensity = 0"
PRINT #1, "                IVASunColor = 0,0,0,0.0"
PRINT #1, "                IVASunIntensity = 0"
PRINT #1, "                sunLensFlareColor = 1,1,1,1.0"
PRINT #1, "                givesOffLight = False"
PRINT #1, "            }"
PRINT #1, "            Material"
PRINT #1, "            {"
PRINT #1, "                emitColor0 = 0,0,0,1"
PRINT #1, "                emitColor1 = 0,0,0,1"
PRINT #1, "                sunspotColor = 0,0,0,1"
PRINT #1, "                rimColor = 0,0,0,1"
PRINT #1, "            }"
PRINT #1, "            Coronas"
PRINT #1, "            {"
PRINT #1, "                Corona"
PRINT #1, "                {"
PRINT #1, "                    rotation = 0"
PRINT #1, "                    speed = -1"
PRINT #1, "                    updateInterval = 5"
PRINT #1, "                    scaleLimitX = 5"
PRINT #1, "                    scaleLimitY = 5"
PRINT #1, "                    scaleSpeed = 0.007"
PRINT #1, "                    Material"
PRINT #1, "                    {"
PRINT #1, "                        texture = To_Boldly_Go/coronae/BlackCorona"
PRINT #1, "                        inverseFade = 2.553731"
PRINT #1, "                    }"
PRINT #1, "                }"
PRINT #1, "            }"
PRINT #1, "        }"
PRINT #1, "    }"
PRINT #1, "}"

'#This transition from Kerbol to other star's SOIs is such a PITA. STH 2017-0902
'star_SOI = kspSOI(blackHole_MassKSP, 1.75656696858329E+28, theSemimajorAxis)
'star_SOI = 2.0e+11

PRINT #1, "@Kopernicus:AFTER[Kopernicus]"
PRINT #1, "{"
PRINT #1, "    %Body[Sun]"
PRINT #1, "    {"
PRINT #1, "        %Properties"
PRINT #1, "        {"
PRINT #1, "            %description = The Sun is the most well known object in the daytime sky. Scientists have noted a particular burning sensation and potential loss of vision if it is stared at for long periods of time. This is especially important to keep in mind considering the effect shiny objects have on the average Kerbal."
'PRINT #1, "            %sphereOfInfluence =  "; star_SOI;""
PRINT #1, "        }"
PRINT #1, "        %ScaledVersion"
PRINT #1, "        {"
'#This is a TERRIBLE way to do this. It should be using a template
'#STH 2018-0302
PRINT #1, "            %Light"
PRINT #1, "            {"
PRINT #1, "                %IntensityCurve"
PRINT #1, "                {"
PRINT #1, "                    key = 0 1 0 0"
PRINT #1, "                    key = 3000000000 1 0 -4.809E-11"
PRINT #1, "                    key = 6000000000 0.9 -2.404E-11 -2.404E-11"
PRINT #1, "                    key = 12000000000 0.8 -1.202E-11 -1.202E-11"
PRINT #1, "                    key = 24000000000 0.7 -6.011E-12 -6.011E-12"
PRINT #1, "                    key = 48000000000 0.6 -3.006E-12 -3.006E-12"
PRINT #1, "                    key = 96000000000 0.5 -1.503E-12 -1.503E-12"
PRINT #1, "                    key = 192000000000 0.4 -7.514E-13 -7.514E-13"
PRINT #1, "                    key = 384000000000 0.3 -3.757E-13 -3.757E-13"
PRINT #1, "                    key = 600000000000 0.235614 -2.404E-13 -1.212E-12"
PRINT #1, "                    key = 768000000000 0.032 -1.212E-12 -3.006E-14"
PRINT #1, "                    key = 1536000000000 0.016 -1.503E-14 -1.503E-14"
PRINT #1, "                    key = 3072000000000 0 -7.514E-15 0"
PRINT #1, "                }"
PRINT #1, "                %ScaledIntensityCurve"
PRINT #1, "                {"
PRINT #1, "                    key = 0 1 0 0"
PRINT #1, "                    key = 87500 1 0 -1.65E-06"
PRINT #1, "                    key = 175000 0.9 -8.24E-07 -8.24E-07"
PRINT #1, "                    key = 350000 0.8 -4.12E-07 -4.12E-07"
PRINT #1, "                    key = 700000 0.7 -2.06E-07 -2.06E-07"
PRINT #1, "                    key = 1400000 0.6 -1.03E-07 -1.03E-07"
PRINT #1, "                    key = 2800000 0.5 -5.15E-08 -5.15E-08"
PRINT #1, "                    key = 5600000 0.4 -2.58E-08 -2.58E-08"
PRINT #1, "                    key = 11200000 0.3 -1.29E-08 -1.29E-08"
PRINT #1, "                    key = 22400000 0.2 -6.44E-09 -6.44E-09"
PRINT #1, "                    key = 44800000 0.1 -3.22E-09 -3.22E-09"
PRINT #1, "                    key = 89600000 0 -1.61E-09 0"
PRINT #1, "                }"
PRINT #1, "                %IVAIntensityCurve"
PRINT #1, "                {"
PRINT #1, "                    key = 0 1 0 0"
PRINT #1, "                    key = 3000000000 1 0 -4.809E-11"
PRINT #1, "                    key = 6000000000 0.9 -2.404E-11 -2.404E-11"
PRINT #1, "                    key = 12000000000 0.8 -1.202E-11 -1.202E-11"
PRINT #1, "                    key = 24000000000 0.7 -6.011E-12 -6.011E-12"
PRINT #1, "                    key = 48000000000 0.6 -3.006E-12 -3.006E-12"
PRINT #1, "                    key = 96000000000 0.5 -1.503E-12 -1.503E-12"
PRINT #1, "                    key = 192000000000 0.4 -7.514E-13 -7.514E-13"
PRINT #1, "                    key = 384000000000 0.3 -3.757E-13 -3.757E-13"
PRINT #1, "                    key = 600000000000 0.235614 -2.404E-13 -1.212E-12"
PRINT #1, "                    key = 768000000000 0.032 -1.212E-12 -3.006E-14"
PRINT #1, "                    key = 1536000000000 0.016 -1.503E-14 -1.503E-14"
PRINT #1, "                    key = 3072000000000 0 -7.514E-15 0"
PRINT #1, "                }"
PRINT #1, "            }"
PRINT #1, "        }"
PRINT #1, "    }"
PRINT #1, "}"

IF GTYPE = 2 THEN
    CLUSTERNUM = 0
    FOR a_Cluster = 1 TO CLUSTER
        theArgPeriapsis = INT(RND * 360)

        PRINT #1, "@Kopernicus"
        PRINT #1, "{"
        PRINT #1, "    Body"
        PRINT #1, "    {"
        'CLS
        aName$ = starNameList$(CLUSTERNUM)
        'aName$ = theStarName$(numbRequestedStars) '#Calls the function "theStarName"
        PRINT #1, "        name = "; CLUSTERNUM; ""
        PRINT #1, "        cbNameLater = "; aName$; " Galaxy"
        PRINT #1, "        Template"
        PRINT #1, "        {"
        PRINT #1, "            name = Sun"
        PRINT #1, "        }"
        'theDescription$ = aName$
        'theStarRadius = 10000
        'theStarSphereOfInfluence = 90118820000 'this is very small for a black hole I think. STH
        'aPropertiesTemplate$ = thePropertiesTemplate$
        'aPropertiesNode$ = propertyNode$(aPropertiesTemplate$, theDescription$, STR$(theStarRadius), "", "", "", "", "", "", "", "", STR$(theStarSphereOfInfluence))
        PRINT #1, "        Properties"
        PRINT #1, "        {"
        PRINT #1, "            description = "; aName$; " Galaxy"
        'PRINT #1, "            sphereOfInfluence = 46992481203007510000" 220118820000
        '#it appears that giving a big SOI to CORE breaks the ability to orbit the stock Sun
        '# STH 2017-0320'
        'PRINT #1, "            sphereOfInfluence = 220118820000"
        PRINT #1, "            sphereOfInfluence ="; (galaxy_RadiusKSP - 2E+12) / CLUSTER
        PRINT #1, "        }"

        PRINT #1, "        Orbit"
        PRINT #1, "        {"
        PRINT #1, "            referenceBody = Core"
        PRINT #1, "            semiMajorAxis ="; RND(1) * (theSemimajorAxis)
        
        PRINT #1, "            inclination ="; theInclination
        
        PRINT #1, "            argumentOfPeriapsis ="; theArgPeriapsis; ""
        PRINT #1, "            mode = 0"
        PRINT #1, "            color = 0.2,0.2,0.2,1"
        PRINT #1, "        }"
        PRINT #1, "        ScaledVersion"
        PRINT #1, "        {"
        PRINT #1, "        Light"
        PRINT #1, "         {"
        PRINT #1, "             sunlightColor = 1,1,1,1.0"
        PRINT #1, "             sunlightIntensity = 0.55"
        PRINT #1, "             scaledSunlightColor = 1,1,1,1.0"
        PRINT #1, "             scaledSunlightIntensity = 0.55"
        PRINT #1, "             IVASunColor = 1,1,1,1.0"
        PRINT #1, "             IVASunIntensity = 0.55"
        PRINT #1, "             sunLensFlareColor = 1,1,1,1.0"
        PRINT #1, "             luminosity = 0"
        PRINT #1, "             ambientLightColor = 0,0,0,1.0"
        PRINT #1, "             givesOffLight = False"
        PRINT #1, "         }"
        PRINT #1, "         Material"
        PRINT #1, "         {"
        PRINT #1, "             emitColor0 = 0,0,0,1"
        PRINT #1, "             emitColor1 = 0,0,0,1"
        PRINT #1, "             sunspotColor = 0,0,0,1"
        PRINT #1, "             rimColor = 0,0,0,1"
        PRINT #1, "         }"
        PRINT #1, "         Coronas"
        PRINT #1, "         {"
        PRINT #1, "            Corona"
        PRINT #1, "            {"
        PRINT #1, "                rotation = 0"
        PRINT #1, "                speed = -1"
        PRINT #1, "                updateInterval = 5"
        PRINT #1, "                scaleLimitX = 5"
        PRINT #1, "                scaleLimitY = 5"
        PRINT #1, "                scaleSpeed = 0.007"
        PRINT #1, ""
        PRINT #1, "                Material"
        PRINT #1, "                {"
        PRINT #1, "                    texture = To_Boldly_Go/coronae/BlackCorona"
        PRINT #1, "                    inverseFade = 2.553731"
        PRINT #1, "                }"
        PRINT #1, "            }"
        PRINT #1, "            Corona"
        PRINT #1, "            {"
        PRINT #1, "                rotation = 0"
        PRINT #1, "                speed = 1"
        PRINT #1, "                updateInterval = 5"
        PRINT #1, "                scaleLimitX = 5"
        PRINT #1, "                scaleLimitY = 5"
        PRINT #1, "                scaleSpeed = 0.009"
        PRINT #1, ""
        PRINT #1, "                Material"
        PRINT #1, "                {"
        PRINT #1, "                      texture = To_Boldly_Go/coronae/BlackCorona"
        PRINT #1, "                      inverseFade = 2.553731"
        PRINT #1, "                }"
        PRINT #1, "            }"
        PRINT #1, "            }"
        PRINT #1, "        }"
        PRINT #1, "    }"
        PRINT #1, "}"
        CLUSTERNUM = CLUSTERNUM + 1
    NEXT
END IF






'###########
'###Make the wiki file
OPEN "wikiEntry.html" FOR OUTPUT AS #10 '#Creates the wiki file

'###########
'###Make the researchBodies mod file
OPEN "TBG-ResearchBodies.cfg" FOR OUTPUT AS #20 '#Creates the researchBodies mod file

'******************************************************************************
FOR a_Star = 1 TO OSTAR
    star_MassKg = 3.18168E+31 + (RND(1) * (3.18168E+32 - 3.18168E+31)) '###pick a star mass in the O stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence blue giant star."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    maxPlanets = 0
    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 6, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'******************************************************************************
FOR a_Star = 1 TO BSTAR
    star_MassKg = 4.17596E+30 + (RND(1) * (3.18168E+31 - 4.17596E+30)) '###pick a star mass in the B stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence blue-white giant star."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)

    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'******************************************************************************
FOR a_Star = 1 TO ASTAR
    star_MassKg = 2.78397E+30 + (RND(1) * (4.17596E+30 - 2.78397E+30)) '###pick a star mass in the A stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence white dwarf star, though not a white-dwarf star. It's complicated."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
        
    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'*****************************************************************************
FOR a_Star = 1 TO FSTAR
    star_MassKg = 2.06809E+30 + (RND(1) * (2.78397E+30 - 2.06809E+30)) '###pick a star mass in the F stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence yellow-white dwarf star."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
        
    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'*****************************************************************************
FOR a_Star = 1 TO GSTAR
    star_MassKg = 1.59084E+30 + (RND(1) * (2.06809E+30 - 1.59084E+30)) '###pick a star mass in the G stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence yellow dwarf star."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
        
    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'*****************************************************************************
FOR a_Star = 1 TO KSTAR
    star_MassKg = 8.94848E+29 + (RND(1) * (1.59084E+30 - 8.94848E+29)) '###pick a star mass in the K stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence orange dwarf star."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)
    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'*****************************************************************************
FOR a_Star = 1 TO MSTAR
    star_MassKg = 1.491825E+29 + (RND(1) * (8.94848E+29 - 1.491825E+29)) '###pick a star mass in the M stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + " is a main sequence red dwarf star."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)

    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT
'*****************************************************************************
FOR a_Star = 1 TO LSTAR
    star_MassKg = 1.2337E+29 + (RND(1) * (1.491825E29 - 1.2337E+29)) '###pick a star mass in the L stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = star_Name$ + ": not quite a star, too big for a planet. A bug in the code of the universe."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'

    IF PENABLE$ = "y" THEN
        '# parent name, number of planets (max), minimum distance from star, maximum distance from star
        star_OrbitalInclination = INT(RND * 360)
        CALL MakePlanets(star_Name$, star_MassKSP, star_RadiusKSP, star_OrbitalInclination, 5, 0.5 * star_HillSphereRadius, star_FrostLineKSP*1000)

    END IF
    SOBJECTNUMBER = SOBJECTNUMBER + 1
NEXT

'******************************************************************************
FOR a_Star = 1 TO DWARFSTAR
    '###These print statements can go away once the starTemplate can be used
    '###Need to get planet and moon template generation working in basic first
    '###STH 2017-0127
    star_Name$ = starNameList$(SOBJECTNUMBER)
    PRINT #1, "@Kopernicus"
    PRINT #1, "{"
    PRINT #1, "    //https://github.com/Kopernicus/Kopernicus/wiki/Syntax-for-stars"
    PRINT #1, "    Body"
    PRINT #1, "    {"
    PRINT #1, "        %name = "; star_Name$
    PRINT #1, "        Template"
    PRINT #1, "        {"
    PRINT #1, "            name = Sun"
    PRINT #1, "        }"
    '########################'
    '###Fill in property data'
    star_Description$ = star_Name$ + " is a white dwarf stellar core remnant."
    star_RadiusKSP = INT(RND * 700000) + 300000
    star_SOI = 90118820000
    aPropertiesTemplate$ = thePropertiesTemplate$
    aPropertiesNode$ = propertyNode$(aPropertiesTemplate$, star_Description$, STR$(star_RadiusKSP), "", "", "", "", "", "", "", "", "", "", STR$(star_SOI))
    PRINT #1, aPropertiesNode$
    '###End property data'
    '########################'
    '########################'
    '###Fill in orbit data'
    IF (GTYPE = 0 OR GTYPE = 1) THEN
        theReferenceBody$ = "Core"
        IF GTYPE = 0 THEN theInclination$ = STR$(INT(RND * 360))
        IF GTYPE = 1 THEN theInclination$ = STR$(INT(RND * 25) + 1)
        '#theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
        theSemimajorAxis$ = str$(galaxy_RadiusKSP)
    ELSE
        theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
        theInclination$ = STR$(INT(RND * 360))
        theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
    END IF
    theArgumentOfPeriapsis$ = STR$(INT(RND * 1000))
    theMeanAnomalyAtEpoch$ = STR$(0)
    theEpoch$ = STR$(0)
    theMode$ = STR$(0)
    theColour$ = "1,1,1,1"
    aOrbitTemp$ = theOrbitTemplate$
    aOrbitNode$ = orbitNode$(aOrbitTemp$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
    PRINT #1, aOrbitNode$
    '###End orbit data'
    '########################'
    PRINT #1, "        ScaledVersion"
    PRINT #1, "        {"
    '########################'
    '###Fill in light data'
    sunlightColor$ = "1.0,1.0,1.0,1.0"
    sunlightIntensity$ = "0.5"
    scaledSunlightColor$ = "1.0,1.0,1.0,1.0"
    scaledSunlightIntensity$ = "0.20"
    IVASuncolor$ = "1.0,1.0,1.0,1.0"
    IVASunIntensity$ = "0.5"
    'sunLensFlareColor$ = "0.2303371,0.4494382,1,1.0"
    sunLensFlareColor$ = "1.0,1.0,1.0,1.0,1.0"
    ambientLightColor$ = "0,0,0,1"
    sunAU$ = "135998402"
    luminosity$ = "0"
    givesOffLight$ = "True"
    aLightTemp$ = theLightTemplate$
    aLightNode$ = lightNode$(aLightTemp$, sunlightColor$, sunlightIntensity$, scaledSunlightColor$, scaledSunlightIntensity$, IVASuncolor$, IVASunIntensity$, sunLensFlareColor$, ambientLightColor$, sunAU$, luminosity$, givesOffLight$, " 0.0045")
    PRINT #1, aLightNode$
    '###End light data'
    '########################'
    '########################'
    '###Fill in material data'
    emitColorZero$ = "1.0,1.0,1.0,1.0"
    emitColorOne$ = "1.0,1.0,1.0,1.0"
    sunspotColor$ = "1.0,1.0,1.0,1.0"
    rimColor$ = "0.7,0.7,0.7,1.0"
    rimPower$ = "1"
    rimBlend$ = "1"
    aMaterialTemp$ = theMaterialTemplate$
    aMaterialNode$ = materialNode$(aMaterialTemp$, emitColorZero$, emitColorOne$, sunspotColor$, rimColor$, rimPower$, rimBlend$)
    PRINT #1, aMaterialNode$
    '###End material data'
    '########################'
    '########################'
    '###Fill in coronas data'
    starColour$ = "White"
    aCoronaTemp$ = theCoronasTemplate$
    aCoronaNode$ = coronaNode$(aCoronaTemp$, starColour$)
    PRINT #1, aCoronaNode$
    '###End coronas data'
    '########################'
    PRINT #1, "        }"
    PRINT #1, "    }"

    IF ASTTOG$ = "y" THEN
        CALL MakeAsteroids(star_Name$, 2)
    END IF
    PRINT #1, "}"
    SOBJECTNUMBER = SOBJECTNUMBER + 1
    DWARFSTARNUMBER = DWARFSTARNUMBER + 1
NEXT

'******************************************************************************

FOR a_Star = 1 TO BLACKHOLE
    'star_MassKg = 4.17596e30 +(RND(1)*(3.18168e31-4.17596e30)) '###pick a star mass in the B stellar class range'
    'star_MassKg = 2.78397E30 +(RND(1)*(4.17596E30-2.78397E30)) '###pick a star mass in the A stellar class range'
    'star_MassKg = 2.06809E30 +(RND(1)*(2.78397E30-2.06809E30)) '###pick a star mass in the F stellar class range'
    'star_MassKg = 1.59084E30 +(RND(1)*(2.06809E30-1.59084E30)) '###pick a star mass in the G stellar class range'
    'star_MassKg = 8.94848E29 +(RND(1)*(1.59084E30-8.94848E29)) '###pick a star mass in the K stellar class range'
    star_MassKg = 1.59084E29 + (RND(1) * (8.94848E29 - 1.59084E29)) '###pick a star mass in the M stellar class range'
    'star_MassKg = 2.46740E28 +(RND(1)*(1.59084E29-2.46740E28)) '###pick a star mass in the Y to L stellar class range'
    '#test value: feed in Kerbol's mass in real world kg: 1.7565459e28*113.2393
    '#star_MassKg = 1.7565459e28*113.2393
    'star_MassKg = RND*(3.18168e31) '###pick a star mass in the Y to L stellar class range'

    '###########################'
    '###STH 2017-0209 Do calculations to get star characteristics
    star_Name$ = starNameList$(SOBJECTNUMBER)
    star_Description$ = "Dim light, Yet so bright. A lonely outpost in the deep dark night. Travelers come far shall know where they are. A new land, A new star, How much pain and suffering it must have took to go this far. For at " + star_Name$ + " your journey might be done. And you will be free."
    CALL makeAStar(star_MassKg, star_Name$, star_Description$) '#call the subroutinue to make a star'
    '###These print statements can go away once the starTemplate can be used
    '###Need to get planet and moon template generation working in basic first
    '###STH 2017-0127
    aStarName$ = theStarName$ '#Calls the function "theStarName"
    PRINT #1, "@Kopernicus"
    PRINT #1, "{"
    PRINT #1, "    Body"
    PRINT #1, "    {"
    PRINT #1, "        name = "; aStarName$
    PRINT #1, "        Template"
    PRINT #1, "        {"
    PRINT #1, "            name = Sun"
    PRINT #1, "        }"
    '########################'
    '###Fill in property data'
    'theDescription$ = "BILLYBOB -" + STR$(BLACKHOLENUMBER) + "is a black hole. An infinitely dense singularity encapsulated by the event horizon."
    theDescription$ = aStarName$ + "is a black hole. An infinitely dense singularity encapsulated by the event horizon."
    theRadius$ = STR$(INT(RND * 700000) + 300000)
    theSphereOfInfluence$ = STR$(90118820000.5)
    theGeeASL$ = STR$(1000000)
    aPropertiesTemplate$ = thePropertiesTemplate$
    aPropertiesNode$ = propertyNode$(aPropertiesTemplate$, theDescription$, theRadius$, "", "", theGeeASL$, "", "", "", "", "", "", "", theSphereOfInfluence$)
    PRINT #1, aPropertiesNode$
    '###End property data'
    '########################'
    '########################'
    '###Fill in orbit data'
    IF (GTYPE = 0 OR GTYPE = 1) THEN
        theReferenceBody$ = "Core"
        IF GTYPE = 0 THEN theInclination$ = STR$(INT(RND * 360))
        IF GTYPE = 1 THEN theInclination$ = STR$(INT(RND * 25) + 1)
        '#theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
        theSemimajorAxis = galaxy_RadiusKSP
    ELSE
        theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
        theInclination$ = STR$(INT(RND * 360))
        theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
    END IF
    theArgumentOfPeriapsis$ = STR$(INT(RND * 1000))
    theMeanAnomalyAtEpoch$ = STR$(0)
    theEpoch$ = STR$(0)
    theMode$ = "" 'STR$(0)
    theColour$ = "0.2,0.2,0.2,1"
    aOrbitTemp$ = theOrbitTemplate$
    aOrbitNode$ = orbitNode$(aOrbitTemp$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
    PRINT #1, aOrbitNode$
    '###End orbit data'
    '########################'
    '###Fill in Ring Data'
    theAngle$ = "0"
    theOuterRadius$ = "72000"
    theInnerRadius$ = "200"
    theRingTexture$ = "BH_ring"
    theColour$ = "0.100, 1.000, 1.000, 1.000"
    theLockRotation$ = "True"
    theUnlit$ = "True"
    aRingsTemp$ = theRingsTemplate$
    aRingsNode$ = ringNode$(aRingsTemp$, theAngle$, theOuterRadius$, theInnerRadius$, theRingTexture$, theColour$, theLockRotation$, theUnlit$)
    PRINT #1, aRingsNode$
    '###End ring data'
    '########################'
    PRINT #1, "        ScaledVersion"
    PRINT #1, "        {"
    '########################'
    '###Fill in light data'
    sunlightColor$ = "1.0,1.0,1.0,1.0"
    sunlightIntensity$ = "0.45"
    scaledSunlightColor$ = "1.0,1.0,1.0,1.0"
    scaledSunlightIntensity$ = "0.45"
    IVASuncolor$ = "1.0, 0.977, 0.896, 1.0"
    IVASunIntensity$ = "0.34"
    sunLensFlareColor$ = "0.0, 0.0, 0.0, 1.0"
    ambientLightColor$ = "0,0,0,1"
    sunAU$ = "13599840256"
    luminosity$ = "0"
    givesOffLight$ = "False"
    aLightTemp$ = theLightTemplate$
    aLightNode$ = lightNode$(aLightTemp$, sunlightColor$, sunlightIntensity$, scaledSunlightColor$, scaledSunlightIntensity$, IVASuncolor$, IVASunIntensity$, sunLensFlareColor$, ambientLightColor$, sunAU$, luminosity$, givesOffLight$, "0.0045")
    PRINT #1, aLightNode$
    '###End light data'
    '########################'
    '########################'
    '###Fill in material data'
    emitColorZero$ = "0.0,0.0,0.0,1.0"
    emitColorOne$ = "0.0,0.0,0.0,1.0"
    sunspotColor$ = "0.0,0.0,0.0,1.0"
    rimColor$ = "0.0,0.0,0.0,1.0"
    rimPower$ = "1.5"
    rimBlend$ = "1.8"
    aMaterialTemp$ = theMaterialTemplate$
    aMaterialNode$ = materialNode$(aMaterialTemp$, emitColorZero$, emitColorOne$, sunspotColor$, rimColor$, rimPower$, rimBlend$)
    PRINT #1, aMaterialNode$
    '###End material data'
    '########################'
    '########################'
    '###Fill in coronas data'
    starColour$ = "BlackHoleCorona"
    aCoronaTemp$ = theCoronasTemplate$
    aCoronaNode$ = coronaNode$(aCoronaTemp$, starColour$)
    PRINT #1, aCoronaNode$
    '###End coronas data'
    '########################'
    PRINT #1, "        }"
    PRINT #1, "    }"

    IF ASTTOG$ = "y" THEN
        CALL MakeAsteroids(star_Name$, 2)
    END IF

    SOBJECTNUMBER = SOBJECTNUMBER + 1
    BLACKHOLENUMBER = BLACKHOLENUMBER + 1
NEXT

'******************************************************************************

FOR a_Star = 1 TO ROGUE
    aStarName$ = theStarName$ '#Calls the function "theStarName"
    PRINT #1, "@Kopernicus"
    PRINT #1, "{"
    PRINT #1, "    Body"
    PRINT #1, "    {"
    PRINT #1, "         name = "; aStarName$
    '########################'
    '###Fill in orbit data'
    IF (GTYPE = 0 OR GTYPE = 1) THEN
        theReferenceBody$ = "Sun"
        IF GTYPE = 0 THEN theInclination$ = STR$(INT(RND * 360))
        IF GTYPE = 1 THEN theInclination$ = STR$(INT(RND * 25) + 1)
        '#theSemiMajorAxis$ = STR$(INT(RND * 1D+16) + 100000000000000#)
        theSemimajorAxis = galaxy_RadiusKSP
    ELSE
        theReferenceBody$ = STR$(INT(RND * CLUSTERNUM))
        theInclination$ = STR$(INT(RND * 360))
        theSemiMajorAxis$ = STR$(INT(RND * 10000000000000) + 10000000000)
    END IF
    theArgumentOfPeriapsis$ = STR$(INT(RND * 1000))
    theMeanAnomalyAtEpoch$ = STR$(0)
    theEpoch$ = STR$(0)
    theMode$ = "" 'STR$(0)
    theColour$ = "1,1,0,1"
    aOrbitTemp$ = theOrbitTemplate$
    aOrbitNode$ = orbitNode$(aOrbitTemp$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
    PRINT #1, aOrbitNode$
    '###End property data'
    '########################'

    PRINT #1, "         Template"
    PRINT #1, "         {"

        
    PLANETTYPE = INT(RND * 13)
    SELECT CASE PLANETTYPE
        CASE 0
            PLANETTYPE$ = "Moho"
        CASE 1
            PLANETTYPE$ = "Eve"
        CASE 2
            PLANETTYPE$ = "Mun"
        CASE 3
            PLANETTYPE$ = "Minmus"
        CASE 4
            PLANETTYPE$ = "Duna"
        CASE 5
            PLANETTYPE$ = "Ike"
        CASE 6
            PLANETTYPE$ = "Dres"
        CASE 7
            PLANETTYPE$ = "Jool"
        CASE 8
            PLANETTYPE$ = "Laythe"
        CASE 9
            PLANETTYPE$ = "Vall"
        CASE 10
            PLANETTYPE$ = "Tylo"
        CASE 11
            PLANETTYPE$ = "Jool"
        CASE 12
            PLANETTYPE$ = "Jool"
        CASE 13
            PLANETTYPE$ = "Eeloo"
    END SELECT
    IF PLANETTYPE$ = "Moho" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Eve" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 1500000) + 300000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Mun" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Minmus" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "                     radius ="; INT(RND * 120000) + 80000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Duna" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 700000) + 270000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Ike" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 250000) + 50000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Dres" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 250000) + 50000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Laythe" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 1000000) + 300000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Vall" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Tylo" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 1500000) + 300000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Bop" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 100000) + 70000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Pol" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 100000) + 70000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Eeloo" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 300000) + 70000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 3)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    IF PLANETTYPE$ = "Jool" THEN
        PRINT #1, "             name = "; PLANETTYPE$
        PRINT #1, "         }"

        PRINT #1, "         ScaledVersion"
        PRINT #1, "         {"
        PRINT #1, "             Material"
        PRINT #1, "             {"
            
        PRINT #1, "                 texture = To_Boldly_Go/gastextures/-"; INT(RND * 16); ".jpg"
        PRINT #1, "             }"
        PRINT #1, "         }"
        PRINT #1, "         Properties"
        PRINT #1, "         {"




            
        PRINT #1, "            radius ="; INT(RND * 10000000) + 700000; ""
        PRINT #1, "            sphereOfInfluence = 50118820000"

        PRINT #1, "         }"
            
        RINGS = INT(RND * 1)
        IF RINGS = 0 THEN
            PRINT #1, "         Rings"
            PRINT #1, "         {"
            PRINT #1, "             Ring"
            PRINT #1, "             {"
            PRINT #1, "                 angle = 0"
            PRINT #1, "                 outerRadius = 3000"
            PRINT #1, "                 innerRadius = 2000"
                
            PRINT #1, "                 texture = To_Boldly_Go/ringtextures/-"; INT(RND * 3); "-.png"
            PRINT #1, "                 color = 1.0,1,1,1.0"
            PRINT #1, "                 lockRotation = false"
            PRINT #1, "                 unlit = false"
            PRINT #1, "             }"
            PRINT #1, "          }"
        END IF
        PRINT #1, "    }"
        PRINT #1, "}"
    END IF
    POBJECTNUMBER = POBJECTNUMBER + 1
NEXT



tempVar$ = forResearchBodies$(theResearchBodyTemplate$, "", discoveryText$, ignoreLevels$, localizationText$ )
print #20, tempVar$
'******************************************************************************

PRINT ""
PRINT ""; SOBJECTNUMBER; "Stars"
PRINT ""; POBJECTNUMBER; "Planets"
PRINT ""; MOBJECTNUMBER; "Moons"
PRINT ""; AOBJECTNUMBER; "Asteroids"
TOTAL = SOBJECTNUMBER + POBJECTNUMBER + MOBJECTNUMBER + AOBJECTNUMBER
PRINT ""; SOBJECTNUMBER + POBJECTNUMBER + MOBJECTNUMBER + AOBJECTNUMBER; " Total"
PRINT ""
INPUT "Are you satisfied with these results? (y/n):", AGAIN$

CLOSE #1
CLOSE #10
FILENAME$ = "Galaxygen_Info-" + GNAME$ + ".txt"
OPEN FILENAME$ FOR OUTPUT AS #1
PRINT #1, "  _______      ____        _     _ _          _____"
PRINT #1, " |__   __|    |  _ \      | |   | | |        / ____|"
PRINT #1, "    | | ___   | |_) | ___ | | __| | |_   _  | |  __  ___"
PRINT #1, "    | |/ _ \  |  _ < / _ \| |/ _` | | | | | | | |_ |/ _ \"
PRINT #1, "    | | (_) | | |_) | (_) | | (_| | | |_| | | |__| | (_) |"
PRINT #1, "    |_|\___/  |____/ \___/|_|\__,_|_|\__, |  \_____|\___/"
PRINT #1, "                                      __/ |"
PRINT #1, "                                     |___/"
PRINT #1, "*****"; GNAME$; "***** v" + TBG_Version$
PRINT #1, "Creation Date: "; TIME$; " "; DATE$
PRINT #1, "Generation Mode: "; CUSTOM$
PRINT #1, "Seed:"; SEED
PRINT #1, "Galaxy Type:"; GTYPE
PRINT #1, "Galaxy Age:"; AGE
PRINT #1, "Cluster Number:"; CLUSTERNUM
PRINT #1, "Planets: "; PENABLE$
PRINT #1, "Asteroids: "; ASTTOG$
PRINT #1, "L to Y class (~Brown~):"; LSTAR
PRINT #1, "M class (~Red~):"; MSTAR
PRINT #1, "K class (~Orange~):"; KSTAR
PRINT #1, "G class (~Yellow~):"; GSTAR
PRINT #1, "F class (~Yellow-white~):"; FSTAR
PRINT #1, "A class (~White~):"; ASTAR
PRINT #1, "B class (~Blue-White~):"; BSTAR
PRINT #1, "O class (~Blue~):"; OSTAR
PRINT #1, "White Dwarves:"; DWARFSTARNUMBER
PRINT #1, "-----------------"
PRINT #1, SOBJECTNUMBER; "Stars"
PRINT #1, POBJECTNUMBER; "Planets"
PRINT #1, MOBJECTNUMBER; "Moons"
PRINT #1, AOBJECTNUMBER; "Asteroids"
PRINT #1, SOBJECTNUMBER + POBJECTNUMBER + MOBJECTNUMBER + AOBJECTNUMBER; " Total"
PRINT #1, "-----------------"
CLOSE #1
'COLOR 15
'PRINT ""
'PRINT "DONE! Remember to place the config file 'galaxy.cfg' into a folder"
'PRINT "within /Gamedata labeled 'To_Boldly_Go'"

IF AGAIN$ = "n" THEN
    GOTO 888
END IF
SYSTEM

777 PRINT























_FONT _LOADFONT("font.ttf", 12, "MONOSPACE") 'select monospace font
_PRINTMODE _KEEPBACKGROUND

DIM Button(2) AS Button, Mouse(2) AS MouseInfo

VQB_Button_New Button(0), 15, 100, 100, 24, _RGB(0, 0, 0), _RGB(255, 255, 255), "Planets", 1
VQB_Button_New Button(1), 150, 100, 100, 24, _RGB(0, 0, 0), _RGB(255, 255, 255), "Asteroids", 1
VQB_Button_New Button(2), 350, 100, 100, 24, _RGB(0, 0, 0), _RGB(255, 255, 255), "Execute", 1

VQB_Button_Draw Button(0)
VQB_Button_Draw Button(1)
VQB_Button_Draw Button(2)

DIM SPONBUTTON AS LONG
SPONBUTTON = _LOADIMAGE("TOGLIGHTON.png")
_PUTIMAGE (11, 96), SPONBUTTON

DIM SAONBUTTON AS LONG
SAONBUTTON = _LOADIMAGE("ASTOGON.png")
_PUTIMAGE (146, 96), SAONBUTTON


DO
    _LIMIT 30
    VQB_Mouse_GetInfo Mouse(0)
    FOR I% = 0 TO 2
        IF VQB_Button_Click(Button(I%), Mouse(0)) THEN
            SELECT CASE I%
                CASE 0 '// Exit

                    IF PTOGGLE = 0 THEN
                        PTOGGLE = 1
                        DIM PONBUTTON AS LONG
                        PONBUTTON = _LOADIMAGE("TOGLIGHTON.png")
                        _PUTIMAGE (11, 96), PONBUTTON
                        '_SNDPLAYFILE "click.wav", .5
                        'PRINT "1"
                    ELSE
                        PTOGGLE = 0

                        DIM POFFBUTTON AS LONG
                        POFFBUTTON = _LOADIMAGE("TOGLIGHTOFF.png")
                        _PUTIMAGE (11, 96), POFFBUTTON
                        '_SNDPLAYFILE "click.wav", .5
                        'PRINT "0"
                    END IF
                    _DELAY 0.3
                CASE 1 '// another exit

                    IF ATOGGLE = 0 THEN
                        ATOGGLE = 1
                        DIM AONBUTTON AS LONG
                        AONBUTTON = _LOADIMAGE("ASTOGON.png")
                        _PUTIMAGE (146, 96), AONBUTTON
                        '_SNDPLAYFILE "click.wav", .5
                        'PRINT "1"
                    ELSE
                        ATOGGLE = 0

                        DIM AOFFBUTTON AS LONG
                        AOFFBUTTON = _LOADIMAGE("ASTOGOFF.png")
                        _PUTIMAGE (146, 96), AOFFBUTTON
                        '_SNDPLAYFILE "click.wav", .5
                        'PRINT "0"
                    END IF
                    _DELAY 0.3
                CASE 2
                    GOTO 778
            END SELECT
            '_SNDPLAYFILE "click.wav", .5
            EXIT FOR
        END IF
    NEXT
LOOP



TYPE Button
    Shape AS INTEGER '// 1=Square, 2=Ellipse
    X AS INTEGER '// Top left if square, Centre if ellipse
    Y AS INTEGER
    Width AS INTEGER '// Used as XRadius! if ellipse
    Height AS INTEGER '// Used as YRadius! if ellipse
    CLR AS LONG
    TextCLR AS LONG
    Text AS STRING * 24
    State AS INTEGER
END TYPE

TYPE MouseInfo
    X AS LONG
    Y AS LONG
    LMB AS INTEGER
    RMB AS INTEGER
END TYPE

SUB VQB_Frame (X%, Y%, Width%, Height%, CLR&)
    OldCLR& = CLR&
    LINE (X%, Y%)-(X% + Width%, Y% + Height%), CLR&, BF
    FOR Border% = 0 TO 4
        IF CLR& > _RGB(0, 0, 0) THEN
            NewRed& = _RED(CLR&) - (6 * Border%)
            NewGreen& = _GREEN(CLR&) - (6 * Border%)
            NewBlue& = _BLUE(CLR&) - (6 * Border%)
            CLR& = _RGB(NewRed&, NewGreen&, NewBlue&)
        ELSE
            NewRed& = _RED(CLR&) + (6 * Border%)
            NewGreen& = _GREEN(CLR&) + (6 * Border%)
            NewBlue& = _BLUE(CLR&) + (6 * Border%)
            CLR& = _RGBA(NewRed&, NewGreen&, NewBlue&, 120)
        END IF
        LINE (X% - Border%, Y% - Border%)-(X% + Width% + Border%, Y% - Border%), CLR&, BF
        LINE (X% - Border%, Y% + Height% + Border%)-(X% + Width% + Border%, Y% + Height% + Border%), CLR&, BF
        LINE (X% - Border%, Y% - Border%)-(X% - Border%, Y% + Height% + Border%), CLR&, BF
        LINE (X% + Width% + Border%, Y% - Border%)-(X% + Width% + Border%, Y% + Height% + Border%), CLR&, BF
    NEXT
    CLR& = OldCLR&
END SUB


'// Buttons

SUB VQB_Button_New (Button AS Button, X%, Y%, Width%, Height%, CLR&, TextClr&, Text$, Shape%)
    Button.X = X%
    Button.Y = Y%
    Button.Width = Width%
    Button.Height = Height%
    Button.CLR = CLR&
    Button.TextCLR = TextClr&
    Button.Text = Text$
    Button.Shape = Shape%
END SUB


SUB VQB_Button_Draw (Button AS Button)
    OldClr& = Button.CLR
    IF Button.Shape = 1 THEN '// Square button
        VQB_Frame Button.X, Button.Y, Button.Width, Button.Height, Button.CLR
        COLOR Button.TextCLR, _RGBA(0, 0, 0, 0)
        _PRINTSTRING (Button.X + (Button.Width / 2) - (_PRINTWIDTH(RTRIM$(Button.Text)) / 2), Button.Y + (_FONTHEIGHT / 4)), Button.Text
    ELSEIF Button.Shape = 2 THEN '// Ellipse button
        EllipseXS Button.X, Button.Y, Button.Width, Button.Height, 1, Button.CLR, _RGB(7, 7, 7)
        PAINT (Button.X, Button.Y), Button.CLR, Button.CLR
        EllipseXS Button.X, Button.Y, Button.Width, Button.Height, 12, Button.CLR, _RGB(7, 7, 7)
        COLOR Button.TextCLR, _RGBA(0, 0, 0, 0)
        _PRINTSTRING (Button.X - (_PRINTWIDTH(RTRIM$(Button.Text)) / 2), Button.Y - (_FONTHEIGHT / 2)), Button.Text
    END IF
    Button.CLR = OldClr&
END SUB


FUNCTION VQB_Button_Click (Button AS Button, Mouse AS MouseInfo)
IF Mouse.LMB THEN
    IF Button.Shape = 1 THEN
        IF Mouse.X >= Button.X AND Mouse.X <= Button.X + Button.Width THEN
            IF Mouse.Y >= Button.Y AND Mouse.Y <= Button.Y + Button.Height THEN
                VQB_Button_Click = -1
                IF Button.State THEN Button.State = 0 ELSE Button.State = -1
                EXIT FUNCTION
            END IF
        END IF
    ELSEIF Button.Shape = 2 THEN
        '// Ellipse detection adapted from a function created by DarthWho
        '// http://www.qb64.net/forum/index.php?topic=3154.15
        Xrad% = Button.Width + 12
        Yrad% = Button.Height + 12
        IF (Mouse.Y - Button.Y) ^ 2 + ((Mouse.X - Button.X) * Yrad% / Xrad%) ^ 2 <= Yrad% * Yrad% THEN
            VQB_Button_Click = -1
            IF Button.State THEN Button.State = 0 ELSE Button.State = -1
            EXIT FUNCTION
        END IF
    END IF
END IF
VQB_ButtonClick = 0
END FUNCTION


'// Graphics feature extracted from GDK_Draw 01
SUB EllipseXS (X%, Y%, XRadius!, YRadius!, Wide%, CLR&, ShadeClr&)
FOR j% = 0 TO Wide% - 1
    IF _RED(CLR&) <= 255 AND _RED(ShadeClr&) > 0 THEN newred& = _RED(CLR&) - _RED(ShadeClr&)
    IF _BLUE(CLR&) <= 255 AND _BLUE(ShadeClr&) > 0 THEN newblue& = _BLUE(CLR&) - _BLUE(ShadeClr&)
    IF _GREEN(CLR&) <= 255 AND _GREEN(ShadeClr&) > 0 THEN newgreen& = _GREEN(CLR&) - _GREEN(ShadeClr&)
    CLR& = _RGB(newred&, newgreen&, newblue&)
    IF XRadius! > YRadius! THEN Radius! = XRadius! ELSE Radius! = YRadius!
    MinStep! = 1 / (2 * 3.1415926535 * Radius!) '<<< Thanks to CodeGuy for this optimisation.
    FOR i = 0 TO 8 * ATN(1) STEP MinStep!
        pointx% = X% + (XRadius! * COS(i))
        pointy% = Y% + (YRadius! * SIN(i))
        PSET (pointx%, pointy%), CLR&
    NEXT
    XRadius! = XRadius! + 1
    YRadius! = YRadius! + 1
NEXT
END SUB


'// Mouse Input

SUB VQB_Mouse_GetInfo (Mouse AS MouseInfo)
DO
    Mouse.RMB = _MOUSEBUTTON(2)
    Mouse.LMB = _MOUSEBUTTON(1)
    Mouse.X = _MOUSEX
    Mouse.Y = _MOUSEY
LOOP WHILE _MOUSEINPUT
END SUB

SUB makeStarNameList (numbRequestedStars)
    '###########################
    '#read in star name prefixes
    REDIM arrayPrefixes$(0)
    theFileName$ = "Data_Folder/TBG_Prefixes.txt"
    IF _FILEEXISTS(theFileName$) THEN
        OPEN theFileName$ FOR INPUT AS #2
        filecount% = 0
        DO UNTIL EOF(2)
            LINE INPUT #2, file$ 'read entire text file line
            arrayPrefixes$(filecount%) = file$
            filecount% = filecount% + 1
            REDIM _PRESERVE arrayPrefixes$(filecount%)
        LOOP
        CLOSE #2
    END IF
    '###########################
    '#read in star name suffixes
    REDIM arraySuffixes$(0)
    theFileName$ = "Data_Folder/TBG_Suffixes.txt"
    IF _FILEEXISTS(theFileName$) THEN
        OPEN theFileName$ FOR INPUT AS #2
        filecount% = 0
        DO UNTIL EOF(2)
            LINE INPUT #2, file$ 'read entire text file line
            arraySuffixes$(filecount%) = file$
            filecount% = filecount% + 1
            REDIM _PRESERVE arraySuffixes$(filecount%)
        LOOP
        CLOSE #2
    END IF
    '########################################################
    '# pick a random index from the prefix and suffix arrays'
    '# the equiv in python would be:
    '# PREFIX = random.choice(thePrefixes)
    '# SUFFIX = random.choice(theSuffixes)
    FOR i = 0 TO numbRequestedStars
        lengArrayPrefixes% = UBOUND(arrayPrefixes$)
        lengArraySuffixes% = UBOUND(arraySuffixes$)
        indexPrefixes% = INT(RND * lengArrayPrefixes%)
        indexSuffixes% = INT(RND * lengArraySuffixes%)
        PREFIX$ = arrayPrefixes$(indexPrefixes%)
        SUFFIX$ = arraySuffixes$(indexSuffixes%)
        '##############################################
        '# combine the prefix and suffix to make a name
        fullStarName$ = PREFIX$ + SUFFIX$
        '#hard coded avoidance of 'sun' and 'core'
        IF fullStarName$ = "Sun" OR fullStarName$ = "Core" THEN
            indexSuffixes% = INT(RND * lengArraySuffixes%)
            SUFFIX$ = arraySuffixes$(indexSuffixes%)
            fullStarName$ = fullStarName$ + "o'" + SUFFIX$
        END IF
        '#I guess qbasic doesn't have a way of boolean testing to see if a value is in an array?
        '####First look and see if the proposed name is in the template name array'
        FOR j = 1 TO UBOUND(planetKey$)
            DO UNTIL fullStarName$ <> planetKey$(j)
                indexSuffixes% = INT(RND * lengArraySuffixes%)
                SUFFIX$ = arraySuffixes$(indexSuffixes%)
                fullStarName$ = fullStarName$ + "o'" + SUFFIX$
            LOOP
        NEXT
        '#do the same sort of check and make sure the star name hasn't been used already
        FOR j = 1 TO UBOUND(starNameList$)
            DO UNTIL fullStarName$ <> starNameList$(j)
                indexSuffixes% = INT(RND * lengArraySuffixes%)
                SUFFIX$ = arraySuffixes$(indexSuffixes%)
                fullStarName$ = fullStarName$ + "a'" + SUFFIX$
            LOOP
        NEXT
        starNameList$(i) = fullStarName$
    NEXT
END SUB

FUNCTION fileAsString$ (fileName$)
    '###########################
    '#read in string template
    theFileName$ = "Data_Folder/templates/" + fileName$
    wholeTxt$ = ""
    IF _FILEEXISTS(theFileName$) THEN
        OPEN theFileName$ FOR INPUT AS #3
        DO UNTIL EOF(3)
            LINE INPUT #3, fileLine$ 'read entire text file line
            wholeTxt$ = wholeTxt$ + fileLine$ + CHR$(10)
        LOOP
        CLOSE #3
    END IF
    fileAsString$ = wholeTxt$
END FUNCTION

'################################################
'########http://www.qb64.net/wiki/index.php/LEFT$
FUNCTION ReplaceStr$ (text$, old$, new$)
    DO
        find = INSTR(start + 1, text$, old$) 'find location of a word in text
        IF find THEN
            count = count + 1
            first$ = LEFT$(text$, find - 1) 'text before word including spaces
            last$ = RIGHT$(text$, LEN(text$) - (find + LEN(old$) - 1)) 'text after word
            text$ = first$ + new$ + last$
        END IF
        start = find
    LOOP WHILE find
    'Replace = count 'function returns the number of replaced words. Comment out in SUB
    'Replace = text$
    ReplaceStr$ = text$
END FUNCTION

FUNCTION propertyNode$ (aTemplate$, theDescription$, theRadius$, theMass$, theGravParam$, theGeeASL$, theDoesRotate$, theRotationPeriod$, theInitialRotation$, theIsTidallyLocked$, theIsHomeWord$, inLWHZ$, inLMHZ$, theSOI$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    '###########################'
    '##Uncomment properties if data is present
    IF theDescription$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%description =", "%description =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theDescription)s", theDescription$)
    END IF
    '#STH 2018-0516. More dogshit code. 
    '#Why doesn't "IF (theRadius$ <> "" THEN IF val(theRadius$) <> 0) THEN" work?
    IF theRadius$ <> "" THEN IF val(theRadius$) > 0 THEN
            aTemplate$ = ReplaceStr(aTemplate$, "//%radius =", "%radius =")
            aTemplate$ = ReplaceStr(aTemplate$, "%(theRadius)s", str$(val(theRadius$)+1))
    END IF 
    END IF
    IF theMass$ <> "" THEN IF val(theMass$) > 0 THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%mass =", "%mass =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theMass)s", theMass$)
    END IF
    END IF
    IF theGravParam$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%gravParameter =", "%gravParameter =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theGravParameter)s", theGravParam$)
    END IF
    IF theGeeASL$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%geeASL =", "%geeASL =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theGeeASL)s", theGeeASL$)
    END IF
    IF theDoesRotate$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%rotates =", "%rotates =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(doesRotate)s", theDoesRotate$)
    END IF
    IF theRotationPeriod$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%rotationPeriod =", "%rotationPeriod =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(rotationPeriod)s", theRotationPeriod$)
    END IF
    IF theInitialRotation$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%initialRotation =", "%initialRotation =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(initialRotation)s", theInitialRotation$)
    END IF
    IF theIsTidallyLocked$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%tidallyLocked =", "%tidallyLocked =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(isTidallyLocked)s", theIsTidallyLocked$)
    END IF
    IF theIsHomeWord$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%isHomeWorld =", "%isHomeWorld =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(isHomeWorld)s", theIsHomeWord$)
    END IF
    IF inLWHZ$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "%(inLWHZ)s", inLWHZ$)
    END IF
    IF inLMHZ$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "%(inLMHZ)s", inLMHZ$)
    END IF
    IF theSOI$ <> "" THEN IF val(theSOI$) > 0 THEN 
        aTemplate$ = ReplaceStr(aTemplate$, "//%sphereOfInfluence =", "%sphereOfInfluence =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theSphereOfInfluence)s", theSOI$)
    END IF
    END if
    '###########################'
    propertyNode$ = aTemplate$
END FUNCTION

FUNCTION orbitNode$ (aTemplate$, theReferenceBody$, theColour$, theMode$, theInclination$, theEccentricity$, theSemiMajorAxis$, theLongitudeOfAscendingNode$, theArgumentOfPeriapsis$, theMeanAnomalyAtEpoch$, theEpoch$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    IF theReferenceBody$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%referenceBody =", "%referenceBody =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theReferenceBody)s", theReferenceBody$)
    END IF
    IF theColour$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%color =", "%color =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theColour)s", theColour$)
    END IF
    IF theMode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%mode =", "%mode =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theMode)s", theMode$)
    END IF
    IF theInclination$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%inclination =", "%inclination =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theInclination)s", theInclination$)
    END IF
    IF theEccentricity$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%eccentricity =", "%eccentricity =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theEccentricity)s", theEccentricity$)
    END IF
    IF theSemiMajorAxis$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%semiMajorAxis =", "%semiMajorAxis =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theSemiMajorAxis)s", theSemiMajorAxis$)
    END IF
    IF theLongitudeOfAscendingNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%longitudeOfAscendingNode =", "%longitudeOfAscendingNode =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theLongitudeOfAscendingNode)s ", theLongitudeOfAscendingNode$)
    END IF
    IF theArgumentOfPeriapsis$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%argumentOfPeriapsis =", "%argumentOfPeriapsis =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theArgumentOfPeriapsis)s", theArgumentOfPeriapsis$)
    END IF
    IF theMeanAnomalyAtEpoch$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%meanAnomalyAtEpoch =", "%meanAnomalyAtEpoch =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theMeanAnomalyAtEpoch)s", theMeanAnomalyAtEpoch$)
    END IF
    IF theEpoch$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%epoch =", "%epoch =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theEpoch)s", theEpoch$)
    END IF
    orbitNode$ = aTemplate$
END FUNCTION

FUNCTION lightNode$ (aTemplate$, sunlightColor$, sunlightIntensity$, scaledSunlightColor$, scaledSunlightIntensity$, IVASuncolor$, IVASunIntensity$, sunLensFlareColor$, ambientLightColor$, sunAU$, luminosity$, givesOffLight$, skyBrightness$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    IF sunlightColor$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//sunlightColor =", "sunlightColor =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theSunlightColor)s", sunlightColor$)
    END IF
    IF sunlightIntensity$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//sunlightIntensity =", "sunlightIntensity =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theSunlightIntensity)s", sunlightIntensity$)
    END IF
    IF scaledSunlightColor$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//scaledSunlightColor =", "scaledSunlightColor =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theScaledSunlightColor)s", scaledSunlightColor$)
    END IF
    IF scaledSunlightIntensity$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//scaledSunlightIntensity =", "scaledSunlightIntensity =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theScaledSunlightIntensity)s", scaledSunlightIntensity$)
    END IF
    IF IVASuncolor$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//IVASuncolor =", "IVASuncolor =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theIVASuncolor)s", IVASuncolor$)
    END IF
    IF IVASunIntensity$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//IVASunIntensity =", "IVASunIntensity =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theIVASunIntensity)s", IVASunIntensity$)
    END IF
    IF sunLensFlareColor$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//sunLensFlareColor =", "sunLensFlareColor =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theSunLensFlareColor)s", sunLensFlareColor$)
    END IF
    IF ambientLightColor$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//ambientLightColor =", "ambientLightColor =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theAmbientLightColor)s", ambientLightColor$)
    END IF
    IF sunAU$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//sunAU =", "sunAU =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theSunAU)s", sunAU$)
    END IF
    IF luminosity$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//luminosity =", "luminosity =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theLuminosity)s", luminosity$)
    END IF
    IF givesOffLight$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//givesOffLight =", "givesOffLight =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theGivesOffLight)s", givesOffLight$)
    END IF
    IF givesOffLight$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//key = 0", "key = 0")
        aTemplate$ = ReplaceStr(aTemplate$, "%(skyBrightness)s", skyBrightness$)
    END IF
    lightNode$ = aTemplate$
END FUNCTION

FUNCTION materialNode$ (aTemplate$, emitColorZero$, emitColorOne$, sunspotColor$, rimColor$, rimPower$, rimBlend$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    aTemplate$ = ReplaceStr(aTemplate$, "%(theEmitColor0)s", emitColorZero$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(theEmitColor1)s", emitColorOne$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSunspotColor)s", sunspotColor$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(theRimColor)s", rimColor$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(theRimPower)s", rimPower$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(theRimBlend)s", rimBlend$)
    materialNode$ = aTemplate$
END FUNCTION

FUNCTION coronaNode$ (aTemplate$, starColour$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    aTemplate$ = ReplaceStr(aTemplate$, "%(theTexture)s", starColour$)
    coronaNode$ = aTemplate$
END FUNCTION

FUNCTION ringNode$ (aTemplate$, theAngle$, theOuterRadius$, theInnerRadius$, theRingTexture$, theColour$, theLockRotation$, theUnlit$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    IF theAngle$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//angle =", "angle =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theAngle)s", theAngle$)
    END IF
    IF theOuterRadius$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//outerRadius =", "outerRadius =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theOuterRadius)s", theOuterRadius$)
    END IF
    IF theInnerRadius$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//innerRadius =", "innerRadius =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theInnerRadius)s", theInnerRadius$)
    END IF
    IF theRingTexture$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//texture =", "texture =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theRingTexture)s", theRingTexture$)
    END IF
    IF theColour$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//color =", "color =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theColour)s", theColour$)
    END IF
    IF theLockRotation$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//lockRotation =", "lockRotation =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theLockRotation)s", theLockRotation$)
    END IF
    IF theUnlit$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//unlit =", "unlit =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theUnlit)s", theUnlit$)
    END IF
    ringNode$ = aTemplate$
END FUNCTION

FUNCTION city2Node$ (aTemplate$, city2Altitude$, city2Latitude$, city2Longitude$, city2isCommnetStation$, city2isKSC$, city2Name$, city2ModelPath$, city2Scale$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2Altitude)s", city2Altitude$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2Latitude)s", city2Latitude$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2Longitude)s", city2Longitude$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2isCommnetStation)s", city2isCommnetStation$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2isKSC)s", city2isKSC$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2Name)s", city2Name$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2ModelPath)s", city2ModelPath$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(city2Scale)s", city2Scale$)
    city2Node$ = aTemplate$
END FUNCTION

FUNCTION PQSNode$ (aTemplate$, vertexSimplexHeightAbsoluteSeed$, vertexHeightNoiseSeed$, voronoiCratersSimplexSeed$, voronoiCratersVoronoiSeed$, aCity2Node$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    IF aCity2Node$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theCity2)s", aCity2Node$)
    END IF
    aTemplate$ = ReplaceStr(aTemplate$, "%(vertexSimplexHeightAbsoluteSeed)s", vertexSimplexHeightAbsoluteSeed$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(vertexHeightNoiseSeed)s", vertexHeightNoiseSeed$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(voronoiCratersSimplexSeed)s", voronoiCratersSimplexSeed$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(voronoiCratersVoronoiSeed)s", voronoiCratersVoronoiSeed$)
    PQSNode$ = aTemplate$
END FUNCTION

SUB readPlanetTemplates ()
    '####2017.0201--STH
    '#This is a mess. I want something like python's dictionary
    '#Played with a multidimensional array, but can't redim it?
    '#Ended up using an array for each colum read in from the CSV
    '#Terrible technique, but I just want it to work at this point
    '###################'
    theFileName$ = "Data_Folder/TBG_Planet_Templates.csv"
    theIndex = 0
    IF _FILEEXISTS(theFileName$) THEN
        OPEN theFileName$ FOR INPUT AS #1
        'read through the file and get the number of lines'
        DO UNTIL EOF(1)
            REDIM _PRESERVE planetKey$(theIndex)
            REDIM _PRESERVE thePlanetRadius(theIndex)
            REDIM _PRESERVE thePlanetMass(theIndex)
            REDIM _PRESERVE thePlanetSOI(theIndex)
            REDIM _PRESERVE thePlanetDesc$(theIndex)
            REDIM _PRESERVE thePlanetStock$(theIndex)
            INPUT #1, aPlanetStock$, aPlanetName$, aPlanetRadius, aPlanetMass, aPlanetSOI, aDescription$
            planetKey$(theIndex) = aPlanetName$
            thePlanetRadius(theIndex) = aPlanetRadius
            thePlanetMass(theIndex) = aPlanetMass
            thePlanetSOI(theIndex) = aPlanetSOI
            thePlanetDesc$(theIndex) = aDescription$
            thePlanetStock$(theIndex) = aPlanetStock$
            theIndex = theIndex + 1
        LOOP
        CLOSE #1
    END IF
END SUB

FUNCTION AU2km (theAU)
    AU2km = theAU * 149597871
END FUNCTION

FUNCTION realKM2kerbinKM (realKM)
    '#from discussion with Gregrox on Kopernicus discord
    '#one way to convert to/from kerbin space is:
    '#Earth SMA/Kerbin SMA = 10.9999726
    realKM2kerbinKM = realKM / 10.9999726
END FUNCTION

FUNCTION kerbinKM2realKM (kerbinKM)
    '#from discussion with Gregrox on Kopernicus discord
    '#one way to convert to/from kerbin space is:
    '#Earth SMA/Kerbin SMA = 10.9999726
    kerbinKM2realKM = kerbinKM * 10.9999726
END FUNCTION

FUNCTION realKM2Parsec (realKM)
    '#1 km = 3.2407792896664E-14 pc
    realKM2Parsec = realKM*3.2407792896664E-14
END FUNCTION

FUNCTION solarMass2kg (SM)
    '#use Sol's solar mass and kg mass to convert
    '#Sol is ~1.989e30kg
    solarMass2kg = 1.98855E30 * SM
END FUNCTION

FUNCTION kg2solarMass (the_kg)
    '#use Sol's solar mass and kg mass to convert
    '#Sol is ~1.989e30kg
    kg2solarMass = the_kg / 1.98855E30
END FUNCTION

FUNCTION sol2Kerbol_kg (the_kg)
    '#The start Kerbol is 113.2393x less massiv than Sol
    sol2Kerbol_kg = the_kg / 113.2393
END FUNCTION

FUNCTION kerbol2Sol_kg (the_kg)
    '#The start Kerbol is 113.2393x less massiv than Sol
    kerbol2Sol_kg = the_kg * 113.2393
END FUNCTION

FUNCTION sol2Kerbol_km (the_km)
    '#The start Kerbol is 2.6594x smaller in radius than Sol
    sol2Kerbol_km = the_km / 2.6594
END FUNCTION

FUNCTION kerbol2Sol_km (the_km)
    '#The start Kerbol is 2.6594x smaller in radius than Sol
    kerbol2Sol_km = the_km * 2.6594
END FUNCTION

FUNCTION solarRadius2km (SR)
    '#use Sol's solar radius and km radius to convert
    '#Sol is ~695700km
    solarRadius2km = 695700.0 * SR
END FUNCTION

FUNCTION km2solarRadius (SR)
    '#use Sol's solar radius and km radius to convert
    '#Sol is ~695700km
    km2solarRadius = SR / 695700.0
END FUNCTION

FUNCTION solarRadiusFromSolarMass (SM)
    '#need a good reference for this
    IF SM < 1 THEN
        SR = SM ^ 0.5
    ELSE
        SR = SM ^ 0.8
    END IF
    solarRadiusFromSolarMass = SR
END FUNCTION

FUNCTION luminosityFromSolarMass (SM)
    luminosityFromSolarMass = SM ^ 3.5
END FUNCTION

FUNCTION absMagFromLuminosity(theLuminosity)
    ratioLum = theLuminosity/78.70
    theLogTen# = log(ratioLum)/log(10.#)
    absMagFromLuminosity = -2.5 * theLogTen#
END FUNCTION

FUNCTION apparentMagFromAbsMag(absMag, theDistance)
    '#the Distance has to be in parsecs
    apparentMagFromAbsMag=5*LOG(theDistance/10)+absMag
ENd FUNCTION

FUNCTION solarTemp (SL, SR)
    '#returns star temp in K from solar luminocty and solar mass
    solarTemp = ((SL / (SR ^ 2.0)) ^ 0.25) * 5778
END FUNCTION

FUNCTION starCircumference (radius_km)
    starCircumference = 2.0 * _PI * radius_km
END FUNCTION

FUNCTION starSurfaceArea (radius_km)
    starSurfaceArea = 4.0 * _PI * (radius_km ^ 2.0)
END FUNCTION

FUNCTION starVolume (radius_km)
    '#return in m^3
    radius_m = radius_km * 1000.0
    starVolume = (4.0 / 3.0) * _PI * (radius_m ^ 3.0)
END FUNCTION

FUNCTION starDensity (mass_kg, radius_km)
    theVolume = starVolume(radius_km)
    starDensity = mass_kg / theVolume
END FUNCTION

FUNCTION stdGravitationalParameter (mass_kg)
    '#https://en.wikipedia.org/wiki/Standard_gravitational_parameter
    G = 6.674E-11
    stdGravitationalParameter = (mass_kg * G)
END FUNCTION

FUNCTION surfaceGravity (mass_kg, radius_km)
    '#https://en.wikipedia.org/wiki/Surface_gravity
    G = 6.674E-11
    surfaceGravity = G * (mass_kg / (radius_km ^ 2.0))
END FUNCTION

FUNCTION escapeVelocity (mass_kg, radius_km)
    G = 6.674E-11
    temp = 2.0 * G * mass_kg
    temp = temp / radius_km
    escapeVelocity = temp ^ 0.5
END FUNCTION

FUNCTION hillSphere (mass_primary, mass_secondary, eccentricity_secondary, semimajorAxis_secondary)
    '#calculate the radius of the Hill sphere
    '#https://en.wikipedia.org/wiki/Hill_sphere
    partOne = (semimajorAxis_secondary * (1.0 - eccentricity_secondary))
    partTwo = (mass_secondary / (3.0 * mass_primary)) ^ (1.0 / 3.0)
    theRadius = partOne * partTwo
    '#for unit test later:
    '#mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; semi-major axis earth = 149,598,023 km; eccentricity earth = 0.0167086
    '#gives a radius of 1471536.617 km
    '#mass blackhole @ center of milky way: 8.55E+37 kg
    hillSphere = theRadius
END FUNCTION

FUNCTION simpleRocheLimit (mass_primary)
    '#If the orbiting body does not have a mass or radius provided
    '#the standard roche limit calc can't be used'
    '#use this dogshit instead.
    '#returns units in km
    simpleRocheLimit = (7.52E-23)*mass_primary
END FUNCTION

FUNCTION rocheLimit (mass_primary, mass_secondary, radius_primary, radius_secondary)
    '#calculate the Roche limit around a body
    '#this is the minimum distance around a primary that a secondary can maintain cohesion
    '#Any closer and you would have a ring instead
    '#https://en.wikipedia.org/wiki/Roche_limit
    densityPrimary = starDensity(mass_primary, radius_primary/1000.0) '#mass in kg, radius in km so divide by 1000
    densitySecondary = starDensity(mass_secondary, radius_secondary/1000.0) '#mass in kg, radius in km so divide by 1000
    theDistance = 1.26 * radius_primary*((densityPrimary/densitySecondary)^(1.0/3.0))
    '#for unit test later:
    '#mass earth = 5.97E+24 kg; mass sol = 1.98855E+30 kg; radius earth = 6378 km
    '#gives a radius of 556,396.86 km
    rocheLimit = theDistance
END FUNCTION

FUNCTION kspSOI (mass_primary, mass_secondary, semimajorAxis_secondary)
    '#http://wiki.kerbalspaceprogram.com/wiki/Sphere_of_influence
    kspSOI = (semimajorAxis_secondary * ((mass_secondary / mass_primary) ^ (2.0 / 5.0)))
END FUNCTION

FUNCTION solFrostLine (luminocity)
    'https://en.wikipedia.org/wiki/Frost_line_(astrophysics)
    solFrostLine = 4.85 * (luminocity ^ 0.5) '#returns units in AU
END FUNCTION

FUNCTION siderealRotationalVel (theRadius, rotationalPeriod)
    theVelocity = starCircumference(theRadius) / rotationalPeriod
    siderealRotationalVel = theVelocity
END FUNCTION

FUNCTION innerLWHZ (theMass)
    '#uses solar mass for calcs
    '#returns distance in kerbal meters
    '#convert kerbal mass to real world mass
    theMass = 1.7565459E+28
    rwKG = kerbol2Sol_kg(theMass)
    '#convert real world kilograms to solar masses
    rwSM = kg2solarMass(rwKG)

    realAU=0.95*(rwSM^1.5)
    realKM=AU2km(realAU)
    kerbalM=realKM2kerbinKM(realKM)*1000
    innerLWHZ = kerbalM
END FUNCTION

FUNCTION outerLWHZ (theMass)
    '#uses solar mass for calcs
    '#returns distance in kerbal meters
    '#convert kerbal mass to real world mass
    rwKG = kerbol2Sol_kg(theMass)
    '#convert real world kilograms to solar masses
    rwSM = kg2solarMass(rwKG)

    realAU=1.37*(rwSM^1.5)
    realKM=AU2km(realAU)
    kerbalM=realKM2kerbinKM(realKM)*1000
    outerLWHZ = kerbalM
END FUNCTION

FUNCTION innerLMHZ (theMass)
    '#uses solar mass for calcs
    '#returns distance in kerbal meters
    '#convert kerbal mass to real world mass
    'print #1, str$(theMass)
    rwKG = kerbol2Sol_kg(theMass)
    'print #1, str$(rwKG)
    '#convert real world kilograms to solar masses
    rwSM = kg2solarMass(rwKG)
    'print #1, str$(rwSM)

    realAU=((rwSM^3.5)/0.057)^0.5
    'print #1, str$(realAU)
    realKM=AU2km(realAU)
    kerbalM=realKM2kerbinKM(realKM)*1000
    'print #1, str$(kerbalM)
    innerLMHZ = kerbalM
END FUNCTION

FUNCTION outerLMHZ (theMass)
    '#uses solar mass for calcs
    '#returns distance in kerbal meters
    '#convert kerbal mass to real world mass
    rwKG = kerbol2Sol_kg(theMass)
    '#convert real world kilograms to solar masses
    rwSM = kg2solarMass(rwKG)

    realAU=((rwSM^3.5)/0.007)^0.5
    realKM=AU2km(realAU)
    kerbalM=realKM2kerbinKM(realKM)*1000
    outerLMHZ = kerbalM
END FUNCTION

FUNCTION synchronousOrbit (theRadius, theMass, rotationalPeriod)
    '#returns the altitude of geosync orbit above sea level
    G = 6.674E-11
    tmpOne = (G * theMass * (rotationalPeriod ^ 2.0))
    tmpTwo = 4.0 * (_PI ^ 2.0)
    tmpThr = (tmpOne / tmpTwo) ^ (1.0 / 3.0)
    theAltitude = tmpThr - theRadius
    synchronousOrbit = theAltitude
END FUNCTION

'#I miss python
FUNCTION pol2cartY(rho, theta)
    '#theta is in degrees
    pol2cartY = rho * sin(theta*0.017453)
END FUNCTION
FUNCTION pol2cartX(rho, theta)
    '#theta is in degrees
    pol2cartX = rho * cos(theta*0.017453)
END FUNCTION

FUNCTION theStarDistance (x1,x2,y1,y2)
    theStarDistance = (((x2-x1)^2)+((y2-y1)^2))^0.5
END FUNCTION

'#star colour RGB from temp
SUB temp2RGB (tmpKelvin):
    '#temps in kelvins
    '#line equations derived using blackbody values from
    '#http://www.vendian.org/mncharity/dir3/blackbody/UnstableURLs/bbr_color.html

    if tmpKelvin<1900 then b = 0
    if tmpKelvin>=1900 and tmpKelvin<=6600 then
        b = int(-1479.374+(196.95357*log(tmpKelvin)))
    end if
    if tmpKelvin<=6600 then 
        r = 255  
        g = int(2.71828^(5.7834281-(1686.3889*(1.0/tmpKelvin))))
    end if
    if tmpKelvin>6600 then
        r = int(1.0/(0.0066897-(18.585712*(1.0/tmpKelvin))))
        g = int(1.0/(0.0057629-(11.79832*(1.0/tmpKelvin))))
        b = 255
    end if
    REDgb = r
    rGREENb = g
    rgBLUE = b
END SUB




FUNCTION starTempSubstitution$ (aTemplate$, aName$, aPropertiesNode$, aOrbitNode$, aRingNode$, aLightNode$, aMaterialNode$, aCoronaNode$, aSolarPowerCurve$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    '###########################'
    IF aName$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%name =", "%name =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theName)s", aName$)
    END IF
    IF aPropertiesNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theProperties)s", aPropertiesNode$)
    END IF
    IF aOrbitNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theOrbitData)s", aOrbitNode$)
    END IF
    IF aRingNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theRingData)s", aRingNode$)
    END IF
    IF aLightNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theLightData)s", aLightNode$)
    END IF
    IF aMaterialNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theMaterialData)s", aMaterialNode$)
    END IF
    IF aCoronaNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theCoronasData)s", aCoronaNode$)
    END IF
    IF aSolarPowerCurve$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theSolarPowerCurve)s", aSolarPowerCurve$)
    END IF

    '###########################'
    starTempSubstitution$ = aTemplate$
END FUNCTION

FUNCTION planetTempSubstitution$ (aTemplate$, aBodyNode$, aName$, aTemplateNode$, aPropertiesNode$, aOrbitNode$, aScaledVerionNode$, aRingNode$, aAtmosphereNode$, aPQSNode$, aOceanNode$, aDebugNode$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    '###########################'
    IF aBodyNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theBodyData)s", aBodyNode$)
    END IF
    IF aName$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%name =", "%name =")
        aTemplate$ = ReplaceStr(aTemplate$, "%(theName)s", aName$)
    END IF
    IF aTemplateNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theTemplateData)s", aTemplateNode$)
    END IF
    IF aPropertiesNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theProperties)s", aPropertiesNode$)
    END IF
    IF aOrbitNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theOrbitData)s", aOrbitNode$)
    END IF
    IF aRingNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theRingData)s", aRingNode$)
    END IF
    IF aScaledVerionNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theScaledVersion)s", aScaledVerionNode$)
    END IF
    IF aAtmosphereNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theAtmosphere)s", aAtmosphereNode$)
    END IF
    IF aPQSNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(thePQS)s", aPQSNode$)
    END IF
    IF aOceanNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theOcean)s", aOceanNode$)
    END IF
    IF aDebugNode$ <> "" THEN
        aTemplate$ = ReplaceStr(aTemplate$, "//%(theDebug)s", aDebugNode$)
    END IF

    '###########################'
    planetTempSubstitution$ = aTemplate$
END FUNCTION

FUNCTION wikiEntry$ (aTemplate$, star_HTMLColour$, star_Name$, star_RadiusKSP, star_Circumference, star_SurfaceArea, star_MassKSP, star_stdGravitationalParameter, star_Density, star_surfaceGravity, star_escapeVelocity, star_RotationalPeriod, star_siderealRotationalVel, star_theSynchronousOrbit, star_SOI, star_FrostLine, star_TempK, star_Lum, star_AbsMag, star_semimajorAxis, star_distToKerbol, star_ApparentMag)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    '###########################'
    aTemplate$ = ReplaceStr(aTemplate$, "%(htmlColour)s", star_HTMLColour$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(starName)s", star_Name$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(theRadius)i", STR$(star_RadiusKSP))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theCircumfrence)g", STR$(star_Circumference))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSurfaceArea)g", STR$(star_SurfaceArea))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theMass)g", STR$(star_MassKSP))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theStdGrav)g", STR$(star_stdGravitationalParameter))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theDensity)g", STR$(star_Density))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSurfaceGravity)g", STR$(star_surfaceGravity))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theEscapeVelocity)g", STR$(star_escapeVelocity))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theRotationPeriod)g", STR$(star_RotationalPeriod))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSideralVelocity)g", STR$(star_siderealRotationalVel))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSynchronousOrbit)f", STR$(star_theSynchronousOrbit))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSOI)g", STR$(star_SOI))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theFrostLine)g", STR$(star_FrostLine))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theTemp)g", STR$(star_TempK))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theLuminosity)g", STR$(star_Lum))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theAbsMagnitude)g", STR$(star_AbsMag))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theApparentMagnitude)g", STR$(star_ApparentMag))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theSMA)i", STR$(star_semimajorAxis))
    aTemplate$ = ReplaceStr(aTemplate$, "%(theDistToKerbol)i", STR$(star_distToKerbol))
    '###########################'
    wikiEntry$ = aTemplate$
END FUNCTION

FUNCTION forResearchBodies$ (aTemplate$, ignoreStrings$, onDiscoveryStrings$, onIgnoreLevelStrings$, localizationTextUS$)
    '#####STH 2017-0124. QBasic doesn't have string formatting like python.
    '#####Replicated that function with string replacement function.
    '###########################'
    aTemplate$ = ReplaceStr(aTemplate$, "%(ignoreStrings)s", ignoreStrings$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(onDiscoveryStrings)s", onDiscoveryStrings$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(onIgnoreLevelStrings)s", onIgnoreLevelStrings$)
    aTemplate$ = ReplaceStr(aTemplate$, "%(localizationText)s", localizationTextUS$)
    '###########################'
    forResearchBodies$ = aTemplate$
END FUNCTION

'$INCLUDE: 'Source\MakeAsteroids.bm'
'$INCLUDE: 'Source\MakeMoons.bm'
'$INCLUDE: 'Source\MakePlanets.bm'
'$INCLUDE: 'Source\MakeStars.bm'
    
