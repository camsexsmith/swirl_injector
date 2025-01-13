from functions import swirlFunc as S
from functions import unit as u
import math


rh = u.in2m(0.060)
rnw = u.in2m(0.250)
R = u.in2m(0.250-0.060)

mdot = 0.25
rho = 1000

n = 4

An = math.pi*rnw**2

theta, phi_n, phi_ne, U_ne, U_n, V_ma_ne, V_ma_n, Vh, r_ma_ne, r_ma_n, K, Cd = S.swirl(R,rh,rnw,rho,n,An,False)