from Fruitmand import fruitmand

a = sorted(fruitmand, key=lambda i: i['weight'])

for i in a [::-1]:
    print(f'{i["name"]}: {i["weight"]}') 