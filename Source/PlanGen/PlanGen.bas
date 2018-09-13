OPEN "planet.cfg" FOR OUTPUT AS #1

RANDOMIZE TIMER
SEED = INT(RND * 1000)

'PLANETTYPE = INT(RND * 2)

RANDOMIZE SEED
'COLOR Settings. 0 = Greyscale, 1 = Yellow, 2 = Blue, 3 = Green, 4 = Red, 5 = White, 6 = Purple,
PRINT SEED
COLORS = INT(RND * 6)
PRINT COLORS
'PLANETTYPE = 1
'SELECT CASE PLANETTYPE
'CASE 0
IF COLORS = 0 THEN
    COLOR0$ = "0.8, 0.8, 0.8,1"
    COLOR1$ = "0.7, 0.7, 0.7,1"
    COLOR2$ = "0.6, 0.6, 0.6,1"
    COLOR3$ = "0.5, 0.5, 0.5,1"
    COLOR4$ = "0.4, 0.4, 0.4,1"
    MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/greycolor.png"
ELSE
    IF COLORS = 1 THEN
        COLOR0$ = "0.8, 0.8, 0.5,8"
        COLOR1$ = "0.7, 0.7, 0.4,7"
        COLOR2$ = "0.6, 0.6, 0.3,6"
        COLOR3$ = "0.5, 0.5, 0,2"
        COLOR4$ = "0.4, 0.4, 0.1,4"
        MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/yellowcolor.png"
    ELSE
        IF COLORS = 2 THEN
            COLOR0$ = "0.5, 0.5, 0.8,1"
            COLOR1$ = "0.4, 0.4, 0.7,1"
            COLOR2$ = "0.3, 0.3, 0.6,1"
            COLOR3$ = "0.2, 0.2, 0.5,1"
            COLOR4$ = "0.1, 0.1, 0.4,1"
            MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/bluecolor.png"
        ELSE
            IF COLORS = 3 THEN
                COLOR0$ = "0.5, 0.8, 0,1"
                COLOR1$ = "0.4, 0.7, 0,1"
                COLOR2$ = "0.3, 0.6, 0,1"
                COLOR3$ = "0.2, 0.5, 0,1"
                COLOR4$ = "0.1, 0.4, 0,1"
                MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/greencolor.png"
            ELSE
                IF COLORS = 4 THEN
                    COLOR0$ = "0.8, 0.5, 0,1"
                    COLOR1$ = "0.7, 0.4, 0,1"
                    COLOR2$ = "0.6, 0.3, 0,1"
                    COLOR3$ = "0.5, 0.2, 0,1"
                    COLOR4$ = "0.4, 0.1, 0,1"
                    MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/redcolor.png"
                ELSE
                    IF COLORS = 5 THEN
                        COLOR0$ = "0.2, 0.2, 0.2,1"
                        COLOR1$ = "0.6, 0.6, 0.6,1"
                        COLOR2$ = "0.9, 0.9, 0.9,1"
                        COLOR3$ = "1, 1, 1, 1"
                        COLOR4$ = "1, 1, 1, 1"
                        MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/whitecolor.png"
                    ELSE
                        IF COLORS = 6 THEN
                            COLOR0$ = "0.8, 0.5, 0.8,1"
                            COLOR1$ = "0.7, 0.4, 0.7,1"
                            COLOR2$ = "0.6, 0.3, 0.6,1"
                            COLOR3$ = "0.5, 0.2, 0.5,1"
                            COLOR4$ = "0.4, 0.1, 0.4,1"
                            MAPCOLOR$ = "To_Boldly_Go/solidplanettextures/purplecolor.png"
                        END IF
                    END IF
                END IF
            END IF
        END IF
    END IF
END IF

ALT = RND
PRINT ALT

SIZE = RND * 4 + 1
PRINT SIZE

