import math as m
from functions import swirlFunc as SF
from functions import cd_hot

#inputs
# mdot,MR, rhoOx, rhoF,ox/f centered,swirl dir, R_i, R_o, rh_i, rh_o, rnw_i, rnw_o, w_thck, n_i, n_o, L recess, Pc

def biSwirl(mdot,MR,rho_ox,rho_f,Pc,centered,swirl_dir,R_i,R_o,r_i_h,r_o_h,r_i_nw,r_o_nw,n_i,n_o,w_th,Lr):

    #Mass flow rate of oxidizer [kg/s]
    mdot_ox = mdot*MR/(MR+1)

    #Mass flow rate of fuel [kg/s]
    mdot_f = mdot/(MR+1)

    #Dictates whether co-swirler (same direction) or counter-swirler (opposite direction)
    # Outer is held constant positive, inner can change direction
    # 1 = co-swirl and -1 = counter swirler

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

    #Cross sectional area of inner swirler [m2]
    A_i_n = m.pi*r_i_nw**2

    #Cross sectional area of outer swirler [m2]
    A_o_n = m.pi*(r_o_nw**2 - (r_i_nw+w_th)**2)

    #Inner swirl calculation
    theta_i, phi_i_n, phi_i_ne, U_i_ne, U_i_n, V_i_ma_ine, V_i_ma_in, V_i_h, r_i_ma_ine, r_o_ma_in, K_i, Cd_i = SF.swirl(R_i,r_i_h,r_i_nw,rho_i,mdot_i,n_i,A_i_n,False)

    #Outer swirl calculation
    theta_o, phi_o_n, phi_o_ne, U_o_ne, U_o_n, V_o_ma_one, V_o_ma_on, V_o_h, r_o_ma_one, r_o_ma_on, K_o, Cd_o = SF.swirl(R_o,r_o_h,r_o_nw,rho_o,mdot_o,n_o,A_o_n,False)

    #Pressure drop analysis
    P_o = Pc + (1/(2*rho_o))*(mdot_o/(Cd_o*A_o_n))**2

    P_i = Pc + (1/(2*rho_i))*(mdot_i/(Cd_i*A_i_n))**2

    #Impingment distance (Lc) [m]
    Lc = (r_o_nw-r_i_nw)/m.tan(m.radians(theta_i))

    #Recess number (Lr/Lc) > 1 for internal mixing
    RN = Lr/Lc

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
    theta_t = m.atan2(V_t_ma_one,U_t_one)*180/m.pi

    print(V_t_ma_one)
    print(U_t_one)
    #Cd correction for hot fire (iffy on accuracy)
    Cd_o_h, Cd_i_h = cd_hot.cd_factor(Cd_o,Cd_i,RN)

    #Pressure drops with corrected Cd
    P_o_h = Pc + (1/(2*rho_o))*(mdot_o/(Cd_o_h*A_o_n))**2
    P_i_h = Pc + (1/(2*rho_i))*(mdot_i/(Cd_i_h*A_i_n))**2

    #Out
    #Recess Number (RN),swirl angle (swirlAng), P outer (Po), P inner (Pi), P outer hot (Po_h), P inner hot (Pi_h), Vel axial (Uaxial), Vel Circum (VCircum),
    #Cd inner (Cdi), Cd outer (Cdo), Cd inner hot (Cdi_h), Cd outer hot (Cdo_h), K inner (Ki), K outer (Ko), Collision dist (Lc), Fill frac inner exit (PhiNEi),
    #Fill frac outer (PhiO)
    out_dict = {'RN':RN,
                'swirlAng':theta_t,
                'Po':P_o,
                'Pi':P_i,
                'Po_h':P_o_h,
                'Pi_h':P_i_h,
                'Uaxial':U_t_one,
                'Vcircum':V_t_ma_one,
                'Cdi':Cd_i,
                'Cdo':Cd_o,
                'Cdi_h':Cd_i_h,
                'Cdo_h':Cd_o_h,
                'Ki':K_i,
                'Ko':K_o,
                'Lc':Lc,
                'PhiNEi':phi_i_ne,
                'PhiO':phi_o_n}
    
    return out_dict