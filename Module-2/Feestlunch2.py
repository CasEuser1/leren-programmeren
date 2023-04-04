prijs1 = 39
prijs2 = 278 
kortingprijs = 50
croissant = float(input('Hoeveel croissantjes?'))
stokbrood = float(input('Hoeveel stokbroden'))
korting = float(input('Hoeveel kortingsbonnen heeft u?'))
print(f'{stokbrood * prijs2 + croissant * prijs1 - korting * kortingprijs} cent')