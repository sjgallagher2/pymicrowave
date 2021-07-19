# Conversion library for microwave functions

import numpy as np
import cmath

def dbmToWatt(p):
	return 10**(p/10)/1000

def dbmToVolt(p, Z):
	if isinstance(Z, complex):
		# Impedance is complex
		pW = dbmToWatt(p)
		return cmath.sqrt(Z*pW);
	else:
		pW = dbmToWatt(p)
		return np.sqrt(Z*pW)

def inToCm(l):
    return l*2.54
def cmToIn(l):
    return l/2.54

# AWG to cm, in, mil
def awgToCm(ga):
    return 0.005*92**((36-ga)/39)
def awgToIn(ga):
    return 0.127*92**((36-ga)/39)
def awgToMil(ga):
	return awgToIn(ga)*1000
def cmToAwg(dia):
    return -39*cmath.log(dia/0.127,92) + 36
def inToAwg(dia):
    return -39*cmath.log(dia/0.005,92) + 36
def milToAwg(dia):
	return inToAwg(dia/1000)

# Oz of copper to thickness in mils, um
def ozCuToMil(o):
	return 1.4*o
def milToOzCu(T):
	return T/1.4
def ozCuToMicron(o):
	return 35*o
def microToOzCu(T):
	return T/35

