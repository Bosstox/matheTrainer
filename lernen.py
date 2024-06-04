import tkinter as tk
import random
import time

# Funktion zum Generieren einer neuen Aufgabe für Addition, Subtraktion oder Multiplikation
def neue_aufgabe(operator_auswahl):
    global zahl1, zahl2, operator, richtige_antwort, aufgaben_zaehler
    operator = operator_auswahl
    if operator in ['+', '-']:
        while True:
            zahl1 = random.randint(1, 100)
            zahl2 = random.randint(1, 100)
            if operator == '-' and zahl1 < zahl2:
                zahl1, zahl2 = zahl2, zahl1  # Sicherstellen, dass das Ergebnis nicht negativ ist
            if operator == '+':
                richtige_antwort = zahl1 + zahl2
            elif operator == '-':
                richtige_antwort = zahl1 - zahl2
            if richtige_antwort <= 100:
                break
    elif operator == '*':
        while True:
            zahl1 = random.randint(1, 10)
            zahl2 = random.randint(1, 10)
            richtige_antwort = zahl1 * zahl2
            if richtige_antwort <= 100:
                break
    aufgabe.set(f"{zahl1} {operator} {zahl2} = ?")
    if operator == '*':
        eingabe_malreihen.delete(0, tk.END)
    else:
        eingabe_addsub.delete(0, tk.END)

# Funktion zum Überprüfen der Antwort
def antwort_pruefen(event=None):
    global richtige_antworten, falsche_antworten, aufgaben_zaehler
    try:
        if operator == '*':
            user_antwort = int(eingabe_malreihen.get())
        else:
            user_antwort = int(eingabe_addsub.get())
        if user_antwort == richtige_antwort:
            ergebnis.set("Richtig!")
            richtige_antworten += 1
        else:
            ergebnis.set(f"Falsch! Richtig wäre {richtige_antwort}")
            falsche_antworten += 1
    except ValueError:
        ergebnis.set("Bitte eine gültige Zahl eingeben")
    update_statistik()
    aufgaben_zaehler += 1
    if aufgaben_zaehler < 50 and time.time() - startzeit < 180:
        neue_aufgabe(operator)
    else:
        ergebnis.set("Test beendet!")
        test_ende()

# Funktion zum Aktualisieren der Statistik
def update_statistik():
    statistik.set(f"Richtig: {richtige_antworten}  Falsch: {falsche_antworten}")

# Funktion zum Zurücksetzen der Statistik
def statistik_zuruecksetzen():
    global richtige_antworten, falsche_antworten
    richtige_antworten = 0
    falsche_antworten = 0
    update_statistik()

# Funktion zum Anzeigen der Übungsseite für die Malreihen
def zeige_malreihen_uebung(malreihe):
    global malreihe_auswahl
    malreihe_auswahl = malreihe
    startseite.pack_forget()
    malreihenseite.pack()
    neue_aufgabe('*')

# Funktion zum Anzeigen der Übungsseite für Addition und Subtraktion
def zeige_add_sub_uebung(operator):
    startseite.pack_forget()
    addsubseite.pack()
    neue_aufgabe(operator)

# Funktion zum Zurückkehren zur Startseite
def zurueck_zur_startseite():
    malreihenseite.pack_forget()
    addsubseite.pack_forget()
    startseite.pack()

# Funktion zum Starten des Tests
def starte_test():
    global aufgaben_zaehler, startzeit
    aufgaben_zaehler = 0
    startzeit = time.time()
    statistik_zuruecksetzen()
    startseite.pack_forget()
    malreihenseite.pack()
    neue_aufgabe('*')
    aktualisiere_timer()

# Funktion zum Aktualisieren des Timers
def aktualisiere_timer():
    verbleibende_zeit = 180 - int(time.time() - startzeit)
    if verbleibende_zeit >= 0 and aufgaben_zaehler < 50:
        timer.set(f"Verbleibende Zeit: {verbleibende_zeit} Sekunden")
        root.after(1000, aktualisiere_timer)
    else:
        ergebnis.set("Test beendet!")
        test_ende()

# Funktion zum Beenden des Tests
def test_ende():
    malreihenseite.pack_forget()
    startseite.pack()

# Hauptanwendung
root = tk.Tk()
root.title("Mathematik Lernprogramm")

aufgabe = tk.StringVar()
ergebnis = tk.StringVar()
statistik = tk.StringVar()
timer = tk.StringVar()
malreihe_auswahl = 1
zahl1, zahl2, operator, richtige_antwort = 0, 0, '', 0
richtige_antworten = 0
falsche_antworten = 0
aufgaben_zaehler = 0
startzeit = 0

# Startseite
startseite = tk.Frame(root)
tk.Label(startseite, text="Hallo Imran, was willst du heute lernen?", font=('Arial', 20)).pack(pady=20)
tk.Button(startseite, text="Addition und Subtraktion lernen", command=lambda: zeige_add_sub_uebung('+'), font=('Arial', 15)).pack(pady=10)
tk.Button(startseite, text="Malreihen lernen", command=lambda: zeige_malreihen_uebung(1), font=('Arial', 15)).pack(pady=10)
tk.Button(startseite, text="Multiplikationstest starten", command=starte_test, font=('Arial', 15)).pack(pady=10)
startseite.pack()

# Malreihenseite
malreihenseite = tk.Frame(root)
tk.Label(malreihenseite, textvariable=timer, font=('Arial', 15)).pack(pady=10)
tk.Label(malreihenseite, textvariable=aufgabe, font=('Arial', 20)).pack(pady=20)
eingabe_malreihen = tk.Entry(malreihenseite, font=('Arial', 20))
eingabe_malreihen.pack(pady=20)
eingabe_malreihen.bind('<Return>', antwort_pruefen)
tk.Button(malreihenseite, text="Antwort überprüfen", command=antwort_pruefen, font=('Arial', 15)).pack(pady=20)
tk.Label(malreihenseite, textvariable=ergebnis, font=('Arial', 20)).pack(pady=20)
tk.Button(malreihenseite, text="Zurück zur Startseite", command=zurueck_zur_startseite, font=('Arial', 15)).pack(pady=20)

# Additions- und Subtraktionsseite
addsubseite = tk.Frame(root)
tk.Label(addsubseite, textvariable=aufgabe, font=('Arial', 20)).pack(pady=20)
eingabe_addsub = tk.Entry(addsubseite, font=('Arial', 20))
eingabe_addsub.pack(pady=20)
eingabe_addsub.bind('<Return>', antwort_pruefen)
tk.Button(addsubseite, text="Antwort überprüfen", command=antwort_pruefen, font=('Arial', 15)).pack(pady=20)
tk.Label(addsubseite, textvariable=ergebnis, font=('Arial', 20)).pack(pady=20)
tk.Button(addsubseite, text="Zurück zur Startseite", command=zurueck_zur_startseite, font=('Arial', 15)).pack(pady=20)

# Statistikbereich
statistik_frame = tk.Frame(root)
tk.Label(statistik_frame, textvariable=statistik, font=('Arial', 15)).pack(pady=10)
tk.Button(statistik_frame, text="Statistik zurücksetzen", command=statistik_zuruecksetzen, font=('Arial', 15)).pack(pady=10)
statistik_frame.pack()

# Initialisierung der Statistik
update_statistik()

# Hauptschleife starten
root.mainloop()
