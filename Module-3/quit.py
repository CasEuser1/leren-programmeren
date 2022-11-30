# stelt de vraag "?" aan de gebruiker
# zolang er geen quit geantwoord word stel je de vraag opnieuw
# print het aantal keer dat de vraag gesteld is
aantal_keer = 0
vraag = input("?")
while vraag != "quit":
    aantal_keer += 1
    vraag = input("?")

print(f'{aantal_keer} pogingen.')