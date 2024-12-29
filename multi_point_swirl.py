import biSwirlFunc as bSF
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Inputs
# mdot,MR, rhoOx, rhoF,ox/f centered,swirl dir, R_i, R_o, rh_i, rh_o, rnw_i, rnw_o, w_thck, n_i, n_o, L recess, Pc

num_swirl = 8
mdot = 3.7/num_swirl
MR = 1.3
rhoOx = 1100
rhoF = 786
centered = 1
swirl_dir = -1
Pc = 500*6895

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
n_i = 8

#Number of inlet port of outer swirler
n_o = 8

out_mat = []
for o in range(4,n_o,1):
    out_temp = []
    for i in range(4,n_i,1):

        #print(f'{i},{o}')
        #Recess Number (RN),swirl angle (swirlAng), P outer (Po), P inner (Pi), Vel axial (Uaxial), Vel Circum (VCircum),
        #Cd inner (Cdi), Cd outer (Cdo), K inner (Ki), K outer (Ko), Collision dist (Lc)

        out = bSF.biSwirl(mdot,MR,rhoOx,rhoF,Pc,centered,swirl_dir,R_i,R_o,r_i_h,r_o_h,r_i_nw,r_o_nw,i,o,w_th,Lr)
        
        out_temp.append(out["Pi"])
        

    out_mat.append(out_temp)

out_mat = np.array(out_mat)



fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Meshing that grid
X = np.arange(4, n_i, 1)
Y = np.arange(4, n_o, 1)
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, out_mat, cmap=cm.coolwarm,linewidth=0, antialiased=False)

ax.set_xlabel('Number inner ports')
ax.set_ylabel('Number outer ports')
ax.set_zlabel('Inj Pressure')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

