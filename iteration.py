import biSwirlFunc as bSF

#Inputs
# mdot,MR, rhoOx, rhoF,ox/f centered,swirl dir, R_i, R_o, rh_i, rh_o, rnw_i, rnw_o, w_thck, n_i, n_o, L recess, Pc

mdot = 0.22
MR = 2.8
rhoOx = 1000
rhoF = 1000
centered = 1
swirl_dir = -1
Pc = 500*6895

#Recess length [m]
Lr = 6/1000

#Distane from swirler center to inner inlet hole centerline [m]
R_i = 2.45/1000

#Inner inlet hole radius [m]
r_i_h = 1.48/2/1000

#Inner nozzle wall radius [m]
r_i_nw = 3.5/2/1000

#Distane from swirler center to outer inlet hole centerline [m]
R_o = 3.25/1000

#Outer inlet hole radius [m]
r_o_h = 0.86/2/1000

#Outer nozzle wall radius [m]
r_o_nw = 7.5/2/1000

#Wall thickness [m]
w_th = 0

#Number of inlet ports of inner swirler
n_i = 8

#Number of inlet port of outer swirler
n_o = 4

#Recess Number (RN),swirl angle (swirlAng), P outer (Po), P inner (Pi), Vel axial (Uaxial), Vel Circum (VCircum),
#Cd inner (Cdi), Cd outer (Cdo), K inner (Ki), K outer (Ko), Collision dist (Lc)

out = bSF.biSwirl(mdot,MR,rhoOx,rhoF,Pc,centered,swirl_dir,R_i,R_o,r_i_h,r_o_h,r_i_nw,r_o_nw,n_i,n_o,w_th,Lr)

print(out['RN'])