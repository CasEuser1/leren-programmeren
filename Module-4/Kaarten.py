import random

KaartTypes = ("harten ", "klaveren ", "schoppen ", "ruiten ")
Nummers = ("aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "koning")
Deck = ["joker", "joker"]

for x in (KaartTypes):
    for y in (Nummers):
        BijElkaar = x + y 
        Deck.append(BijElkaar)

random.shuffle(Deck)
for z in range(1,8):
    card = Deck.pop(0)
    print(f'Kaart {z}: {card}')

print(f"aantal kaarten: {len(Deck)} {Deck}")