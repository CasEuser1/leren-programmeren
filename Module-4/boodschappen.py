Lijst = {}
x = True

while x == True:
    print('Wat wil jij in je lijst doen?')
    User = input('')
    print('Hoeveel wil jij ervan hebben?')
    UserInt = int(input())
    Lijst.update({User: UserInt})
    quit = input('Typ Stop om te stoppen: ').lower()
    if quit == 'stop':
        x = False

print('- Boodschappenlijst -')
print('')
print(Lijst)
print('')
print('-------------------------------')