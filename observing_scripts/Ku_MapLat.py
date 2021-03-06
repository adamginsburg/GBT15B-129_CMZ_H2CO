cat = Catalog("/users/aginsbur/GBT15B-129/gc.astrid")

Configure("/users/aginsbur/GBT15B-129/H2CO_2cm_KUSetup.py")

Slew("DustRidgeCenter")
AutoPeakFocus( frequency=4829., beamName="1" )
Break("Check pointing/focus")
Configure("/users/aginsbur/GBT15B-129/H2CO_2cm_KUSetup.py")

Slew("DustRidgeCenter")
Balance()

asectodeg = 1/3600.
amintodeg = 1/60.
scanrate = 3. # arcmin/min

glon_length = 1800 # arcsec
glat_length = 720 # arcsec

# vertical scans
DecLatMap('DustRidgeCenter',     #center of map
    hLength = Offset("Galactic", glon_length*asectodeg, 0.0,cosv=True), 
    vLength = Offset("Galactic", 0.0, glat_length*asectodeg, cosv=True), 
    hDelta  = Offset("Galactic", (1./3.)*amintodeg, 0.0, cosv=True), 
    scanDuration = 60,
    beamName="1")

# TODO: add reference scans.  I think they are helpful for improving data quality.  Unclear whether they'll add too much overhead...

