def optellen(number1: float, number2: float):
    print(f"{number1} + {number2} = {float(number1) + float(number2)}")
    return number1 + number2

def aftrekken(number1: float, number2: float):
    print(f"{number1} - {number2} = {float(number1) - float(number2)}")
    return number1 -number2

def keer(number1: float, number2: float):
    print(f"{number1} * {number2} = {float(number1) * float(number2)}")
    return number1 * number2

def delen(number1: float, number2: float):
    print(f"{number1} / {number2} = {float(number1) / float(number2)}")
    return number1 / number2

nummer = 0
another_round = True

while another_round:
    keuze = input("""wat te doen?
    |    A) getallen optellen           |
    |    B) getallen aftrekken          |
    |    C) getallen vermenigvuldigen   |
    |    D) getallen delen              |
    |    E) getal ophogen               |
    |    F) getal verlagen              |
    |    G) getal verdubbelen           |
    |    H) getal halveren              |
    |    Kies: """).upper()

    if nummer != 0:
        n1 = nummer
        n2 = float(input("Welk getal: "))
        nummer = 0
        
    elif keuze == "A" or keuze == "B" or keuze == "C" or keuze == "D":
        n1 = float(input("Getal 1: "))
        n2 = float(input("Getal 2: "))
    else:
        n1 = float(input("Welk getal: "))

    if keuze == "A":
        nummer += float(optellen(n1, n2))
    elif keuze == "B":
        nummer += aftrekken(n1, n2)
    elif keuze == "C":
        nummer += keer(n1, n2)
    elif keuze == "D":
        nummer += delen(n1, n2)
    elif keuze == "E":
        nummer += optellen(n1, 1)
    elif keuze == "F":
        nummer += aftrekken(n1, 1)
    elif keuze == "G":
        nummer += keer(n1, 2)
    elif keuze == "H":
        nummer += delen(n1, 2)

    another_round = input(f"Do you want to do something with {nummer}? (Y/N): ").upper()
    if another_round == "N":
        another_round = False
    elif another_round == "Y":
        another_round = True
    else:
        print("Invalid answer")