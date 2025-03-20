# stworzyc funkcje kantor
# dwie funkcje wew usd, eur
# w zalezności od od parametru ma zwrocic jedną z tych funkcji


def kantor(waluta):
    def usd(kwota=0):
        print("Wymieniam usd:", kwota)

    def eur(kwota=0):
        print("Wymieniam euro:", kwota)

    if waluta == "usd":
        return usd
    else:
        return eur


kantor_eur = kantor("eur")
kantor_eur(1000)  # Wymieniam euro: 1000

kantor_usd = kantor("usd")
kantor_usd(500)  # Wymieniam usd: 500
kantor_usd()  # Wymieniam usd: 0
