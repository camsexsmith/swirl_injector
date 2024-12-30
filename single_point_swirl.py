import biSwirlFunc as bSF
import numpy as np
import unit as u

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
Lr = 0.00635

#Distane from swirler center to inner inlet hole centerline [m]
R_i = 0.00381-0.000635

#Inner inlet hole radius [m]
r_i_h = 0.000635

#Inner nozzle wall radius [m]
r_i_nw = 0.00381

#Distane from swirler center to outer inlet hole centerline [m]
R_o = 0.00762-0.00127

#Outer inlet hole radius [m]
r_o_h = 0.00127

#Outer nozzle wall radius [m]
r_o_nw = 0.00762

#Wall thickness [m]
w_th = 0.00254

#Number of inlet ports of inner swirler
n_i = 6

#Number of inlet port of outer swirler
n_o = 6

#Recess Number (RN),swirl angle (swirlAng), P outer (Po), P inner (Pi), Vel axial (Uaxial), Vel Circum (VCircum),
#Cd inner (Cdi), Cd outer (Cdo), K inner (Ki), K outer (Ko), Collision dist (Lc)

out = bSF.biSwirl(mdot,MR,rhoOx,rhoF,Pc,centered,swirl_dir,R_i,R_o,r_i_h,r_o_h,r_i_nw,r_o_nw,n_i,n_o,w_th,Lr)

dP_o = out["Po"] - Pc
dP_i = out["Pi"] - Pc

stiff_o = dP_o/Pc*100
stiff_i = dP_i/Pc*100

print('Pressures')
print(f'Outer Inj Pressure: {round(u.pa2psi(out["Po"]),1)} psi \ Stiffness {round(stiff_o,2)}')
print(f'Inner Inj Pressure: {round(u.pa2psi(out["Pi"]),1)} psi \ Stiffness {round(stiff_i,2)}')