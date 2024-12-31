import biSwirlFunc as bSF
import numpy as np
import unit as u
import math as m

#Inputs
# mdot,MR, rhoOx, rhoF,ox/f centered,swirl dir, R_i, R_o, rh_i, rh_o, rnw_i, rnw_o, w_thck, n_i, n_o, L recess, Pc

num_swirl = 8
mdot = 3.7/num_swirl
MR = 1.3
rhoOx = 1100
rhoF = 786
centered = 1
swirl_dir = -1
Pc = u.psi2pa(500)

#Recess length [m]
Lr = u.in2m(0.250)

#Distane from swirler center to inner inlet hole centerline [m]
R_i = u.in2m(0.150)-u.in2m(0.025)

#Inner inlet hole radius [m]
r_i_h = u.in2m(0.025)

#Inner nozzle wall radius [m]
r_i_nw = u.in2m(0.150)

#Distane from swirler center to outer inlet hole centerline [m]
R_o = u.in2m(0.300)-u.in2m(0.050)

#Outer inlet hole radius [m]
r_o_h = u.in2m(0.050)

#Outer nozzle wall radius [m]
r_o_nw = u.in2m(0.300)

#Wall thickness [m]
w_th = u.in2m(0.080)

#Number of inlet ports of inner swirler
n_i = 6

#Number of inlet port of outer swirler
n_o = 6

#Recess Number (RN),swirl angle (swirlAng), P outer (Po), P inner (Pi), Vel axial (Uaxial), Vel Circum (VCircum),
#Cd inner (Cdi), Cd outer (Cdo), K inner (Ki), K outer (Ko), Collision dist (Lc), Fill frac inner exit (PhiNEi),
#Fill frac outer (PhiO)

out = bSF.biSwirl(mdot,MR,rhoOx,rhoF,Pc,centered,swirl_dir,R_i,R_o,r_i_h,r_o_h,r_i_nw,r_o_nw,n_i,n_o,w_th,Lr)

dP_o = out["Po"] - Pc
dP_i = out["Pi"] - Pc

phi_i_ne = out["PhiNEi"]
phi_o_n = out["PhiO"]

stiff_o = dP_o/Pc*100
stiff_i = dP_i/Pc*100

#Radius of gas core on outer swirl
r_o_gc = r_o_nw*m.sqrt(1-phi_o_n)

r_i_tot = r_i_nw + w_th

if r_o_gc < r_i_tot:
    print(f"NOT Possible: gas core {round(u.m2in(r_o_gc),3)} inner {round(u.m2in(r_i_tot),3)}")
else:
    print(f"Possible: gas core {round(u.m2in(r_o_gc),3)} inner {round(u.m2in(r_i_tot),3)}")


print('Pressures')
print(f'Outer: {round(u.pa2psi(out["Po"]),1)} psi \ Stiffness {round(stiff_o,2)}')
print(f'Inner: {round(u.pa2psi(out["Pi"]),1)} psi \ Stiffness {round(stiff_i,2)}')

print('Fill Fraction')
print(f'Outer: {round(u.pa2psi(out["Po"]),1)} psi \ Stiffness {round(stiff_o,2)}')
print(f'Inner: {round(u.pa2psi(out["Pi"]),1)} psi \ Stiffness {round(stiff_i,2)}')