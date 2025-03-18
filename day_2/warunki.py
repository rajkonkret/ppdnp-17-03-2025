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
