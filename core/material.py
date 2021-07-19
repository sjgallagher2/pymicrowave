# Data on various materials

import numpy as np
from core.constants import physical_constants
import cmath

# Built in materials
builtin_materials = ["A35","Aluminum","Alumina","Barium tetratitanate","Beeswax","Beryllia","Brass","Bronze" ,
    "Chromium","Copper","Fused quartz","GaAs","Germanium","Glazed ceramic","Pyrex","Lucite","Mild steel",
    "Nylon","Parafin","Plexiglass","Polyethylene","Polystyrene","Porcelain","Rexolite","Silicon",
    "Styrofoam","Teflon","Titania","Vaseline","Water","FR4","Iron","Nichrome","Nickel","Platinum",
    "Silver","Gold","StainlessSteel","Solder","Tungsten","Vacuum","Zinc"
]

# 0 = Conductor
#Relaive permittivities
dielectric_ = {"A35":5.6,"Aluminum":0,"Alumina":9.5,"Barium tetratitanate":37,"Beeswax":2.35,"Beryllia":6.4,"Brass":0,"Bronze":0 ,
    "Chromium":0,"Copper":0,"Fused quartz":3.78,"GaAs":13,"Germanium":0,"Glazed ceramic":7.2,"Pyrex":4.82,"Lucite":2.56,"Mild steel":0,
    "Nylon":2.84,"Parafin":2.24,"Plexiglass":2.6,"Polyethylene":2.25,"Polystyrene":2.54,"Porcelain":5.04,"Rexolite":2.54,"Silicon":11.9,
    "Styrofoam":1.03,"Teflon":2.08,"Titania":96,"Vaseline":2.16,"Water":76.7,"FR4":4.4,"Iron":0,"Nichrome":0,"Nickel":0,"Platinum":0,
    "Silver":0,"Gold":0,"StainlessSteel":0,"Solder":0,"Tungsten":0,"Vacuum":1,"Zinc":0}

# 0 = dielectric material (still defaults to u0)
# 1 = no relative permeability
# Relative permeabilities
permeability_ = {"A35":0,"Aluminum":1,"Alumina":0,"Barium tetratitanate":0,"Beeswax":0,"Beryllia":0,"Brass":1,"Bronze":1,
    "Chromium":1,"Copper":1,"Fused quartz":0,"GaAs":0,"Ge":1,"Glazed ceramic":0,"Pyrex":0,"Lucite":0,"Mild steel":2000,"Nylon":0,"Parafin":0,
    "Plexiglass":0,"Polyethylene":0,"Polystyrene":0,"Porcelain":0,"Rexolite":0,"Silicon":0,"Styrofoam":0,"Teflon":0,
    "Titania":0,"Vaseline":0,"Water":0,"FR4":0,"Iron":4000,"Nichrome":1,"Nickel":100,"Platinum":1,"Silver":1,"Gold":1,"Stainless steel":2,
    "Tin lead solder":1,"Tungsten":1,"Vacuum":1,"Zinc":1}

# 0 = Conductor (they have their own way of approximating complex permittivity)
#Loss tangent
lossTangent_ = {"A35":0.0041,"Aluminum":0,"Alumina":0.0003,"Barium tetratitanate":0.0005,"Beeswax":0.005,"Beryllia":0.0003,"Brass":0,"Bronze":0,
    "Chromium":0,"Copper":0,"Fused quartz":0.0001,"GaAs":0.006,"Germanium":0,"Glazed ceramic":0.008,"Pyrex":0.0054,"Lucite":0.008,"Mild steel":0,
    "Nylon":0.012,"Parafin":0.0002,"Plexiglass":0.0057,"Polyethylene":0.0004,"Polystyrene":0.00033,"Porcelain":0.0078,"Rexolite":0.00048,
    "Silicon":0.004,"Styrofoam":0.0001,"Teflon":0.0004,"Titania":0.001,"Vaseline":0.001,"Water":0.157,"FR4":0.008,"Iron":0,"Nichrome":0,
    "Nickel":0,"Platinum":0,"Silver":0,"Gold":0,"Stainless steel":0,"Tin lead solder":0,"Tungsten":0,"Vacuum":0,"Zinc":0}

