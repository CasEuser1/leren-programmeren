land1 = input('Wat is het eerste land in groep A?')
land2 = input('Wat is het tweede land in groep A?')
land3 = input('Wat is het derde land in groep A?')

print(f'''
Wedstrijd |'Thuis'|    | 'uit' | Doelpunten land 1| Doelpunten land 2|    Winnaar
 _________|_______|____|_______|__________________|__________________|________________
1         |{land1}|    |{land2}|                  |                  |
2   	  |{land2}|    |{land3}|                  |                  |
3         |{land1}|    |{land3}|                  |                  |

''')
score1 = input(f'Hoevaak heeft {land1} gescoord?')
score2 = input(f'Hoevaak heeft {land2} gescoord?')
punten_land1 = 0
punten_land2 = 0
winnaar = ''
if score1 > score2:
    winnaar = land1
    punten_land1 += 3

elif score2 > score1:
    winnaar = land2
    punten_land2 += 3

print(f'''
    Land |               
________ | ________________________________________________________________________
{land1}     

''')

