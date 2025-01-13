from functions import swirlFunc as S
from functions import unit as u
import math


rh = u.in2m(0.060)
rnw = u.in2m(0.20)
R = u.in2m(0.20-0.060)

mdot = 0.2
rho = 1000

n = 4

An = math.pi*rnw**2

theta, phi_n, phi_ne, U_ne, U_n, V_ma_ne, V_ma_n, Vh, r_ma_ne, r_ma_n, K, Cd = S.swirl(R,rh,rnw,rho,mdot,n,An,True)

