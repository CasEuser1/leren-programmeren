getal = 50
som = 50
string = '50 '

while som < 1000:
    getal += 1
    som += getal
    string += f'+ {getal}'
    print(f'{string} = {som}')