from Fruitmand import fruitmand
import random

Nieuwe_Random_fruit = -1
aantal_fruit = int(input('Hoeveel stukken fruit wil je?'))

for i in fruitmand:
    Nieuwe_Random_fruit += 1

for i in range(0, aantal_fruit):
    random_fruit = random.randint(0, Nieuwe_Random_fruit)
    print(fruitmand[random_fruit]['name'])