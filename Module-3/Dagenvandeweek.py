vraag = input('Welke dag is het vandaag?')
dagen = ["Maandag","Dinsdag","Woensdag","Donderdag","Vrijdag","Zaterdag","Zondag"]
while vraag != dagen[-1]:
    print(dagen[-1])
    dagen.pop(-1)
