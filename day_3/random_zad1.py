import random

# operacje na liczbach losowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99, z prawej otwarty
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # float 0.12935079192306997 od 0 do 0.9999999
print(random.random() * 7)  # float 5.467984313184935 od 0 do 6.9999999

lista = ["Radek", "Tomek", 'Zenek', "Anna", "Sylwia", "Marek"]
print(random.choice(lista))  # Marek

# lista, range, choice, remove
lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [18, 24, 29, 5, 24, 43], z powtózeniami
print(random.sample(lista_kule, k=6))  # [25, 28, 40, 9, 13, 45], bez powtórzen
print(random.sample(lista_kule, 6))  # [33, 22, 27, 39, 32, 23], bez powtórzen
