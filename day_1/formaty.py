user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001  #
print(type(wersja))  # <class 'float'> - liczby zmiennoprzecinkowe
liczba = 678987654123  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.

# TypeError: %d format: a real number is required, not str
# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# %d - liczba całkowita (integer)
# %s - łańcuch znaków (string)
# %f - liczba zmiennoprzecinkowa (float)

print("Witaj %(user)s, jestes%(user)s" % {"user": user})
# Witaj Tomek, jestesTomek

# f-string
print(f"witaj {user}, masz teraz {wiek} lat.")
# witaj Tomek, masz teraz 39 lat.

print("Uzywamy wersji pythona %i" % 3)  # Uzywamy wersji pythona 3
print("Uzywamy wersji pythona %f" % 3)  # Uzywamy wersji pythona 3.000000
print("Uzywamy wersji pythona %.2f" % 3.9)  # Uzywamy wersji pythona 3.90
print("Uzywamy wersji pythona %.1f" % 3.9)  # Uzywamy wersji pythona 3.9
print("Uzywamy wersji pythona %.0f" % 3.9)  # Uzywamy wersji pythona 4 zaokrągla do wyświetlania
print("Uzywamy wersji pythona %.f" % 3.9)  # Uzywamy wersji pythona 4 zaokrągla do wyświetlania

x = 3.8796
print(x)  # 3.8796
print("%.2f" % x)  # 3.88
print(x)  # 3.8796

print(f"Uzywamy wersji pythona {wersja}")
print(f"Uzywamy wersji pythona {wersja:.2f}")
print(f"Uzywamy wersji pythona {wersja:.1f}")
print(f"Uzywamy wersji pythona {wersja:.0f}")
# Uzywamy wersji pythona 3.90001
# Uzywamy wersji pythona 3.90
# Uzywamy wersji pythona 3.9
# Uzywamy wersji pythona 4

print(f"{user:<10}")  # "Tomek     " # rownanie do lewej i uzupełnie do brakującej długości spacjami
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^30}")  # "            Tomek             "

print(liczba)  # 678987654123
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 678,987,654,123 , oddziela tysiace
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 678_987_654_123
print(f"Nasza duża liczba {liczba:_}".replace("_", "."))  # Nasza duża liczba 678.987.654.123
print(f"Nasza duża liczba {liczba:_}".replace("_", " "))  # Nasza duża liczba 678 987 654 123

liczba = 15_000_000_000
print(type(liczba))  # <class 'int'>
print(liczba)  # 15000000000
