plik = open("zad1.txt", "a")

while True:
    tekst = input("Podaj tekst: ")

    if tekst == "":
        break
    else:
        plik.write(f"{tekst}\n")

plik.close()
