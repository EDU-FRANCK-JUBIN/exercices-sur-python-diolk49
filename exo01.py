from math import *

hauteur = float(input("Saisir la hauteur en cm : "))
rayon = float(input("Saisir le rayon en cm : "))

volume = (pi * rayon*rayon * hauteur)/3

print(f"Le volume du cube est de {volume} cm3")