PRINT #1, "@Kopernicus"
PRINT #1, "{"
PRINT #1, "    Body"
PRINT #1, "    {"
PRINT #1, "        name = INSERTNAMEHERE"
PRINT #1, "        Template"
PRINT #1, "        {"
PRINT #1, "            name = Mun"
PRINT #1, "            removePQSMods = VertexColorMap, VoronoiCraters, VertexHeightMap,"
PRINT #1, "        }"
PRINT #1, "        Properties"
PRINT #1, "        {"
PRINT #1, "            rotationPeriod ="; INT(RND * 100000)
PRINT #1, "            tidallyLocked = False"
PRINT #1, "            radius ="; 100000 * SIZE
PRINT #1, "            geeASL ="; 0.10 * SIZE
PRINT #1, "            description ="
PRINT #1, "            sphereOfInfluence ="; 2429559.1 * SIZE
PRINT #1, "        }"
PRINT #1, "        ScaledVersion"
PRINT #1, "        {"
PRINT #1, "            Material"
PRINT #1, "            {"
PRINT #1, "              texture ="; MAPCOLOR$
PRINT #1, "              normals = To_Boldly_Go/solidplanettextures/greycolor.png"
PRINT #1, "            }"
PRINT #1, "        }"
PRINT #1, "        Orbit"
PRINT #1, "        {"
PRINT #1, "            referenceBody = Kerbin"
PRINT #1, "            semiMajorAxis ="; INT(RND * 40000000) + 20000000
PRINT #1, "            eccentricity = 0"
PRINT #1, "            color ="; COLOR0$
PRINT #1, "        }"
PRINT #1, "        PQS"
PRINT #1, "        {"
PRINT #1, "            Material"
PRINT #1, "            {"
PRINT #1, "                fogColorRamp = BUILTIN/desert_atmogradient"
PRINT #1, "                steepTex = BUILTIN/lunar cliff face"
PRINT #1, "                steepBumpMap = BUILTIN/Cliff (Layered Rock)_NRM"
PRINT #1, "                lowTex = BUILTIN / RockyGround"
PRINT #1, "                midTex = BUILTIN / RockyGround"
PRINT #1, "                midBumpMap = BUILTIN / RockyGround2"
PRINT #1, "                highTex = BUILTIN / RockyGround"
PRINT #1, "            }"
PRINT #1, "            Mods"
PRINT #1, "            {"
PRINT #1, "                //VertexHeightMap"
PRINT #1, "                //{"
PRINT #1, "                //  map = To_Boldly_Go/"
PRINT #1, "                //  deformity = 10700"
PRINT #1, "                //}"
PRINT #1, "                VoronoiCraters"
PRINT #1, "                {"
PRINT #1, "                    name = 1"
PRINT #1, "                    colorOpacity = 1"
PRINT #1, "                    DebugColorMapping = False"
PRINT #1, "                    deformation ="; 200 * ALT
PRINT #1, "                    jitter = 0.1"
PRINT #1, "                    jitterHeight = 2"
PRINT #1, "                    rFactor = 1"
PRINT #1, "                    rOffset = 1.1"
PRINT #1, "                    simplexFrequency = 300"
PRINT #1, "                    simplexOctaves = 3"
PRINT #1, "                    simplexPersistence = 0.5"
PRINT #1, "                    simplexSeed = 123123"
PRINT #1, "                    voronoiDisplacement = 0"
PRINT #1, "                    voronoiFrequency = 50"
PRINT #1, "                    voronoiSeed = "; INT(RND * 1000)
PRINT #1, "                    order = 100"
PRINT #1, "                    enabled = True"
PRINT #1, "                    CraterCurve"
PRINT #1, "                    {"
PRINT #1, "                        key = -0.9982381 -0.741178 -0.4099868 -0.4099868"
PRINT #1, "                        key = -0.9332262 -0.767832 3.078513 3.078513"
PRINT #1, "                        key = -0.8990405 -0.543334 11.04789 11.04789"
PRINT #1, "                        key = -0.7445966 1.854991 6.299723 6.299723"
PRINT #1, "                        key = -0.4015177 0.85 -4.159815 -4.159815"
PRINT #1, "                        key = -0.2297457 0.4 -1.548222 -1.548222"
PRINT #1, "                        key = 0.2724952 0.004238 -0.3350353 -0.3350353"
PRINT #1, "                        key = 0.9998434 0.004091 -0.000202104 -0.000202104"
PRINT #1, "                    }"
PRINT #1, "                }"
PRINT #1, "                VoronoiCraters"
PRINT #1, "                {"
PRINT #1, "                    name = 2"
PRINT #1, "                    colorOpacity = 1"
PRINT #1, "                    DebugColorMapping = False"
PRINT #1, "                    deformation = "; 500 * ALT
PRINT #1, "                    jitter = 0.1"
PRINT #1, "                    jitterHeight = 3"
PRINT #1, "                    rFactor = 1"
PRINT #1, "                    rOffset = 1"
PRINT #1, "                    simplexFrequency = 120"
PRINT #1, "                    simplexOctaves = 3"
PRINT #1, "                    simplexPersistence = 0.5"
PRINT #1, "                    simplexSeed = 123123"
PRINT #1, "                    voronoiDisplacement = 0"
PRINT #1, "                    voronoiFrequency = 22"
PRINT #1, "                    voronoiSeed = "; INT(RND * 1000)
PRINT #1, "                    order = 101"
PRINT #1, "                    enabled = True"
PRINT #1, "                    CraterCurve"
PRINT #1, "                    {"
PRINT #1, "                        key = -0.9982381 -0.741178 -0.4099868 -0.4099868"
PRINT #1, "                        key = -0.9332262 -0.767832 3.078513 3.078513"
PRINT #1, "                        key = -0.8990405 -0.543334 11.04789 11.04789"
PRINT #1, "                        key = -0.7445966 1.854991 6.299723 6.299723"
PRINT #1, "                        key = -0.4015177 0.85 -4.159815 -4.159815"
PRINT #1, "                        key = -0.2297457 0.4 -1.548222 -1.548222"
PRINT #1, "                        key = 0.2724952 0.004238 -0.3350353 -0.3350353"
PRINT #1, "                        key = 0.9998434 0.004091 -0.000202104 -0.000202104"
PRINT #1, "                    }"
PRINT #1, "                }"
PRINT #1, "                VoronoiCraters"
PRINT #1, "                {"
PRINT #1, "                    name = 3"
PRINT #1, "                    colorOpacity = 1"
PRINT #1, "                    DebugColorMapping = False"
PRINT #1, "                    deformation = "; 720 * ALT
PRINT #1, "                    jitter = 0.1"
PRINT #1, "                    jitterHeight = 3"
PRINT #1, "                    rFactor = 1"
PRINT #1, "                    rOffset = 1"
PRINT #1, "                    simplexFrequency = 120"
PRINT #1, "                    simplexOctaves = 3"
PRINT #1, "                    simplexPersistence = 0.5"
PRINT #1, "                    simplexSeed = 123123"
PRINT #1, "                    voronoiDisplacement = 0"
PRINT #1, "                    voronoiFrequency = 10"
PRINT #1, "                    voronoiSeed = "; INT(RND * 1000)
PRINT #1, "                    order = 102"
PRINT #1, "                    enabled = True"
PRINT #1, "                    CraterCurve"
PRINT #1, "                    {"
PRINT #1, "                        key = -0.9982381 -0.741178 -0.4099868 -0.4099868"
PRINT #1, "                        key = -0.9332262 -0.767832 3.078513 3.078513"
PRINT #1, "                        key = -0.8990405 -0.543334 11.04789 11.04789"
PRINT #1, "                        key = -0.7445966 1.854991 6.299723 6.299723"
PRINT #1, "                        key = -0.4015177 0.85 -4.159815 -4.159815"
PRINT #1, "                        key = -0.2297457 0.4 -1.548222 -1.548222"
PRINT #1, "                        key = 0.2724952 0.004238 -0.3350353 -0.3350353"
PRINT #1, "                        key = 0.9998434 0.004091 -0.000202104 -0.000202104"
PRINT #1, "                    }"
PRINT #1, "                }"
PRINT #1, "                VoronoiCraters"
PRINT #1, "                {"
PRINT #1, "                    name = 4"
PRINT #1, "                    colorOpacity = 1"
PRINT #1, "                    DebugColorMapping = False"
PRINT #1, "                    deformation = "; 970 * ALT
PRINT #1, "                    jitter = 0.1"
PRINT #1, "                    jitterHeight = 3"
PRINT #1, "                   rFactor = 1"
PRINT #1, "                    rOffset = 1"
PRINT #1, "                    simplexFrequency = 120"
PRINT #1, "                    simplexOctaves = 3"
PRINT #1, "                    simplexPersistence = 0.5"
PRINT #1, "                    simplexSeed = 123123"
PRINT #1, "                    voronoiDisplacement = 0"
PRINT #1, "                    voronoiFrequency = 7"
PRINT #1, "                    voronoiSeed = "; INT(RND * 1000)
PRINT #1, "                    order = 103"
PRINT #1, "                    enabled = True"
PRINT #1, "                    CraterCurve"
PRINT #1, "                    {"
PRINT #1, "                        key = -0.9982381 -0.741178 -0.4099868 -0.4099868"
PRINT #1, "                        key = -0.9332262 -0.767832 3.078513 3.078513"
PRINT #1, "                        key = -0.8990405 -0.543334 11.04789 11.04789"
PRINT #1, "                        key = -0.7445966 1.854991 6.299723 6.299723"
PRINT #1, "                        key = -0.4015177 0.85 -4.159815 -4.159815"
PRINT #1, "                        key = -0.2297457 0.4 -1.548222 -1.548222"
PRINT #1, "                        key = 0.2724952 0.004238 -0.3350353 -0.3350353"
PRINT #1, "                        key = 0.9998434 0.004091 -0.000202104 -0.000202104"
PRINT #1, "                    }"
PRINT #1, "                }"
PRINT #1, "                HeightColorMap"
PRINT #1, "                {"
PRINT #1, "                    blend = 0.75"
PRINT #1, "                    order = 999999"
PRINT #1, "                    enabled = True"
PRINT #1, "                    LandClasses"
PRINT #1, "                    {"
PRINT #1, "                        Class"
PRINT #1, "                        {"
PRINT #1, "                            name = Lvl1"
PRINT #1, "                            color = "; COLOR0$
PRINT #1, "                            altitudeStart = 0"
PRINT #1, "                            altitudeEnd = 0.25"
PRINT #1, "                            lerpToNext = True"
PRINT #1, "                            delete = False"
PRINT #1, "                        }"
PRINT #1, "                        Class"
PRINT #1, "                        {"
PRINT #1, "                            name = Lvl2"
PRINT #1, "                            color = "; COLOR1$
PRINT #1, "                            altitudeStart = 0.25"
PRINT #1, "                            altitudeEnd = 0.3"
PRINT #1, "                            lerpToNext = True"
PRINT #1, "                            delete = False"
PRINT #1, "                        }"
PRINT #1, "                        Class"
PRINT #1, "                        {"
PRINT #1, "                            name = Lvl3"
PRINT #1, "                            color = "; COLOR2$
PRINT #1, "                            altitudeStart = 0.3"
PRINT #1, "                            altitudeEnd = 0.4"
PRINT #1, "                            lerpToNext = True"
PRINT #1, "                            delete = False"
PRINT #1, "                        }"
PRINT #1, "                        Class"
PRINT #1, "                        {"
PRINT #1, "                            name = Lvl4"
PRINT #1, "                            color = "; COLOR3$
PRINT #1, "                            altitudeStart = 0.4"
PRINT #1, "                            altitudeEnd = 0.5"
PRINT #1, "                            lerpToNext = True"
PRINT #1, "                            delete = False"
PRINT #1, "                        }"
PRINT #1, "                        Class"
PRINT #1, "                        {"
PRINT #1, "                            name = Lvl5"
PRINT #1, "                            color = "; COLOR4$
PRINT #1, "                            altitudeStart = 0.5"
PRINT #1, "                            altitudeEnd = 0.65"
PRINT #1, "                            lerpToNext = True"
PRINT #1, "                            delete = False"
PRINT #1, "                        }"
PRINT #1, "                        Class"
PRINT #1, "                        {"
PRINT #1, "                            name = Lvl6"
PRINT #1, "                            color = "; COLOR4$
PRINT #1, "                            altitudeStart = 0.65"
PRINT #1, "                            altitudeEnd = 2"
PRINT #1, "                            lerpToNext = False"
PRINT #1, "                            delete = False"
PRINT #1, "                        }"
PRINT #1, "                    }"
PRINT #1, "                }"
PRINT #1, "            }"
PRINT #1, "        }"
PRINT #1, "    }"
PRINT #1, "}"
'CASE 1

