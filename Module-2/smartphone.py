telefoon = int(input('Hoe duur is de iPhone 13?'))
telefoon2 = int(input('Hoe duur is de Samnsung Galaxy S22?'))
verschil = telefoon - telefoon2
if telefoon > telefoon2:
    print(f'De iPhone is het duurst, de telefoon kost {telefoon}')
    print(f'De Samsung is het goedkoopst, de telefoon kost {telefoon2}')
    print(f'Het verschil is {verschil}')
    print('Het advies is dus de Samsung. Deze is namelijk goedkoper dan de iPhone.')
if verschil < 50:
    print('Het verschil is lager dan 50 euro, dus ik raad nogsteeds de iPhone aan.')

verschil2 = telefoon2 - telefoon
if telefoon2 > telefoon:
    print(f'De Samsung is het duurst,de telefoon kost {telefoon2}')
    print(f'De iPhone is het goedkoopst, de telefoon kost {telefoon}')
    print(f'Het verschil is {verschil}')
    print('Het advies is dus de iPhone. Deze is namelijk goedkoper dan da Samsung')
    if verschil2 < 50:
        print('Het verschil is lager dan 50 euro, dus ik raad nogsteeds de Samsung aan')

elif telefoon == telefoon2:
    print('Ze kosten allebei evenveel, maar iPhone had uw voorkeur, dus ik raad de iPhone aan.')
