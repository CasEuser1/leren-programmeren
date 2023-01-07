from random import randint,choice

KleurMnM = ('bruin','oranje', 'blauw','groen')
vraag = int(input('Hoeveel M&M wil je hebben?'))
LegeList = []

for x in range(vraag):
    KleurVerschil = randint(0,3)
    LegeList.append(KleurMnM[KleurVerschil])
print(LegeList)
