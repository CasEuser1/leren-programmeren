def naamleeftijd(x: list):
    naam = input('Geef naam: ').capitalize()
    leeftijd = int(input('Geef een leeftijd: '))
    NamenEnLeeftijd.append({'naam': naam, 'leeftijd':leeftijd})
    return x

NamenEnLeeftijd = []
stop = True
while stop:
    naamleeftijd(NamenEnLeeftijd)
    stoppen = input('Toets enter om door te gaan of stop om te printen:').lower()
    if stoppen == 'stop':
        stop = False

x = len(NamenEnLeeftijd)
for aantallen in range(0,x):
    print(f'{NamenEnLeeftijd[aantallen]["naam"]} is {NamenEnLeeftijd[aantallen]["leeftijd"]}')