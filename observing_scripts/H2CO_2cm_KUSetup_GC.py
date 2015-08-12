# Ku-band H2CO 2 cm (and friends)
# keywords defined at www.gb.nrao.edu/~fghigo/gbtdoc/config/configparams_rev1.doc
#
# CONFIGURATION:
# Bandwidth Polarization Level Number of Number of Lags - Approximate Resolution
#   (MHz) Cross-Products Sampling Spectral Beams Low Medium High
# BW Pol Lev  Windows Beams Channels / resolution
# 50 No  9    4       2     4096 - 12.2070 kHz 4096 - 12.2070 kHz 4096 - 12.2070 kHz

receiver  = 'Rcvr12_18'               # select Ku-band receiver
beam      = 'B12'                     # use two beams
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
swmode    = "tp"                      # set switching scheme (tp(total power with cal), tp_nocal, sp(switched power with cal), sp_nocal )
swtype    = "none"                    # for frequency switching; not used for tp mode
swper     = 1.0                       # one second cycle for switching
swfreq    = 0.0, 0.0                  # for freq switching
tint      = 0.5                       # integration time (for 4 quadrants, 1.2-40 sec.  Important to avoid smearing)
vlow      = 0
vhigh     = 0
vframe    = "lsrk"                    # LSR - kinematic is the "normal" definition (don't use dynamic)
vdef      = "Radio"                   # radio (optical is also acceptable, but not the norm for Galactic observations)
noisecal  = "lo"
pol       = "Circular"  # should this be linear?
nchan     = "high"
vegas.vpol='self'
restfreq = [ {"restfreq": 14488.479, 'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 14511.,    'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 14465.,    'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 13778.80,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 13801.,    'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 13756.,    'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 14151.61,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 14105.61,  'bandwidth': 23.44, "res":5.7, "deltafreq": 0},
             {"restfreq": 12625.,    'bandwidth': 1250., "res":92.0, "delatfreq": 0},
           ]
