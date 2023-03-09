gebruiker_nummer = 0
meer_rondes = True

def optellen(nummer1: float, nummer2: float):
    print(f"{nummer1} + {nummer2} = {float(nummer1) + float(nummer2)}")
    return nummer1 + nummer2

def aftrekken(nummer1: float, nummer2: float):
    print(f"{nummer1} - {nummer2} = {float(nummer1) - float(nummer2)}")
    return nummer1 -nummer2

def vermenigvuldigen(nummer1: float, nummer2: float):
    print(f"{nummer1} * {nummer2} = {float(nummer1) * float(nummer2)}")
    return nummer1 * nummer2

def delen(nummer1: float, nummer2: float):
    print(f"{nummer1} / {nummer2} = {float(nummer1) / float(nummer2)}")
    return nummer1 / nummer2

while meer_rondes:
    Som = input("""wat wil je doen?
    |     A) getallen optellen          | 
    |     B) getallen aftrekken         |        
    |     C) getallen vermenigvuldigen  |
    |     D) getallen delen             |
    |     E) getal ophogen              |
    |     F) getal verlagen             |
    |     G) getal verdubbelen          |
    |     H) getal halveren             |
         Kies: """).upper()

    if gebruiker_nummer:
        n1 = float(input("Welk getal: "))
        n2 = gebruiker_nummer
    elif Som == "A" or Som == "B" or Som == "C" or Som == "D":
        n1 = float(input("Getal 1: "))
        n2 = float(input("Getal 2: "))
    else:
        n1 = float(input("Welk getal: "))

    if Som == "A":
        gebruiker_nummer += float(optellen(n1, n2))
    elif Som == "B":
        gebruiker_nummer += min(n1, n2)
    elif Som == "C":
        gebruiker_nummer += vermenigvuldigen(n1, n2)
    elif Som == "D":
        gebruiker_nummer += delen(n1, n2)
    elif Som == "E":
        gebruiker_nummer += optellen(n1, 1)
    elif Som == "F":
        gebruiker_nummer += min(n1, 1)
    elif Som == "G":
        gebruiker_nummer += vermenigvuldigen(n1, 2)
    elif Som == "H":
        gebruiker_nummer += delen(n1, 2)

    meer_rondes = input(f"Do you want to do something with {gebruiker_nummer}? (Y/N): ").upper()
    if meer_rondes == "N":
        meer_rondes = False
    elif meer_rondes == "Y":
        meer_rondes = True
    else:
        print("Invalid answer")