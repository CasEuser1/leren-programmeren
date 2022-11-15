nummer1 = 50
som = 50
string = '50 '

while som < 1000:
    nummer1 += 1
    som += nummer1
    string += f'+ {nummer1}'
    print(f'{string} = {som}')