import random
naam = input ('Wat is je naam')
nummer = int(input('Hoeveel complimenten wil je?'))

for x in range (nummer):
    hip = random.randint(1,4)
    if hip == 1:
        print(f'Je bent cool {naam}')
    elif hip == 2:
        print(f'Je bent goofy ahh {naam}')
    elif hip == 3:
        print(f'Je bent slim {naam}')
    elif hip == 4:
        print(f'Je bent geweldig {naam}')
    vorige_randint = (hip)
    print(vorige_randint)

