from time import time
import random as zufall

#Zufallszahlen Generation
zufall.seed()

#Listendefinition
werteliste = []

#Großbuchstaben Indizes 26-51
buchstaben=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Max.Index 10
sonderzeichen=['!', '#', '$', '%', '&', '*', '+', ',', '-', '.', '/']

#Programm erklärung
print("Dieses Programm erstellt zufällige Passwörter.")

#IO-Sequenz
länge = int(input("Wählen Sie ihre Sicherheitsstufe. 1=Niedrig 2=Mittel 3=Hoch"))

#Niedrige Sicherheitsstufe
if länge == 1:
    limit = 6
    i = 0
    print("Sie haben die niedrige Sicherheitsstufe gewählt.")
    for i in range(limit):
        zufallsindex = zufall.randint(0, 51)
        zufallswert = buchstaben[zufallsindex]
        werteliste.append(zufallswert)
        passwort = ''.join(werteliste)
        zeichenliste = list(passwort)
        zufall.shuffle(zeichenliste)
        passwort=''.join(zeichenliste)
    print(passwort)
    with open("Passwörter.txt", "a") as datei:
        datei.write(passwort + "\n")


#Mittlere Sicherheitsstufe
elif länge == 2:
    limit = 10
    ziffernlimit=zufall.randint(2,6)
    zufall.seed()
    i = 0
    print("Sie haben die mittlere Sicherheitsstufe gewählt.")
    for i in range(limit):
        zufallsindex = zufall.randint(0, 51)
        zufall.seed()
        zufallswert = buchstaben[zufallsindex]
        werteliste.append(zufallswert)
        passwort = ''.join(werteliste)
    for i in range(ziffernlimit):
        passwort=passwort+str(zufall.randint(0,9))
        zufall.seed()
        zeichenliste = list(passwort)
        zufall.shuffle(zeichenliste)
        passwort=''.join(zeichenliste)
    print(passwort)
    with open("Passwörter.txt", "a") as datei:
        datei.write(passwort + "\n")

#Hohe Sicherheitsstufe
elif länge == 3:
    limit = 25
    ziffernlimit=zufall.randint(2,4)
    zufall.seed()
    sonderzeichenlimit=zufall.randint(2,6)
    zufall.seed()
    i = 0
    print("Sie haben die hohe Sicherheitsstufe gewählt.")
    for i in range(limit):
        zufallsindex = zufall.randint(0, 51)
        zufall.seed()
        zufallswert = buchstaben[zufallsindex]
        werteliste.append(zufallswert)
        passwort = ''.join(werteliste)
    for i in range(ziffernlimit):
        passwort=passwort+str(zufall.randint(0,9))
        zufall.seed()
    for i in range(sonderzeichenlimit):
        zufallsindex = zufall.randint(0,10)
        zufall.seed()
        zufallswert = sonderzeichen[zufallsindex]
        werteliste.append(zufallswert)
        passwort = ''.join(werteliste)
        zeichenliste = list(passwort)
        zufall.shuffle(zeichenliste)
        passwort=''.join(zeichenliste)
    print(passwort)
    with open("Passwörter.txt", "a") as datei:
        datei.write(passwort + "\n")

#Fehlerhafte Eingabe
else:
    print("Ein Fehler ist aufgetreten.")