from Fruitmand import fruitmand

translated = ""
def translation(fruitColor: str) -> str:
    translated = {"yellow": "gele", "green": "groene", "orange": "oranje", "red": "rode", "brown": "bruine", "pink": "roze", "purple": "paarse", "black": "zwarte"}
    if fruitColor in translated:
        return translated[fruitColor]
    else:
        return fruitColor

lengte = []
lengte_nummer = []

for x in fruitmand:
    lengte_nummer.append(len(x['name']))

index = lengte_nummer.index(max(lengte_nummer))
longestFruit = fruitmand[index]

print(f"De {longestFruit['name']} ({len(longestFruit['name'])} letters) heeft een {translation(longestFruit['color'])} kleur en een gewicht van {longestFruit['weight'] / 1000}KG")