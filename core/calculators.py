# Various calculators useful in RF/microwave
import core.material as rf_material
import core.constants as universal_constants
import numpy as np
import cmath


def gamma_from_RLGC(freq,R,L,G,C):
    """Get propagation constant gamma from RLGC transmission line parameters"""
    w=2*np.pi*freq
    return cmath.sqrt((R+1j*w*L)*(G+1j*w*C))

def Z0_from_RLGC(freq,R,L,G,C):
    """Get characteristic impedance Z0 from RLGC transmission line parameters"""
    w=2*np.pi*freq
    return cmath.sqrt( (R+1j*w*L)/(G+1j*w*C) )

def nepers_to_db(neper):
    return neper*20*np.log10(np.e)

def db_to_nepers(decibel):
    return decibel*(1/20)*np.log(10)
