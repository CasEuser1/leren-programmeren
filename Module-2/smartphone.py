telefoon =int(input('Hoe duur is de iPhone 13?'))
telefoon2 = int(input('Hoe duur is de Samnsung Galaxy S22?'))
if telefoon > telefoon2:
    print(f'De iPhone is het duurst, de telefoon kost {telefoon}')
    print(f'De Samsung is het goedkoopst, de telefoon kost {telefoon2}')
    print('Het advies is dus de Samsung. Deze is namelijk goedkoper dan de iPhone.')
elif telefoon2 > telefoon:
    print(f'De Samsung is het duurst,de telefoon kost {telefoon2}')
    print(f'De iPhone is het goedkoopst, de telefoon kost {telefoon}')
    print('Het advies is dus de iPhone. Deze is namlijk goedkoper dan de Samsung.')
elif telefoon == telefoon2:
    print('Ze kosten allebei evenveel, maar iPhone had uw voorkeur, dus ik raad de iPhone aan.')