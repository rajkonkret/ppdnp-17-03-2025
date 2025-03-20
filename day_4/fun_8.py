def all_params(a, b, /, c=43, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)
all_params(1, 2, 3, 4)
all_params(1, 2, c=3, d=4)


# / oddziela elemnty które muszą być przekane po pozycji od tych ktore moga byc po pozycji lub po nazwie
# all_params(a=1, b=2, c=3, d=4)

def all_params_2(a, b, /, c=43, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{kwargs}")


all_params_2(1, 2, c=9, d=10, a=11)
# a=1, b=2
# c=9, d=10
# {'a': 11}