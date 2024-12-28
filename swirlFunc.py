import math as m

def swirl(R,rh,rnw,rho,mdot,n,An,prnt:bool=True):

    K = rnw*R/(n*rh**2)     #Geometric constant

    phi_n = 0.01  #Initial filling coefficient guess
    err = 1     #Initializing error variable

    #Loop using Newtons Method for finding filling coefficient
    while err > 1e-6:

        phiX = (m.sqrt(2)*(1-phi_n))/phi_n**(3/2) - K
        phiXp = -3/2*m.sqrt(2)*phi_n**(-5/2) + m.sqrt(2)/2*phi_n**(-3/2)
        phi_n_new = phi_n - phiX/phiXp

        err = abs(phi_n_new - phi_n)
        phi_n = phi_n_new

    phi_ne = phi_n/(m.sqrt(3-2*phi_n))

    U_n = mdot/(rho*phi_n*An)       #Axial velocity in nozzle [m/s]
    U_ne = mdot/(rho*phi_ne*An)     #Axial velocity at nozzle exit [m/s]

    Vh = mdot/(rho*n*m.pi*rh**2)    #Circumferential velocity from inelt holes [m/s]

    P = R*Vh                            #Angular momentum of center swirl

    r_ma_n = rnw*m.sqrt((2-phi_n)/2)    #Radius of mass averaged liquid film in nozzle [m]
    r_ma_ne = rnw*m.sqrt((2-phi_ne)/2)  #Radius of mass averaged liquid film at nozzle exit [m]

    V_ma_n = P/r_ma_n                   #Circumferential velocity of liquid film in nozzle [m/s]
    V_ma_ne = P/r_ma_ne                 #Circumferential velocity of liquid film at nozzle exit [m/s]

    theta = m.degrees(m.atan(V_ma_ne/U_ne))      #Resulting angle of center swirl sheet  [deg]

    Cd = 1.7432*(K**0.4961 + (R/rnw)**-0.2956)**-2.4204

    #Printing

    if prnt == True:
        print(f'Filling Coefficient in Nozzle: {round(phi_n,2)}')
        print(f'Filling Coefficient at Nozzle Exit: {round(phi_ne,2)}')
        print(f'Nozzle Velocity: {round(U_n,2)} m/s')
        print(f'Nozzle Exit Velocity: {round(U_ne,2)} m/s')
        print(f'Radius of mass avg liquid film in nozzle: {round(r_ma_n*1000,2)} mm')
        print(f'Radius of mass avg liquid film at nozzle exit: {round(r_ma_ne*1000,2)} mm')
        print(f'Circumferential velocity of liquid film in nozzle: {round(V_ma_n,2)} m/s')
        print(f'Circumferential velocity of liquid film at nozzle exit: {round(V_ma_ne,2)} m/s')
        print(f'Resultant swirl angle: {round(theta,1)} deg')
        print(f'Geometric Constant (K): {round(K,2)}')
        print(f'Cd: {round(Cd,2)}')
    

    return theta, phi_n, phi_ne, U_ne, U_n, V_ma_ne, V_ma_n, Vh, r_ma_ne, r_ma_n, K, Cd