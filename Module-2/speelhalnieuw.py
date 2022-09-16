Toegangsticket = 7.45
Aantal_mensen = 4.0
Gameseat = 0.37
GameseatTijd = 45.0
Gameseat5 = 5.0

Mensen = int(input("Wat is het aantal mensen dat binnenkomt?"))
Seat = float(input("Hoelang wilde je de VIP-Seat gebruiken?"))

totaal_tickets = Mensen * Toegangsticket
totaalprijs_gameseat = Mensen + Seat / Gameseat5 * Gameseat

print(f'{totaal_tickets} euro voor toegangstickets')
print(f'{totaalprijs_gameseat} euro voor de VR')