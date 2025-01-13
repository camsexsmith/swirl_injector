from functions import film

mdot = 1

MR = 2

mdot_film, mdot_fuel = film.distribute(mdot,MR,0.1)

print(mdot_film)
print(mdot_fuel)