from functions import biSwirlFunc as bSF
import numpy as np
import functions.unit as u
import math as m
import json

#Inputs
# mdot,MR, rhoOx, rhoF,ox/f centered,swirl dir, R_i, R_o, rh_i, rh_o, rnw_i, rnw_o, w_thck, n_i, n_o, L recess, Pc

num_swirl = 8
mdot = 4.25/num_swirl
MR = 1.1
rhoOx = 1100
rhoF = 786
centered = 1
swirl_dir = 1     # 1 = co-swirl and -1 = counter swirler
Pc = u.psi2pa(500)

#Recess length [m]
Lr = u.in2m(0.250)

#Distane from swirler center to inner inlet hole centerline [m]
R_i = u.in2m(0.150)-u.in2m(0.025)

#Inner inlet hole radius [m]
r_i_h = u.in2m(0.03)

#Inner nozzle wall radius [m]
r_i_nw = u.in2m(0.150)

#Distane from swirler center to outer inlet hole centerline [m]
R_o = u.in2m(0.300)-u.in2m(0.050)

#Outer inlet hole radius [m]
r_o_h = u.in2m(0.05)

#Outer nozzle wall radius [m]
r_o_nw = u.in2m(0.300)

#Wall thickness [m]
w_th = u.in2m(0.080)

#Number of inlet ports of inner swirler
n_i = 6

#Number of inlet port of outer swirler
n_o = 6

#Recess Number (RN),swirl angle (swirlAng), P outer (Po), P inner (Pi), P outer hot (Po_h), P inner hot (Pi_h), Vel axial (Uaxial), Vel Circum (VCircum),
#Cd inner (Cdi), Cd outer (Cdo), Cd inner hot (Cdi_h), Cd outer hot (Cdo_h), K inner (Ki), K outer (Ko), Collision dist (Lc), Fill frac inner exit (PhiNEi),
#Fill frac outer (PhiO)

out = bSF.biSwirl(mdot,MR,rhoOx,rhoF,Pc,centered,swirl_dir,R_i,R_o,r_i_h,r_o_h,r_i_nw,r_o_nw,n_i,n_o,w_th,Lr)

K_i = out["Ki"]
K_o = out["Ko"]

cd_o = out["Cdo"]
cd_i = out["Cdi"]

cd_o_h = out["Cdo_h"]
cd_i_h = out["Cdi_h"]

dP_o = out["Po"] - Pc
dP_i = out["Pi"] - Pc

dP_o_h = out["Po_h"] - Pc
dP_i_h = out["Pi_h"] - Pc

RN = out["RN"]
swirl_ang = out["swirlAng"]

phi_i_ne = out["PhiNEi"]
phi_o_n = out["PhiO"]

stiff_o = dP_o/Pc*100
stiff_i = dP_i/Pc*100

stiff_o_h = dP_o_h/Pc*100
stiff_i_h = dP_i_h/Pc*100

#Radius of gas core on outer swirl
r_o_gc = r_o_nw*m.sqrt(1-phi_o_n)
r_i_gc = r_i_nw*m.sqrt(1-phi_i_ne)

r_i_tot = r_i_nw + w_th

print('-----------------------------')
if r_o_gc < r_i_tot:
    print(f"NOT Possible: gas core {round(u.m2in(r_o_gc),3)} inner {round(u.m2in(r_i_tot),3)}")
else:
    print(f"Possible: gas core {round(u.m2in(r_o_gc),3)} inner {round(u.m2in(r_i_tot),3)}")
print('-----------------------------')
print('Pressures (Cold Flow)')
print(f'Outer: {round(u.pa2psi(out["Po"]),1)} psi \ Stiffness {round(stiff_o,2)}')
print(f'Inner: {round(u.pa2psi(out["Pi"]),1)} psi \ Stiffness {round(stiff_i,2)}')
print('Pressures (Hot Fire)')
print(f'Outer: {round(u.pa2psi(out["Po_h"]),1)} psi \ Stiffness {round(stiff_o_h,2)}')
print(f'Inner: {round(u.pa2psi(out["Pi_h"]),1)} psi \ Stiffness {round(stiff_i_h,2)}')
print('-----------------------------')
print('Fill Fractions')
print(f'Outer: {round(phi_o_n,2)} \ gas core radius {round(u.m2in(r_o_gc),3)} in')
print(f'Inner: {round(phi_i_ne,2)} \ gas core radius {round(u.m2in(r_i_gc),3)} in')
print('-----------------------------')
print('Swirls')
print(f'RN: {round(RN,2)}')
print(f'Angle: {round(swirl_ang,2)}')
print('-----------------------------')
print('Flow Rates')
print(f'Total flow {round(mdot*num_swirl,1)} kg/s')
print(f'Flow per swirl {round(mdot,3)} kg/s')
print(f'    Ox flow {round(mdot*MR/(1+MR),3)} kg/s')
print(f'    Fuel flow {round(mdot/(1+MR),3)} kg/s')
print('-----------------------------')

#Geometric output
dimen = {"INNER":{"Nozzle diameter (in)": u.m2in(r_i_nw*2),
                  "Port diameter (in)": u.m2in(r_i_h*2),
                  "Port number": n_i,
                  "Recess length (in)": u.m2in(Lr),
                  "Wall thickness (in)": u.m2in(w_th)},
         "OUTER":{"Nozzle diameter (in)":u.m2in(r_o_nw*2),
                  "Port diameter (in)": u.m2in(r_o_h*2),
                  "Port number": n_o}}

swirl = {"PRESSURE":
         {
        "Outer":{
            "Inj Pressure (psi)": round(u.pa2psi(out["Po"]),1),
            "Stiffness (%)": round(stiff_o,2)
            },
        "Inner":{
            "Inj Pressure (psi)": round(u.pa2psi(out["Pi"]),1),
            "Stiffness (%)": round(stiff_i,2)}
        },
        "FILL FRACTIONS":
        {
        "Outer":{
            "Fill Frac": round(phi_o_n,2)},
        "Inner":{
            "Fill Frac": round(phi_i_ne,2)}
        },
        "FLOW RATES":
        {
        "Outer":{
            "Per swirl (kg/s)": round(mdot/(1+MR),3),},
        "Inner":{
            "Per swirl (kg/s)": round(mdot*MR/(1+MR),3)}
        },
        "SWIRL":
        {
            "Recess Number": round(RN,2),
            "Swirl angle (deg)":round(u.rad2deg(swirl_ang),1),

            "Outer":{
                "Geometric const": round(K_o,2)
            },
            "Inner":{
                "Geometric const": round(K_i,2)
            }
        }
}

with open("swirl_dimensions.json", "w") as dimenout: 
    json.dump(dimen, dimenout, indent=4)

with open("swirl_performance.json", "w") as swirlout: 
    json.dump(swirl, swirlout, indent=4)