import random
naam = input ('Wat is je naam')
nummer = int(input('Hoeveel complimenten wil je?'))

for x in range (nummer):
    hip = random.randint(1,4)
    if hip == 1:
        print(f'Je bent cool {naam}')
        if hip == 1:
            print(f'{2 or 3 or 4}')
    elif hip == 2:
        print(f'Je bent goofy ahh {naam}')
        if hip == 2:
            print(f'{1 or 3 or 4}')
    elif hip == 3:
        print(f'Je bent slim {naam}')
        if hip == 3:
            print(f'{1 or 2 or 4}')
    elif hip == 4:
        print(f'Je bent geweldig {naam}')
        if hip == 4:
            print(f'{1 or 2 or 3}')

