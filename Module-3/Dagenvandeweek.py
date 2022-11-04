vraag = input('Welke dag is het vandaag?')
dagen = ["Maandag","Dinsdag","Woensdag","Donderdag","Vrijdag","Zaterdag","Zondag"]
while vraag != dagen[0]:
    print(dagen[0])
    dagen.pop(0)
