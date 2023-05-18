from time import time
import random as zufall

# Zufallszahlen Generation
zufall.seed()

# Listendefinition
werteliste = []

# Großbuchstaben Indizes 26-51
buchstaben = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Max.Index 10
sonderzeichen = ['!', '#', '$', '%', '&', '*', '+', ',', '-', '.', '/']

def passwort_niedrig(limit):
    werteliste.clear()
    for _ in range(limit):
        zufallsindex = zufall.randint(0, 51)
        zufallswert = buchstaben[zufallsindex]
        werteliste.append(zufallswert)
    zufall.shuffle(werteliste)
    passwort = ''.join(werteliste)
    return passwort

def passwort_mittel(limit, ziffernlimit):
    werteliste.clear()
    for _ in range(limit):
        zufallsindex = zufall.randint(0, 51)
        zufallswert = buchstaben[zufallsindex]
        werteliste.append(zufallswert)
    for _ in range(ziffernlimit):
        werteliste.append(str(zufall.randint(0, 9)))
    zufall.shuffle(werteliste)
    passwort = ''.join(werteliste)
    return passwort

def passwort_hoch(limit, ziffernlimit, sonderzeichenlimit):
    werteliste.clear()
    for _ in range(limit):
        zufallsindex = zufall.randint(0, 51)
        zufallswert = buchstaben[zufallsindex]
        werteliste.append(zufallswert)
    for _ in range(ziffernlimit):
        werteliste.append(str(zufall.randint(0, 9)))
    for _ in range(sonderzeichenlimit):
        zufallsindex = zufall.randint(0, 10)
        zufallswert = sonderzeichen[zufallsindex]
        werteliste.append(zufallswert)
    zufall.shuffle(werteliste)
    passwort = ''.join(werteliste)
    return passwort

def passwort_speicherung(passwort):
    with open("Passwörter.txt", "a") as datei:
        datei.write(passwort + "\n")

def sicherheitslevel():
    while True:
        länge = int(input("Wählen Sie Ihre Sicherheitsstufe. 1=Niedrig 2=Mittel 3=Hoch: "))
        if länge in [1, 2, 3]:
            return länge
        print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")

def passwortanzahl():
    while True:
        try:
            anzahl = int(input("Wie viele Passwörter möchten Sie generieren? "))
            return anzahl
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

def passwort_generator():
    länge = sicherheitslevel()
    anzahl = passwortanzahl()

    if länge == 1:
        limit = 6
        print("Sie haben die niedrige Sicherheitsstufe gewählt.")
        for _ in range(anzahl):
            passwort = passwort_niedrig(limit)
            print(passwort)
            passwort_speicherung(passwort)

    elif länge == 2:
        limit = 10
        ziffernlimit = zufall.randint(2, 6)
        print("Sie haben die mittlere Sicherheitsstufe gewählt.")
        for _ in range(anzahl):
            passwort = passwort_mittel(limit, ziffernlimit)
            print(passwort)
            passwort_speicherung(passwort)

    elif länge == 3:
        limit = 25
        ziffernlimit = zufall.randint(2, 4)
        sonderzeichenlimit = zufall.randint(2, 6)
        print("Sie haben die hohe Sicherheitsstufe gewählt.")
        for _ in range(anzahl):
            passwort = passwort_hoch(limit, ziffernlimit, sonderzeichenlimit)
            print(passwort)
            passwort_speicherung(passwort)

    else:
        #Fehlermeldung
        print("Ein Fehler ist aufgetreten.")

# Programm erklärung
print("Dieses Programm erstellt zufällige Passwörter.")

# Hauptfunktion aufrufen
passwort_generator()
