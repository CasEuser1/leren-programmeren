# Cas Euser opdracht pizzaCalculator
PizzaSmall = int(input('Hoeveel Small pizzas van 25cm en 7$ wilt u?'))
PizzaMedium = int(input('Hoeveel medium pizzas van 29 cm en 9$ wilt u?'))
PizzaLarge = int(input('Hoeveel large pizzas van 35 cm en 12$ wilt u?'))
SmallPrijs = 7
MediumPrijs =9
LargePrijs =12
print('Uw pizzas kosten in totaal:')
print(f'{PizzaSmall * SmallPrijs} voor small')
print(f'{PizzaMedium * MediumPrijs} voor medium')
print(f'{PizzaLarge * LargePrijs} voor large')
print(f"{PizzaSmall * SmallPrijs + PizzaMedium * MediumPrijs + PizzaLarge * LargePrijs} Is uw totaalbedrag")
print('Bedankt voor uw bestelling!')

# Was lastig