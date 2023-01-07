from Fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
})
for x in fruitmand:
    print(x['weight'])