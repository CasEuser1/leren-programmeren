geel = input("Is de kaas geel?")
if geel == "ja":
    gaten = input("Zitten er gaten in?")
    if gaten == "ja":
        Duur = input('Is de kaas belachelijk duur?')
        if Duur == "ja":
            print('De kaas die jij bedoelt is de Emmenthaler.')
        if Duur == "nee":
            print("De kaas de jij bedoelt is de Leerdammer.")
    elif gaten == "nee":
        Steen = input('Is de kaas hard als steen')
        if Steen == "ja":
            print("De kaas die jij bedoelt is de Parmigiano Reggiano.")
        if Steen == "nee":
            print("De kaas die jij bedoelt is de Goudse Kaas.")
if geel == "nee":
    Schimmel = input('Heeft de kaas blauwe schimmel?')
    if Schimmel == "ja":
        Korst = input('Heeft de kaas een korst?')
        if Korst == "ja":
            print('De kaas die jij bedoelt is de Blue de Rochbaron.')
        if Korst == "nee":
            print('De kaas die jij bedoelt is de Foume d Ambert.')
    elif Schimmel == "nee":
        Korst = input('Heeft deze kaas een korst?')
        if Korst == "Ja":
            print("De kaas die jij bedoelt is de Camembert.")
        if Korst == "nee":
            print('De kaas die jij bedoelt is de Mozzarella.')

        
    