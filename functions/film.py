def distribute(mdot_total,MR,percent_film):
    '''
    Takes total engine mass flow rate, mixture ratio, and percent film allocation
    and distributes the fuel flow to the main injector and to the film ports
    '''

    mdot_fuel_total = mdot_total/(MR+1)

    mdot_film = mdot_fuel_total*percent_film

    mdot_fuel_main = mdot_fuel_total - mdot_film


    return mdot_film, mdot_fuel_main

def film_size(mdot_film,num_film,cd_film,fuel_density,dP):
    import math 
    
    a_film = mdot_film/(cd_film*(2*fuel_density*dP)**0.5)

    d_film = (4*a_film/(num_film*math.pi))**0.5

    return d_film