'ALT = RND
'PRINT ALT

'SIZE = RND * 4
'PRINT SIZE

'PRINT #1, "@Kopernicus"
'PRINT #1, "{"
'PRINT #1, "    Body"
'PRINT #1, "    {"
'PRINT #1, "        name = 1"
'PRINT #1, "        Template"
'PRINT #1, "        {"
'PRINT #1, "            name = Laythe"
'PRINT #1, "            removePQSMods = VertexHeightNoise, VertexSimplexHeightMap, VertexHeightMap, City,//LandControl,"
'PRINT #1, "        }"
'PRINT #1, "        Properties"
'PRINT #1, "        {"
'PRINT #1, "            rotationPeriod ="; INT(RND * 100000)
'PRINT #1, "            tidallyLocked = False"
'PRINT #1, "            radius ="; 600000 * SIZE
'PRINT #1, "            geeASL ="; 1 * SIZE
'PRINT #1, "            description ="
'PRINT #1, "            sphereOfInfluence ="; 3723645.3 * SIZE
'PRINT #1, "        }"
'PRINT #1, "        ScaledVersion"
'PRINT #1, "        {"
'PRINT #1, "            Material"
'PRINT #1, "            {"
'PRINT #1, "              texture = To_Boldly_Go/solidplanettextures/Ocean.png"
'PRINT #1, "            //  normals = To_Boldly_Go/"
'PRINT #1, "            }"
'PRINT #1, "        }"
'PRINT #1, "        Orbit"
'PRINT #1, "        {"
'PRINT #1, "            referenceBody = Kerbin"
'PRINT #1, "            semiMajorAxis ="; INT(RND * 40000000) + 20000000
'PRINT #1, "            eccentricity = 0"
'PRINT #1, "            color ="; COLOR0$
'PRINT #1, "        }"
'PRINT #1, "        PQS"
'PRINT #1, "        {"
'PRINT #1, "            Mods"
'PRINT #1, "            {"
'PRINT #1, "                //VertexHeightMap"
'PRINT #1, "                //{"
'PRINT #1, "                //  map = To_Boldly_Go/"
'PRINT #1, "                //  deformity = 10700"
'PRINT #1, "                //}"
'PRINT #1, "                Material"
'PRINT #1, "                {"
'PRINT #1, "                    steepTex = BUILTIN/SandyGround"
'PRINT #1, "                    steepBumpMap = BUILTIN/cloud_normal"
'PRINT #1, "                    steepNearTiling = 1000"
'PRINT #1, "                    lowTex = BUILTIN/SandyGround"
'PRINT #1, "                    midTex = BUILTIN/RockyGround"
'PRINT #1, "                    midBumpMap = BUILTIN/cloud_normal"
'PRINT #1, "                    highTex = BUILTIN/snow"
'PRINT #1, "                }"
'PRINT #1, "                VertexHeightNoise"
'PRINT #1, "                {"
'PRINT #1, "                    deformity ="; 10000 * ALT
'PRINT #1, "                    frequency ="; INT(RND * 20 + 5)
'PRINT #1, "                    octaves = 0"
'PRINT #1, "                    persistence = 0"
'PRINT #1, "                    seed ="; INT(RND * 1000)
'PRINT #1, "                    noiseType = Perlin"
'PRINT #1, "                    mode = Low"
'PRINT #1, "                    lacunarity = 0"
'PRINT #1, "                    order = 100"
'PRINT #1, "                    enabled = True"
'PRINT #1, "                    name = PQSMod_VertexHeightNoise"
'PRINT #1, "                    index = 0"
''PRINT #1, "                }"
'PRINT #1, "            }"
'PRINT #1, "        }"
'PRINT #1, "    }"
'PRINT #1, "}"

'CASE 2
'END SELECT
CLOSE #1
