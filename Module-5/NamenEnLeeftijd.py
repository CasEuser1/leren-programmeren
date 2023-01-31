def naamleeftijd(x: list):
    stop = True
    while stop:
        naam = input('Geef naam: ').capitalize()
        leeftijd = input('Geef een leeftijd: ')
        if naam == 'stop' or leeftijd == 'stop':
            stop = False
            return x
        NamenEnLeeftijd.append({'naam': naam, 'leeftijd':leeftijd})

NamenEnLeeftijd = []

naamleeftijd(NamenEnLeeftijd)

print(NamenEnLeeftijd)