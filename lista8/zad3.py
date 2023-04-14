wiersze = []

try:
    plik = open("zad1.txt")
except FileNotFoundError:
    print("Plik nie istnieje!")
else:
    wiersze = plik.readlines()

    tekst = ""
    for wiersz in wiersze:
        tekst += wiersz.strip()

    print(tekst)
    print(f"Tekst ma {len(tekst)} znaków")

    fraza = input("Podaj fraze: ")
    if fraza in tekst:
        print(f"Podana fraza: {fraza}, znajduje sie w pliku tekstowym")
    else:
        print(f"Podana fraza: {fraza}, NIE znajduje sie w pliku tekstowym")
