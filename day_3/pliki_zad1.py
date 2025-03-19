# działąnia z plikami
# filehandler - rura do pliku
# context manager - pomaga w pracy z zasobami np.: pliki
# with - context manager w pythonie

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Powitanie\n")
    fh.write("kolejne\n")

with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Nowe\n")
    fh.write("Nowe\n")
    fh.write("Nowe\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding="utf-8") as fh:
#     fh.write("Nowe\n")
#     fh.write("Nowe\n")
#     fh.write("Nowe\n")

with open("test.log", "a", encoding="utf-8") as fh:
    fh.write("Dopisane\n")
    fh.write("Kolejne\n")
    fh.write("Jescze jedno\n")
    fh.write("Dośdane\n")

with open("test.log", "r", encoding="utf-8") as fh:
    lines = fh.read()

print(lines)
# Nowe
# Nowe
# Nowe
# Dopisane
# Kolejne
# Jescze jedno
