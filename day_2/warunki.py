# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zaleznosci od warunku wykona jeden lub drugi blok programu
# warunek musi zwracac bool
odp = True  # prawda
# odp = False
if odp:
    # blok programu, wykonywany gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"
print(bool(odp))  # True

if odp:
    print("Dane zostały pobrane.")
# Dane zostały pobrane.

if odp == "Radek":
    print("Nadal Radek")
# Nadal Radek

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym razie
    print("Zero -> False")
# Zero -> False

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")

# operator morsa :=, walrus operator
# odpowiednik
# n = len(a)
# if n > 3:
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

# pierwszy warunek True oznacza wyjście z drzewa
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f'Podatek wynosi {podatek * zarobki}')
# dodac podatek 0.2 dla przedziału 10_000 do 39_999
# Podaj zarobki75000
# Podatek wynosi 30000.0
# ctrl / - automatyczny komentarz

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulejemy system zbierania logów
# zmienna bedzie zawierac informację jaki to system
# email, console, inny
# gdy log z systemu "console" wyświetlimy napis "Stało się coś strasznego"
# "email" -> "System email"
# jesi przyjdzie system "email"
# to w zmiennej bedzie poziom błedy: error, medium, inny
# nalezy do listy dodać opis błedu
alert_system = "email"
error = "error"
lista_b = []
if alert_system == "console":  # == porównanie
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Nie znam takiego systemu")

print(lista_b)
# System email
# ['Krytyczny']

# napisac program test z ....
# zadac pytanie
# pobrac odpowiedz
# spradzic czy prawidłowo i wyswietlic wynik testu
punkty = 0
odp = input("Podaj rok Chrztu Polski")  #
if odp.strip().casefold() == "966".casefold().strip():
    punkty += 1  # punkty = punkty + 1
    print("Dobrze")
else:
    print("Idż się pouczyć")

print("Punkty:", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
odp = input("Gdzie się odbył?")
if odp.strip().casefold() == "Gniezno".strip().casefold():  # Ostrów Lednicki
    punkty += 1
    print("Dobrze")
else:
    print("Musisz się dalej uczyć")
print("Razem punktów:", punkty)
# Podaj rok Chrztu Polski966
# Dobrze
# Punkty: 1
# Gdzie się odbył?Gniezno
# Dobrze
# Razem punktów: 2
