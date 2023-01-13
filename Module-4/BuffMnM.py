from random import randint

KleurMnM = ['bruin','rood', 'blauw','groen','geel']
vraag = int(input('Hoeveel M&M wil je hebben?'))
ZakMnM = {}

for x in range(vraag):
    KleurVerschil = randint(0,4)
    RandomKLeur = KleurMnM[KleurVerschil]
    if KleurMnM[KleurVerschil] not in ZakMnM:
        ZakMnM.update({RandomKLeur : 1})
    else:
        x = ZakMnM.get(KleurMnM[KleurVerschil]) +1
        ZakMnM.update({KleurMnM[KleurVerschil]:x})
    
print(ZakMnM)