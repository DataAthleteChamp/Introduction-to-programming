import math

def normalize(tablica):

    suma_kwadratów = 0
    kopia=[]

    for n in tablica:
        suma_kwadratów += n**2

    for n in range(0,len(tablica)):
        tablica[n] = tablica[n] / math.sqrt(suma_kwadratów)

    for n in tablica:
        kopia.append("%.5f" %n)

    print(kopia)

normalize([2.2, 5.6, 4.3, 3.0, 0.5])


# dla 2 liczb w tablicy [n1 / sqrt(n1**2 + n2**2)] * [n2 / sqrt(n1**2 + n2**2)] = 1