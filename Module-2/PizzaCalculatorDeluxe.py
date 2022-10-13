#PizzaCalculatorDeluxe van Cas

try:
    PizzaSmall = int(input('Hoeveel Small pizzas van 25cm en 7$ wilt u?'))
except ValueError:
    print('U heeft iets verkeerd ingetypt, gebruik alstublieft cijfers en geen letters.')
    exit()
try:
    PizzaMedium = int(input('Hoeveel medium pizzas van 29 cm en 9$ wilt u?'))
except ValueError:
    print('U heeft iets verkeerd ingetypt, gebruik alstublieft cijfers en geen letters.')
    exit()
try:
    PizzaLarge = int(input('Hoeveel large pizzas van 35 cm en 12$ wilt u?'))
except ValueError:
    print('U heeft iets verkeerd ingetypt, gebruik alstublieft cijfers en geen letters.')
    exit()

SmallPrijs = 7
MediumPrijs = 9
LargePrijs = 12

print('---------------------------------------------------------------------------------------------------------')
print('Uw pizzas kosten in totaal:')
print(f'{PizzaSmall * SmallPrijs} euro voor small')
print(f'{PizzaMedium * MediumPrijs} euro voor medium')
print(f'{PizzaLarge * LargePrijs} euro voor large')
print(f"{PizzaSmall * SmallPrijs + PizzaMedium * MediumPrijs + PizzaLarge * LargePrijs} euro Is uw totaalbedrag")
print('Bedankt voor uw bestelling!')
print('---------------------------------------------------------------------------------------------------------')