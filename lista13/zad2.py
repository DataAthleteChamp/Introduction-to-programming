wielokrotności = list(filter(lambda liczba : 50 > liczba > 0 and (liczba % 3 == 0 or liczba % 5 == 0), [12, 33, 4, 7, 11, 13, 27, 45]))
print(wielokrotności)