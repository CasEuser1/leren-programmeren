def tafels(nummer: int):
    for x in range(1, 11):
        print(f"{x} x {nummer} = {x * nummer}")

tafels(int(input("Van welk getal wilt u de tafel zien?: ")))