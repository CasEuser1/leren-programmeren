Naam = input('Wat is uw naam?')
if Naam == 'karen':
    raise NameError ('Karens zijn niet welkom, alstublieft ga weg.')
Gender = input('Wat is uw gender?')
if Gender != 'Man' and Gender != 'Vrouw':
    raise NameError ('Kies alstublieft tussen man en vrouw')
if Gender ==  ('man'):
    snor1 = input('Heeft u een snor?')
    if snor1 == 'ja':
        snor2 = int(input('Hoe breed is je snor in cm?'))
if Gender == ('vrouw'):
    Kapsel1 = input('Wat voor soort haar heeft u?')
    Kapsel2 = input('Wat voor kleur haar heeft u?')
    Kapsel3 = int(input('Hoelang is uw haar in cm?'))
hoed = input("Heeft u een hoge hoed?")
Rijbewijs = input("heeft u een geldig vrachtwagenbewijs?")
lengte = int(input("Hoelang bent u?"))
gewicht = int(input('Hoeveel weegt u?'))
if gewicht > 150:
    raise NameError ('Je bent te zwaar, ga sporten.')
MBO = input('Bent u in bezit van een Diploma MBO-4 ondernemen?')
Certificaat = input('Heeft Certificaat “Overleven met gevaarlijk personeel?')
Dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?'))
jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren?'))
acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?'))
strafblad = input('Heeft/had u een strafblad?')
banaan = input('Houd u van banaan?')
try:
    games = int(input('Hoeveel games speelt u?'))
except ValueError:
    raise NameError ('Noem de hoeveelheid alstublieft in nummers, geef geen titels en niet in letters typen.')

familie = int(input('Hoeveel broers en/of zussen heeft u?'))

if (Gender == 'man') or (Gender == 'vrouw' and Kapsel1 == 'krullen' and Kapsel2 == 'rood' and Kapsel3 >= 20) and  hoed == 'ja' and Rijbewijs == 'ja' and lengte >= 150 and gewicht >= 90 and MBO == 'ja' and Certificaat == 'ja' and Dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3 and strafblad == 'ja' and banaan == 'nee' and games >= 4 and familie >= 1:
    print('Je bent geslaagd')
else:
    print('Je hebt de sollicitaie niet goed ingevuld.')