# 0 = Dielectric material
#Conductivity in S/m
conductivity_ = {"A35":0,"Aluminum":3.186e7,"Alumina":0,"Barium tetratitanate":0,"Beeswax":0,"Beryllia":0,"Brass":2.564e7,"Bronze":1e7,\
    "Chromium":3.846e7,"Copper":5.813e7,"Fused quartz":0,"GaAs":0,"Germanium":2.2e6,"Glazed ceramic":0,"Pyrex":0,"Lucite":0,
    "Mild steel":1.01e7,"Nylon":0,"Parafin":0,"Plexiglass":0,"Polyethylene":0,"Polystyrene":0,"Porcelain":0,"Rexolite":0,"Silicon":0,
    "Styrofoam":0,"Teflon":0,"Titania":0,"Vaseline":0,"Water":0,"FR4":0,"Iron":1.03e7,"Nichrome":10**6,"Nickel":1.449e7,"Platinum":9.52e6,
    "Silver":6.173e7,"Gold":4.098e7,"Stainless steel":1.1e6,"Tin lead solder":7e6,"Tungsten":1.825e7,"Vacuum":0,"Zinc":1.67e7}

class Medium:
    """
    General material/media independent of frequency

    Depending on the material parameters, the permittivity (epsilon) will either be real (conductors) or complex
    (dielectrics with dielectric loss). The conductivity is not included in the permittivity by default.
    The additional term sometimes added to the imaginary component is (-2*pi*f)/sigma, for frequency f and
    conductivity sigma.

    Optional keyword parameters:
        name : string
            Name of material. If this coincides with a built-in material, properties are added automatically (but
            can be overwritten).
        rel_dielectric : number
            Dielectric constant/relative permittivity, a real number
        rel_permeability : number
            Relative permeability, a real number
        loss_tangent : number
            Loss tangent (dielectrics), a real number
        conductivity : number
            Conductivity (conductors), a real number
    """
    def __init__(self, **kwargs):
        # Handle input parameters
        if 'name' in kwargs.keys():
            self.name = kwargs['name']
            if self.name in builtin_materials:
                self.rel_dielectric = dielectric_[self.name]
                self.rel_permeability = permeability_[self.name]
                self.loss_tangent = lossTangent_[self.name]
                self.conductivity = conductivity_[self.name]
        else:
            self.name = "unnamed medium"
        if 'rel_dielectric' in kwargs.keys():
            self.rel_dielectric = kwargs['rel_dielectric']
        else:
            self.rel_dielectric = 1.0
        if 'rel_permeability' in kwargs.keys():
            self.rel_permeability = kwargs['rel_permeability']
        else:
            self.rel_permeability = 1.0
        if 'loss_tangent' in kwargs.keys():
            self.loss_tangent = kwargs['loss_tangent']
        else:
            self.loss_tangent = 0
        if 'conductivity' in kwargs.keys():
            self.conductivity = kwargs['conductivity']
        else:
            self.conductivity = 0

        self.epsilon = physical_constants["e0"]*self.rel_dielectric
        self.mu = physical_constants["mu0"]*self.rel_permeability

    def complex_permittivity(self,freq=0,include_conductivity=False):
        """Return complex (lossy) permittivity for phasor calculations. If include_conductivity,
        the imaginary part becomes (-2*pi*freq)/sigma for conductivity sigma."""
        if freq == 0:
            return self.epsilon
        elif freq > 0:
            w=2*np.pi*freq
            if include_conductivity:
                return self.epsilon*(1 + 1j * (self.loss_tangent+w/self.conductivity))
            else:
                return self.epsilon*(1 + 1j * (self.loss_tangent))
    def skin_depth(self,freq):
        """Return skin depth in meters"""
        sigma = self.conductivity
        delta_s = cmath.sqrt(2/(2*np.pi*freq*self.mu*sigma))
        return delta_s

    def surface_resistance(self,freq):
        """Return surface resistance in ohms"""
        sigma = self.conductivity
        Rs = cmath.sqrt(2*np.pi*freq*self.mu/(2*sigma))
        return Rs

    def phase_velocity(self):
        """Return phase velocity in material, in m/s"""
        return 1/np.sqrt(self.mu*self.epsilon)

    def wavelength(self,freq):
        """Return wavelength in material, in meters"""
        return self.phase_velocity()/freq

    def propagation_constant(self,freq):
        """Return complex propagation constant at a given frequency in the medium"""
        sigma = self.conductivity
        w = 2*np.pi*freq
        gamma = w*1j*cmath.sqrt(self.mu*self.epsilon)*cmath.sqrt(1-1j*sigma/(w*self.epsilon))
        return gamma

    def attenuation_constant(self,freq):
        """Return attenuation constant in nepers/m"""
        return np.real(self.propagation_constant(freq))

    def phase_constant(self,freq):
        """Return phase constant"""
        return np.imag(self.propagation_constant(freq))

    def intrinsic_impedance(self,freq):
        """Return intrinsic impedance in material, in ohms"""
        if freq == 0:
            return cmath.sqrt(self.mu/self.eps)
        else:
            gamma = self.propagation_constant(freq)
            w = 2*np.pi*freq
            return 1j*w*self.mu/gamma
