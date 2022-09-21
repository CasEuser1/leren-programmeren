naam = input('Wat is je naam')
leeftijd = int(input('Wat is je leeftijd'))
print(type (leeftijd))
speciale_naam = ('Arnold')


# iedereen jonger dan 18 mag niet naar binnen
# tussen de 18 en 21 wel naar binnen maar geen sterke drank
# boven de 21 naar binnen en sterke drank

if leeftijd < 18:
    print(f'Helaas {naam} je mag nog niet naar binnen.')
    if naam == 'Arnold':
        print(f'Hallo {naam} hier je vrijkaart.')
    else:
        print("Hier heb je een sticker.")
elif leeftijd >= 18 and leeftijd < 21:
    print(f'Welkom {naam}, je mag naar binnen maar geen sterke drank bestellen.')
else:
    print(f'Welkom {naam}, je mag naar binnen en sterke drank bestellen.')

    