import chardet

# pip install chardet
with open('test.log', "r", encoding="utf-8") as f:
    raw_data = f.read()

print(raw_data)

# biblioteka chardet wymaga by otworzyc plik do odczytu bajtowo
with open('test.log', "rb") as f:
    raw_data = f.read()

print(raw_data)
# b'Nowe\r\nNowe\r\nNowe\r\nDopisane\r\nKolejne\r\nJescze jedno\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding'', 'confidence': 0.6271830985915493, 'language': ''}
# pozwiekszeniu ilości polskich liter, wykrywa utf-8
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print(encoding)  # utf-8
print(raw_data.decode(encoding=encoding))
# Nowe
# Nowe
# Nowe
# Dopisane
# Kolejne
# Jescze jedno
# Dośdane
# Dośdążćane
