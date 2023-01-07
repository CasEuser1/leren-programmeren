from Fruitmand import fruitmand
kleuren = []

for x in fruitmand:
    if x['name'] == 'druif':
        fruitmand.remove(x)

for x in fruitmand:
    if x['color'] not in kleuren:
        kleuren.append(x['color'])

print(kleuren)