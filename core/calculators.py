# Various calculators useful in RF/microwave
import core.material as rf_material
import core.constants as universal_constants
import numpy as np
import cmath

# TODO Convert material parameters to objects

def skin_depth(freq,material="Vacuum"):
    """Return skin depth in meters"""
    mu = rf_material.permeability(material)
    sigma = rf_material.conductivity(material)
    delta_s = cmath.sqrt(2/(2*np.pi*freq*mu*sigma))
    return delta_s

def surface_resistance(freq,material="Vacuum"):
    """Return surface resistance in ohms"""
    mu = rf_material.permeability(material)
    sigma = rf_material.conductivity(material)
    Rs = cmath.sqrt(2*np.pi*freq*mu/(2*sigma))
    return Rs

def phase_velocity(material="Vacuum"):
    """Return phase velocity in material, in m/s"""
    mu = rf_material.permeability(material)
    eps = rf_material.permittivity(material,get_complex=False)
    return 1/np.sqrt(mu*eps)

def wavelength(freq,material="Vacuum"):
    """Return wavelength in material, in meters"""
    return phase_velocity(material)/freq


def propagation_constant(freq,material="Vacuum"):
    """Return complex propagation constant at a given frequency in the medium"""
    mu = rf_material.permeability(material)
    eps = rf_material.permittivity(material)
    sigma = rf_material.conductivity(material)
    w = 2*np.pi*freq
    gamma = w*1j*cmath.sqrt(mu*eps)*cmath.sqrt(1-1j*sigma/(w*eps))
    return gamma

def attenuation_constant(freq,material="Vacuum"):
    """Return attenuation constant in nepers/m"""
    return np.real(propagation_constant(freq,material))

def phase_constant(freq,material="Vacuum"):
    """Return phase constant"""
    return np.imag(propagation_constant(freq,material))

def intrinsic_impedance(freq=0,material="Vacuum"):
    """Return intrinsic impedance in material, in ohms"""
    mu = rf_material.permeability(material)
    eps = rf_material.permittivity(material)
    if freq == 0:
        return cmath.sqrt(mu/eps)
    else:
        gamma = propagation_constant(freq,material)
        w = 2*np.pi*freq 
        return 1j*w*mu/gamma 
        
def gamma_from_RLGC(freq,R,L,G,C):
    """Get propagation constant gamma from RLGC transmission line parameters"""
    w=2*np.pi*freq
    return cmath.sqrt((R+1j*w*L)*(G+1j*w*C))

def Z0_from_RLGC(freq,R,L,G,C):
    """Get characteristic impedance Z0 from RLGC transmission line parameters"""
    w=2*np.pi*freq
    return cmath.sqrt( (R+1j*w*L)/(G+1j*w*C) )


