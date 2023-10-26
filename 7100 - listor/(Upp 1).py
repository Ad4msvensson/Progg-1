import random


resultat_lista = []

for x in range(10):
    kast = random.randint(1, 6)
    resultat_lista.append(kast)

resultat_lista.sort()

summa = sum(resultat_lista)

medelvärde = summa / len(resultat_lista)

minsta = min(resultat_lista)

största = max(resultat_lista)

antalet_sexor = resultat_lista.count(6)

print("Resultatlista:", resultat_lista)
print("Summa:", summa)
print("Medelvärde:", medelvärde)
print("Minsta:", minsta)
print("Största:", största)
print("Antal sexor:", antalet_sexor)