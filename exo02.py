nb = int(input("Entrez un nombre strictement positif : "))

listeDiviseurs=[]

for a in range(2, nb):
	if nb % int(a) == 0:
		listeDiviseurs.append(a)

if len(listeDiviseurs) > 0:
	print(f"Diviseurs propres sans répétition de {nb} : {', '.join(map(str, listeDiviseurs))} (soit {len(listeDiviseurs)} diviseurs propres)")
else:
	print(f"Il n'y en a pas. {nb} est le premier")
