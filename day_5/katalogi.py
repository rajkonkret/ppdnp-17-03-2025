import os.path
import shutil
from pathlib import Path

base_path = Path('ops_example')

print(base_path)
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

base_path.mkdir()  # Process finished with exit code 0

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'
# nie ma katalogu A, nie potrafi stworzyc zagnieżdzonych
# path_b.mkdir()
path_b.mkdir(parents=True)  # tworzy całe drzewo katalogów
path_c.mkdir()  # katalog A juz istnieje, stworzy katalog C

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding='utf-8') as stream:
        stream.write(f"Jakaś treść pliku {filename}")

# przeniesienie katalogu
shutil.move(path_b, path_d)

# zmiana nazwy pliku
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / "ex1renamed.log")

# kopia pliku
ex1 = path_d / "ex1renamed.log"
docelowy = path_c
shutil.copy(ex1, docelowy)

print(ex1.resolve())
# C:\Users\CSComarch\PycharmProjects\ppdnp-17-03-2025\day_5\ops_example\A\D\ex1renamed.log

print(os.path.abspath(ex1))
# C:\Users\CSComarch\PycharmProjects\ppdnp-17-03-2025\day_5\ops_example\A\D\ex1renamed.log

# bieżący katalog
print(os.getcwd())
# C:\Users\CSComarch\PycharmProjects\ppdnp-17-03-2025\day_5
