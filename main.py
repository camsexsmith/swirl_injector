import numpy
import math as m
import swirlFunc as SF

mdot = 1
MR = 1.3

mdot_ox = mdot*MR/(MR+1)
mdot_f = mdot/(MR+1)

rho_ox = 1000
rho_f = 700

centered = 1    # 1 = Ox centered : 0 = Fuel centered

if centered == 1:
    mdot_i = mdot_ox
    rho_i = rho_ox

    mdot_o = mdot_f
    rho_o = rho_f
elif centered == 0:
    mdot_i = mdot_f
    rho_i = rho_f

    mdot_o = mdot_ox
    rho_o = rho_ox

R_i = 0.0079375 
r_i_h = 0.0015875   #Inlet hole radius [m]
r_i_nw = 0.01905      #Nozzle wall radius [m]

R_o = 0.0206375
r_o_h = 0.0015875
r_o_nw = 0.022225

n = 4

A_i_n = m.pi*r_i_nw**2
A_o_n = m.pi*(r_o_nw**2 - r_i_nw**2)

print('----------------------------------------------')
print('                 Outer Swirl                  ')
print('----------------------------------------------')

SF.swirl(R_i,r_i_h,r_i_nw,rho_i,mdot_i,n,A_i_n)

print('----------------------------------------------')
print('                 Inner Swirl                  ')
print('----------------------------------------------')

SF.swirl(R_o,r_o_h,r_o_nw,rho_o,mdot_o,n,A_o_n)
