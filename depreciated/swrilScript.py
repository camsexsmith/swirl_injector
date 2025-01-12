import math as m
import functions.swirlFunc as SF

#Total mass flow rate through swirl [kg/s]
mdot = 0.22

#Chamber pressure [Pa]
Pc = 500*6895

#Mixture ratio
MR = 2.8

#Mass flow rate of oxidizer [kg/s]
mdot_ox = mdot*MR/(MR+1)

#Mass flow rate of fuel [kg/s]
mdot_f = mdot/(MR+1)

#Density of oxidizer [kg/m3]
rho_ox = 1000

#Density of fuel [kg/m3]
rho_f = 1000

# 1 = Ox centered : 0 = Fuel centered
centered = 1

#Dictates whether co-swirler (same direction) or counter-swirler (opposite direction)
# Outer is held constant positive, inner can change direction
# 1 = co-swirl and -1 = counter swirler
swirl_dir = -1

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
n_i = 4

#Number of inlet port of outer swirler
n_o = 12

#Cross sectional area of inner swirler [m2]
A_i_n = m.pi*r_i_nw**2

#Cross sectional area of outer swirler [m2]
A_o_n = m.pi*(r_o_nw**2 - (r_i_nw+w_th)**2)

print('----------------------------------------------')
print('                 Inner Swirl                  ')
print('----------------------------------------------')

theta_i, phi_i_n, phi_i_ne, U_i_ne, U_i_n, V_i_ma_ine, V_i_ma_in, V_i_h, r_i_ma_ine, r_o_ma_in, K_i, Cd_i = SF.swirl(R_i,r_i_h,r_i_nw,rho_i,mdot_i,n_i,A_i_n)

print('----------------------------------------------')
print('                 Outer Swirl                  ')
print('----------------------------------------------')

theta_o, phi_o_n, phi_o_ne, U_o_ne, U_o_n, V_o_ma_one, V_o_ma_on, V_o_h, r_o_ma_one, r_o_ma_on, K_o, Cd_o = SF.swirl(R_o,r_o_h,r_o_nw,rho_o,mdot_o,n_o,A_o_n)

#Pressure drop analysis
P_o = Pc + (1/(2*rho_o))*(mdot_o/(Cd_o*A_o_n))**2

P_i = Pc + (1/(2*rho_i))*(mdot_i/(Cd_i*A_i_n))**2

#print((P_o-Pc)/100000)
#print((P_i-Pc)/100000)

#Impingment distance (Li) [m]
Li = (r_o_nw-r_i_nw)/m.tan(m.radians(theta_i))

#Recess number (Lr/Li) > 1 for internal mixing
RN = Lr/Li

#Combined propellant density [kg/m3]
rho_t = (rho_o*mdot_o + rho_i*mdot_i)/(mdot_i+mdot_o)

#Combined axial nozzle velocity [m/s]
U_t_on = (mdot_i*U_i_ne + mdot_o*U_o_n)/(mdot_i+mdot_o)

#Combined nozzle filling coefficient
phi_t_on = (mdot_i+mdot_o)/(rho_t*U_t_on*A_o_n)

#Combined nozzle exit filling coefficient
phi_t_one = phi_t_on/m.sqrt(3-2*phi_t_on)

#Combined radius of mass avg liquid film in nozzle [m]
r_t_ma_on = r_o_nw*m.sqrt((2-phi_t_on)/2)

#Combined radius of mass avg liquid film at nozzle exit [m]
r_t_ma_one = r_o_nw*m.sqrt((2-phi_t_one)/2)

#Combined circumferential velocity in nozzle [m/s]
V_t_ma_on = (swirl_dir*mdot_i*V_i_ma_ine*r_i_ma_ine + mdot_o*V_o_ma_on*r_o_ma_on)/((mdot_o + mdot_i)*r_t_ma_on)

#Combined axial velocity at nozzle exit [m/s]
U_t_one = (mdot_o + mdot_i)/(rho_t*phi_t_one*A_o_n)

#Combined circumferential velocity at nozzle exit [m/s]
V_t_ma_one = V_t_ma_on*r_t_ma_on/r_t_ma_one

#Combined spray angle [deg]
theta_t = m.degrees(m.atan2(V_t_ma_one,U_t_one))

print('----------------------------------------------')
print('               Resulting Swirl                ')
print('----------------------------------------------')

print(f'Impingment distance: {round(Li*100,2)} cm')
print(f'Filling Coefficient in Nozzle: {round(phi_t_on,2)}')
print(f'Filling Coefficient at Nozzle Exit: {round(phi_t_one,2)}')
print(f'Axial Nozzle Velocity: {round(U_t_on,2)} m/s')
print(f'Axial Nozzle Exit Velocity: {round(U_t_one,2)} m/s')
print(f'Radius of mass avg liquid in nozzle: {round(r_t_ma_on*1000,2)} mm')
print(f'Radius of mass avg liquid at nozzle exit: {round(r_t_ma_one*1000,2)} mm')
print(f'Circumferential Nozzle Velocity: {round(V_t_ma_on,2)} m/s')
print(f'Circumferential Nozzle Exit Velocity: {round(V_t_ma_one,2)} m/s')
print(f'Resulting swirl angle: {round(theta_t,1)} deg')
print(f'Recess Number (RN): {round(RN,2)}')