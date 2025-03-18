# wyjątki - błędy podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-17-03-2025\day_2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

lista = []
try:
    # print(5 / 0)
    # print("A" * "23")
    # print(int("A"))
    # print(lista[10])
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # wykona się tylko gdy nie ma błędu
    print("Wynik:", wynik)
finally:
    print("Wykona się zawsze")

print("Dalsza częśc programu")
# Nie dziel przez zero
# Dalsza częśc programu
# Błąd typu
# Dalsza częśc programu
# Bład list index out of range
# Dalsza częśc programu
# Wynik: 2.727272727272727
# Dalsza częśc programu
