from time import time
import random as zufall
import tkinter as tk
import threading
import os

# Initialisierung
fragen_anzeigen = True

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

eingabefeld_1 = None
eingabefeld_2 = None
start = None

def ergaenze_passwörter(sicherheitsstufe, limit, ziffernlimit=0, sonderzeichenlimit=0, anzahl=1):
    if not os.path.isfile("Passwörter.txt"):
        with open("Passwörter.txt", "w") as datei:
            pass

    with open("Passwörter.txt", "r") as datei:
        vorhandene_passwoerter = datei.readlines()
        bereits_erstellt = len(vorhandene_passwoerter)
        differenz = anzahl - bereits_erstellt

    if differenz > 0:
        passwort_count = 0
        while passwort_count < differenz:
            if sicherheitsstufe == '1':
                passwort = passwort_niedrig(limit)
            elif sicherheitsstufe == '2':
                passwort = passwort_mittel(limit, ziffernlimit)
            elif sicherheitsstufe == '3':
                passwort = passwort_hoch(limit, ziffernlimit, sonderzeichenlimit)
            print(passwort)
            passwort_speicherung(passwort)
            passwort_count += 1
    else:
        print("Es wurden bereits genügend Passwörter erstellt.")

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
        zufallsindex = zufall.randint(0, 7)
        zufallswert = sonderzeichen[zufallsindex]
        werteliste.append(zufallswert)
    zufall.shuffle(werteliste)
    passwort = ''.join(werteliste)
    return passwort

def passwort_speicherung(passwort):
    with open("Passwörter.txt", "a") as datei:
        datei.write(passwort + "\n")

def passwort_generieren(sicherheitsstufe, limit, ziffernlimit=0, sonderzeichenlimit=0, anzahl=1):
    passwort_count = 0
    while passwort_count < anzahl:
        if sicherheitsstufe == '1':
            passwort = passwort_niedrig(limit)
        elif sicherheitsstufe == '2':
            passwort = passwort_mittel(limit, ziffernlimit)
        elif sicherheitsstufe == '3':
            passwort = passwort_hoch(limit, ziffernlimit, sonderzeichenlimit)
        print(passwort)
        passwort_speicherung(passwort)
        passwort_count += 1

def sicherheitslevel():
    sicherheitsstufe = eingabefeld_1.get()
    if sicherheitsstufe in ['1', '2', '3']:
        if sicherheitsstufe == '1':
            limit = 6
            print("Sie haben die niedrige Sicherheitsstufe gewählt.")
        elif sicherheitsstufe == '2':
            limit = 10
            ziffernlimit = zufall.randint(2, 6)
            print("Sie haben die mittlere Sicherheitsstufe gewählt.")
        elif sicherheitsstufe == '3':
            limit = 25
            ziffernlimit = zufall.randint(2, 4)
            sonderzeichenlimit = zufall.randint(2, 6)
            print("Sie haben die hohe Sicherheitsstufe gewählt.")

        eingabefeld_1.config(state='disabled')  # Deaktiviere das Eingabefeld nach der Eingabe
        eingabefeld_2.config(state='disabled')  # Deaktiviere das Eingabefeld nach der Eingabe
        start.config(state='disabled')  # Deaktiviere den Start-Button nach der Eingabe

        anzahl = int(eingabefeld_2.get())
        ergaenze_passwörter(sicherheitsstufe, limit, ziffernlimit, sonderzeichenlimit, anzahl)
    else:
        print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")

def fenster():
    global eingabefeld_1, eingabefeld_2, start
    # Fenster erstellen
    fenster = tk.Tk()
    fenster.title("Password Manager")

    # Fenstergröße festlegen
    bildschirm_breite = fenster.winfo_screenwidth()
    bildschirm_höhe = fenster.winfo_screenheight()
    fensterbreite = int(bildschirm_breite * 0.6)
    fensterhöhe = int(bildschirm_höhe * 0.6)
    fenster.geometry(f"{fensterbreite}x{fensterhöhe}")

    # Komponenten hinzufügen
    label1 = tk.Label(fenster, text="Sicherheitsstufe (1, 2 oder 3):")
    label1.pack(pady=10)
    eingabefeld_1 = tk.Entry(fenster)
    eingabefeld_1.pack()

    label2 = tk.Label(fenster, text="Anzahl der Passwörter:")
    label2.pack(pady=10)
    eingabefeld_2 = tk.Entry(fenster)
    eingabefeld_2.pack()
    # Button erstellen
    start = tk.Button(fenster, text="Passwortgenerator Starten", command=sicherheitslevel)
    start.pack()

    # Fensterloop
    fenster.mainloop()

# Hauptfunktion aufrufen
fenster()
