# ** dowolna ilosc elemento po nazwie, dane słownikowe
def connect(**opcje):
    print(opcje)


connect(a=10)  # {'a': 10}
connect(a=10, c=90, name="Radek")  # {'a': 10, 'c': 90, 'name': 'Radek'}


def all_arg(*args, **kwargs):
    print(args, kwargs)


all_arg(1, 2, 3, 4)
all_arg(1, 2, 3, 4, a=0, b=89, name="radek")
all_arg(a=10)
# (1, 2, 3, 4) {}
# (1, 2, 3, 4) {'a': 0, 'b': 89, 'name': 'radek'}
# () {'a': 10}
