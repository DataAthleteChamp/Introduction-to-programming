class Uzytkownik:
    def __init__(self, imie, nazwisko, pseudonim, email, nr_telefonu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.proby_logowania = 0
        self.pseudonim = pseudonim
        self.email = email
        self.nr_telefonu = nr_telefonu

    def opisz_uzytkownika(self):
        opis = f"Imie: {self.imie}\n" \
               f"Nazwisko: {self.nazwisko}\n" \
               f"Próby logowania: {self.proby_logowania}\n" \
               f"Pseudonim: {self.pseudonim}\n" \
               f"Email: {self.email}\n" \
               f"Numer telefonu: {self.nr_telefonu}"
        print(opis)

    def pozdrow_uzytkownika(self):
        print(f"Serdeczne pozdrowienia dla {self.imie} {self.nazwisko}!")

    def dodaj_probe_logowania(self):
        self.proby_logowania += 1

    def resetuj_proby_logowania(self):
        self.proby_logowania = 0


class Admin(Uzytkownik):
    def __init__(self, imie, nazwisko, pseudonim, email, nr_telefonu):
        super().__init__(imie, nazwisko, pseudonim, email, nr_telefonu)
        self.przywileje = Przywileje()


class Przywileje:
    def __init__(self):
        self.przywiele = ["może dodać post", "może usunąć post", "możę zablokować użytkownika"]

    def pokaz_przywileje(self):
        print(f"Ten admin ma następujące przywileje: {self.przywiele}")


uzytkownik1 = Uzytkownik("Jakub", "Piotrowski", "dilbert", "dilbert@gmail.com", "123456789")
uzytkownik1.opisz_uzytkownika()
uzytkownik1.pozdrow_uzytkownika()
uzytkownik1.dodaj_probe_logowania()
print(f"Ilość prób logowania użytkownika {uzytkownik1.imie} {uzytkownik1.nazwisko}: {uzytkownik1.proby_logowania}")
uzytkownik1.resetuj_proby_logowania()
print(f"Ilość prób logowania użytkownika {uzytkownik1.imie} {uzytkownik1.nazwisko}: {uzytkownik1.proby_logowania}")

uzytkownik2 = Uzytkownik("łukasz", "Duży", "olbrzym", "olbrzym@gmail.com", "123456789")
uzytkownik2.dodaj_probe_logowania()
uzytkownik2.dodaj_probe_logowania()
uzytkownik2.dodaj_probe_logowania()
print(f"Ilość prób logowania użytkownika {uzytkownik2.imie} {uzytkownik2.nazwisko}: {uzytkownik2.proby_logowania}")
uzytkownik2.resetuj_proby_logowania()
print(f"Ilość prób logowania użytkownika {uzytkownik2.imie} {uzytkownik2.nazwisko}: {uzytkownik2.proby_logowania}")

admin = Admin("Jakub", "Piotrowski", "dilbert", "dilbert@gmail.com", "123456789")
admin.przywileje.pokaz_przywileje()
