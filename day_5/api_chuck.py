import requests

# pip install requests
url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx warningi, przekierowania
# 4xx 404 - brak zasobu, 400 Bad Request - bład w zapytaniu
# 5xx - bład serwera
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

data = response.text
print(data)
print(type(data))  # <class 'str'>

data = response.json()  # tworzenie słownika z jsona
print(data)
# {'categories': [], 'created_at': '2020-01-05 13:42:30.730109',
#  'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png',
#  'id': 'kNklS3PRQ-y-ZviDofGdIA',
#  'updated_at': '2020-01-05 13:42:30.730109',
#  'url': 'https://api.chucknorris.io/jokes/kNklS3PRQ-y-ZviDofGdIA',
#  'value': 'Chuck Norris makes a line have to shit'}

# wszystkie klucze
print(data.keys())
# dict_keys(['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])

for k in data:
    print(k)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(data["value"])
# Chuck Norris is shit... but nothing like Jacksonnn !!!!!!!!!!!!!! Ownedddddd

url_icon = data['icon_url']
response_img = requests.get(url_icon)
with open('icon.jpg', "wb") as f:
    f.write(response_img.content)

print("Zdjęcie zapisane")
