import datetime

class Restauracja:
    def __init__(self, nazwa_restauracji, typ_kuchnii):
        self.nazwa_restauracji = nazwa_restauracji
        self.typ_kuchnii = typ_kuchnii
        self.liczba_klientow = 0

    def opis_restauracji(self):
        opis = (f"-----------------[ Informacja o resturacji {self.nazwa_restauracji} ]-----------------\n"
                f"Restauracja o nazwie {self.nazwa_restauracji} serwuje typ kuchnii: {self.typ_kuchnii}\n"
                f"Aktualna liczba obsłużonych klientów: {self.liczba_klientow}\n"
                f"----------------------------------------------------------------------")
        return opis

    def otwarta_restauracja(self):
        godzina = datetime.datetime.now().hour
        if godzina <= 10:
            return f"Restauracja {self.nazwa_restauracji} jest otwarta od 10:00 do 24:00 każdego dnia tygodnia."
        else:
            return f"Restauracja otwarta, zapraszamy!"

    def ustaw_liczbe_obsluzonych_klietow(self, liczba_klientow):
        self.liczba_klientow = liczba_klientow
        return f"Ustawiono liczbę obsłużonych klientów na {self.liczba_klientow}"

    def dodaj_liczbe_obsluzonych_klientow(self, ile):
        self.liczba_klientow += ile
        return f"Aktualna liczba obsłużonych klientów w {self.nazwa_restauracji}: {self.liczba_klientow}"


class Lodziarnia(Restauracja):
    def __init__(self, nazwa_restauracji, typ_kuchnii):
        super().__init__(nazwa_restauracji, typ_kuchnii)
        self.smaki = ["Czekolada", "Wanilla", "Truskawka"]

    def lista_smakow(self):
        print(f"{self.smaki}")


marbella = Restauracja("Marbella", "włoska")
fairwick = Restauracja("Fairwick", "gruzińska")
oriental = Restauracja("Oriental", "azjatycka")

print(marbella.nazwa_restauracji)
print(marbella.typ_kuchnii)

print(fairwick.nazwa_restauracji)
print(fairwick.typ_kuchnii)

print(oriental.nazwa_restauracji)
print(oriental.typ_kuchnii)

print(marbella.opis_restauracji())
print(marbella.otwarta_restauracja())
print(marbella.ustaw_liczbe_obsluzonych_klietow(100))
print(marbella.dodaj_liczbe_obsluzonych_klientow(20))

print(fairwick.opis_restauracji())
print(fairwick.otwarta_restauracja())
print(fairwick.ustaw_liczbe_obsluzonych_klietow(50))
print(fairwick.dodaj_liczbe_obsluzonych_klientow(10))

print(oriental.opis_restauracji())
print(oriental.otwarta_restauracja())
print(oriental.ustaw_liczbe_obsluzonych_klietow(80))
print(oriental.dodaj_liczbe_obsluzonych_klientow(20))

lodziarnia = Lodziarnia("Lodziarnia", "lody")
lodziarnia.lista_smakow()
