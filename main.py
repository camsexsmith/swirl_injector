import numpy
import math as m

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




mdot_i = 0.5    #Mass flow rate through inner swirl [kg/s]
rho_i = 1000    #Density of inner propellant [kg/m3]


R = 0.02
rh = 0.005/2    #Inlet hole radius [m]
rnw = 0.01      #Nozzle wall radius [m]

An = m.pi*rh**2

n = 4           #Number of inlet holes

K = rnw*R/(n*rh**2)     #Geometric constant


phi_i_n = 0.2  #Initial filling coefficient guess
err = 1     #Initializing error variable

#Loop using Newtons Method for finding filling coefficient
while err > 1e-6:

    phiX = (m.sqrt(2)*(1-phi_i_n))/phi_i_n**(3/2) - K
    phiXp = -3/2*m.sqrt(2)*phi_i_n**(-5/2) + m.sqrt(2)/2*phi_i_n**(-3/2)
    phi_i_n_new = phi_i_n - phiX/phiXp

    err = abs(phi_i_n_new - phi_i_n)
    phi_i_n = phi_i_n_new


phi_i_ne = phi_i_n/(m.sqrt(3-2*phi_i_n))
print(f'Filling Coefficient in Nozzle: {round(phi_i_n,2)}')
print(f'Filling Coefficient at Nozzle Exit: {round(phi_i_n,2)}')

U_n = mdot_i/(rho_i*phi_i_n*An)       #Axial velocity in nozzle [m/s]
U_ne = mdot_i/(rho_i*phi_i_ne*An)     #Axial velocity at nozzle exit [m/s]

print(f'Center Nozzle Velocity: {round(U_n,2)} m/s')
print(f'Center Nozzle Exit Velocity: {round(U_ne,2)} m/s')

Vh = mdot_i/(rho_i*n*m.pi*rh**2)    #Circumferential velocity from inelt holes [m/s]

P = R*Vh                            #Angular momenutm of center swirl

r_ma_n = rnw*m.sqrt((2-phi_i_n)/2)    #Radius of mass averaged liquid film in nozzle [m]
r_ma_ne = rnw*m.sqrt((2-phi_i_ne)/2)  #Radius of mass averaged liquid film at nozzle exit [m]

print(f'Radius of mass avg liquid film in nozzle: {round(r_ma_n*1000,2)} mm')
print(f'Radius of mass avg liquid film at nozzle exit: {round(r_ma_ne*1000,2)} mm')

V_ma_n = P/r_ma_n                   #Circumferential velocity of liquid film in nozzle [m/s]
V_ma_ne = P/r_ma_ne                 #Circumferential velocity of liquid film at nozzle exit [m/s]

print(f'Circumferential velocity of liquid film in nozzle: {round(V_ma_n,2)} m/s')
print(f'Circumferential velocity of liquid film at nozzle exit: {round(V_ma_ne,2)} m/s')

theta_c = m.degrees(m.atan(V_ma_ne/U_ne))      #Resulting angle of center swirl sheet  [deg]

print(f'Resultant swirl angle: {round(theta_c,1)} deg')

#If RN (Recess number) > 1 impingment will occur within the swirl injector

