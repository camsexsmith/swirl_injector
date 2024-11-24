import math as m

def swirl(R,rh,rnw,rho,mdot,n,An):

    K = rnw*R/(n*rh**2)     #Geometric constant


    phi_i_n = 0.1  #Initial filling coefficient guess
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
    print(f'Filling Coefficient at Nozzle Exit: {round(phi_i_ne,2)}')

    U_n = mdot/(rho*phi_i_n*An)       #Axial velocity in nozzle [m/s]
    U_ne = mdot/(rho*phi_i_ne*An)     #Axial velocity at nozzle exit [m/s]

    print(f'Center Nozzle Velocity: {round(U_n,2)} m/s')
    print(f'Center Nozzle Exit Velocity: {round(U_ne,2)} m/s')

    Vh = mdot/(rho*n*m.pi*rh**2)    #Circumferential velocity from inelt holes [m/s]

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

    return