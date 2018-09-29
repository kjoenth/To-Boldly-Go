#To Boldly Go v0.3.1.2 - Kopernicus Procedural Galaxy Generator!
#Copyright (C) 2018  Daniel L. & Sean T. Hammond

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#PGNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

TBG_Version = "0.3.1.2"

import random

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
#RANDOMIZE SEED

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
if (CUSTOM!="c") or (ADVANCED!="y"):
    AGE = random.randint(0,5)
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

if CUSTOM!="c":
    PENABLE = "y"
    ASTTOG = "y"
    GTYPE = random.randint(0,2)
    if GTYPE == 2:
        CLUSTER =random.randint(1,4)

# numbRequestedStars = OSTAR + BSTAR + ASTAR + FSTAR + GSTAR + KSTAR + MSTAR + LSTAR + DWARFSTAR + CLUSTER
# DIM SHARED starNameList$(0 TO numbRequestedStars)
# CALL makeStarNameList(numbRequestedStars)
# '################################
# '#Make the cfg header text
# '###Insert 10 empty lines
# FOR i = 1 TO 10
#     PRINT #1, ""
# NEXT
# PRINT #1, "// WARNING! SPOILERS!"
# PRINT #1, "// This file contains spoilers. If you don't want to have your surprises ruined, you should stop reading now."
# '###Insert 34 empty lines'
# FOR i = 1 TO 34
#     PRINT #1, ""
# NEXT
# PRINT #1, "// Seriously, it's a lot more fun to find this stuff out in the game."
# PRINT #1, "// Last chance to turn back."
# '###Insert 28 empty lines'
# FOR i = 1 TO 28
#     PRINT #1, ""
# NEXT
# PRINT #1, "// I did warn you."
# '###Insert 6 empty lines'
# FOR i = 1 TO 6
#     PRINT #1, ""
# NEXT

# PRINT #1, "//Generated by To Boldly Go, version " + TBG_Version$
# PRINT #1, "//Seed: " + STR$(SEED)
# '#End the cfg header text'
# '#############################
# '###Read in the string templates
# DIM SHARED thePropertiesTemplate$, theOrbitTemplate$, theLightTemplate$, theMaterialTemplate$, theCoronasTemplate$
# DIM SHARED theGasGiantTemplate$, theRingsTemplate$, theOceanTemplate$, thePlanetTemplate$, theStarTmp$, theWikiTemplate$
# thePropertiesTemplate$ = fileAsString("propertiesTmp.txt")
# theOrbitTemplate$ = fileAsString("orbitTmp.txt")
# theLightTemplate$ = fileAsString("lightTmp.txt")
# theMaterialTemplate$ = fileAsString("materialTmp.txt")
# theCoronasTemplate$ = fileAsString("coronaTmp.txt")
# theGasGiantTemplate$ = fileAsString("gasGiantScaledVersionTmp.txt")
# theRingsTemplate$ = fileAsString("ringsTmp.txt")
# theOceanTemplate$ = fileAsString("oceanTmp.txt")
# thePlanetTemplate$ = fileAsString("planetTmp.txt")
# theStarTmp$ = fileAsString("starTmp.txt")
# theWikiTemplate$ = fileAsString("wikiTemplate.html")

# '###############################
# '#Template files for integration with other mods
# DIM SHARED theResearchBodyTemplate$
# theResearchBodyTemplate$ = fileAsString("forReserachBodiesTmp.txt")

# DIM SHARED blackHole_MassKSP
# DIM SHARED blackHole_RadiusKSP
# DIM SHARED galaxy_RadiusKSP

# DIM SHARED REDgb AS INTEGER
# DIM SHARED rGREENb AS INTEGER
# DIM SHARED rgBLUE AS INTEGER

# blackHole_MassKg = 8.55E37
# blackHole_MassKSP = sol2Kerbol_kg(blackHole_MassKg)
# blackHole_RadiusKSP = 100000

galaxy_RadiusKSP = (6.62251E+17)/6
print GNAME
print CUSTOM
print SEED
print AGE
print PENABLE
print ASTTOG
print GTYPE
print OSTAR 
print BSTAR 
print ASTAR 
print FSTAR 
print GSTAR 
print KSTAR 
print MSTAR 
print LSTAR 
print DWARFSTAR 


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



print "  Reading in GalaxyGen_Info template..."
theFile=open('Data_Folder/templates/Info_template.txt','r')
theInfoTemp=theFile.read()
theFile.close


print theInfoTemp % {"GNAME":GNAME, "TBG_Version":TBG_Version, "CUSTOM":CUSTOM, "SEED":SEED, "GTYPE":GTYPE, 
    "AGE":AGE, "CLUSTERNUM":0, "PENABLE":PENABLE, "ASTTOG":ASTTOG, "LSTAR":LSTAR, "MSTAR":MSTAR, "KSTAR":KSTAR, 
    "GSTAR":GSTAR, "FSTAR":FSTAR, "ASTAR":ASTAR, "BSTAR":BSTAR, "OSTAR":OSTAR, "DWARFSTAR":DWARFSTAR}