# Data on various materials

import numpy as np
from core.constants import physical_constants

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


def dielectric(material):  # Dielectric constant
	return dielectric_[material]

def permittivity(material,get_complex=True):
	e0 = physical_constants["e0"]
	if not get_complex:
		epsilon = e0*dielectric(material) 
		return epsilon
	else:
		if lossTangent_[material] != 0:
			eRe = e0*dielectric_[material]
			eIm = eRe*lossTangent_[material]
			eCpl = eRe + eIm*1j
			return eCpl
	return e0

def permeability(material):
	u0 = physical_constants["mu0"]
	if permeability_[material] == 0:
		return u0
	else:
		return u0*permeability_[material]

def lossTangent(material):
	return lossTangent_[material]

def conductivity(material):
	return conductivity_[material]

