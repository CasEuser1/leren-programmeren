def optellen(nummer1: float, nummer2: float):
    return nummer1 + nummer2

def min(nummer1: float, nummer2: float):
    return nummer1 - nummer2

def vermenigvuldigen(nummer1: float, nummer2: float):
    return nummer1 * nummer2

def delen(nummer1: float, nummer2: float):
    return nummer1 / nummer2

user_input = 0
another_round = True

while another_round:
    som = input('''wat te doen?
    |     (A) getallen optellen          |
    |     (B) getallen aftrekken         |
    |     (C) getallen vermenigvuldigen  |
    |     (D) getallen delen             |
    |     (E) getal ophogen              |
    |     (F) getal verlagen             |
    |     (G) getal verdubbelen          |
    |     (H) getal halveren             |
    |     (I) stoppen                    |
          Kies: ''').capitalize         

    if user_input:
        num1 = float(input("Kies je eerst getal: "))
        num2 = user_input
    elif som == "A" or som == "B" or som == "C" or som == "D":
        num1 = float(input("Je eerst getal: "))
        num2 = float(input("Je tweede getal: "))
    else:
        num1 = float(input("Welk getal: "))

    if som == "A":
        user_input += float(optellen(num1, num2))
    elif som == "B":
        user_input += min(num1, num2)
    elif som == "C":
        user_input += vermenigvuldigen(num1, num2)
    elif som == "D":
        user_input += delen(num1, num2)
    elif som == "E":
        user_input += optellen(num1, 1)
    elif som == "F":
        user_input += min(num1, 1)
    elif som == "G":
        user_input += vermenigvuldigen(num1, 2)
    elif som == "H":
        user_input += delen(num1, 2)
    elif som == "I":
        exit()

    another_round = input(f"Wil je nog wat doen met {user_input}? (Yes/No): ").capitalize
    if another_round == "Nee":
        another_round = False
    elif another_round == "Ja":
        another_round = True
    else:
        print("Geen goed antwoord.")