"""
Create a 12x15' map of the Lima Bean 

Per Glen Langston's recommendations, I should:
    1. not use refs for each scan (because the pipeline doesn't use them)
    2. use "Track" to observe offs
    3. do pointing scans as normal; break up map into 2 sub-maps

Following pipeline recommendations:
https://safe.nrao.edu/wiki/bin/view/Kbandfpa/ObserverGuide?sortcol=table;up=#Reduction_Execute_Pipeline_with
"""


cat = Catalog("/users/aginsbur/GBT15B-129/gc.astrid")

Configure("/users/aginsbur/GBT15B-129/H2CO_6cm_CSetup.py")

Slew("DustRidgeCenter")
AutoPeakFocus( frequency=4829., beamName="1" )
Break("Check pointing/focus")
Configure("/users/aginsbur/GBT15B-129/H2CO_6cm_CSetup.py")

Slew("DustRidgeCenter")
Balance()

amintodeg = 1/60.
scanrate = 3. # arcmin/min

glon_length = 1800 # arcsec
glat_length = 720 # arcsec

# horizontal scans
RALongMap('DustRidgeCenter',     #center of map
    hLength = Offset("Galactic", glon_length*asectodeg, 0.0,cosv=True), 
    vLength = Offset("Galactic", 0.0, glat_length*asectodeg, cosv=True), 
    vDelta  = Offset("Galactic",0.0,1.*amintodeg,cosv=True), 
    scanDuration = 60,
    beamName="1")
