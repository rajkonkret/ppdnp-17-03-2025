# stworzyc funkcję obliczającą średnia
# * worek na dane, dowolna liczba danych po pozycji
def liczby(name=None, *cyfry):
    print(cyfry)
    count = len(cyfry)
    suma = 0
    # avg = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Koniec")


liczby(1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
liczby(1, 2, 3, 4, 5, 6, 89, 90)
# (1, 2, 3, 4, 5, 6, 89, 90)
liczby()
liczby("Radek", 5, 4, 5, 6, 5, 4, 4)
# (5, 4, 5, 6, 5, 4, 4)
# Średnia dla ucznia Radek wynosi 4.714285714285714
# Koniec
