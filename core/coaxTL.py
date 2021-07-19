# Coax cable data and methods
from core.material import Medium
import numpy as np
import cmath
from scipy.special import jv,yv  # Modified Bessel functions of the first and second kind

class CoaxialCable:
    def __init__(self,ID,OD,outer_thickness=70e-6,dielectric=Medium(name="Polyethylene foam"),conductor=Medium(name="Copper")):
        self.ID = ID
        self.OD = OD
        self.outer_thickness = outer_thickness
        self.dielectric = dielectric
        self.conductor = conductor
        self.R=-1
        self.G=-1
        self.L=-1
        self.C=-1

    def calculate_RLGC(self,freq):
        # Source: Qinghai Shi, Troltzsch, U., & Kanoun, O. (2011)
        #         doi:10.1109/ssd.2011.5767393
        # TODO this is broken, Bessel functions *do not* like arguments this large
        if freq <= 0:
            return (-1,-1,-1,-1)
        w=2*np.pi*freq
        eta = self.conductor.intrinsic_impedance(freq)
        gamma = cmath.sqrt(1j*w*self.conductor.conductivity*self.conductor.mu)
        a=self.ID
        b=self.OD
        c=self.OD+self.outer_thickness
        print(gamma)
        Za = eta/(2*np.pi*a)*(jv(0,gamma*a)/jv(1,gamma*a))
        Zb = eta/(2*np.pi*b)*(jv(0,gamma*b)*yv(1,gamma*c)+jv(1,gamma*c)*yv(0,gamma*b))/(jv(1,gamma*c)*yv(1,gamma*b)-jv(1,gamma*b)*yv(1,gamma*c))
        mu = self.conductor.mu
        self.R = np.real(Za+Zb)
        self.L = np.imag(Za+Zb)/w + mu/(2*np.pi)*np.arccosh(b/a)
        self.C = 2*np.pi*self.dielectric.epsilon/(np.arccosh(b/a))
        self.G = np.pi*w*(-np.imag(self.dielectric.epsilon))/np.arccosh(b/a)

        return (self.R,self.L,self.G,self.C)


