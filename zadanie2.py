# Dla podanych liczb, oblicz:
# 1. średnią arytmetyczną (https://pl.wikipedia.org/wiki/%C5%9Arednia_arytmetyczna)
# 2. średnią geometryczną (https://pl.wikipedia.org/wiki/%C5%9Arednia_geometryczna)
# 3. średnią harmoniczną (https://pl.wikipedia.org/wiki/%C5%9Arednia_harmoniczna)
# 4. średnią kwadratową (https://pl.wikipedia.org/wiki/%C5%9Arednia_kwadratowa)
# Zadanie dodatkowe: oblicz średnią ważoną dla podanych wag. Możesz wykorzystać
# funkcję zip(): https://docs.python.org/3/library/functions.html#zip
# Oczekiwane wyniki:
# średnia arytmetyczna:   5.133333333333334
# średnia geometryczna:   38.041931258128585
# średnia harmoniczna:    166.87719921937406
# średnia kwadratowa:     58.18762755088061
# średnia ważona:         8.571428571428571
# """

# wartosci = [-24, 70, -88, 12, -4, -33, -33, -75, 84, 67, -98, 97, 40, 79, 7,
#             -30, 17, -50, 4, -60, -26, -69, 71, 80, 30, -66, 88, 26, 60, -22]

# wagi = [4, 4, 3, 1, 2, 4, 2, 1, 5, 5, 5, 1, 1, 2, 5, 1, 1, 2, 1, 5, 5, 3, 2,
#         5, 4, 1, 5, 5, 3, 3]

wartosci = [-24, 70, -88, 12, -4, -33, -33, -75, 84, 67, -98, 97, 40, 79, 7,
            -30, 17, -50, 4, -60, -26, -69, 71, 80, 30, -66, 88, 26, 60, -22]

wagi = [4, 4, 3, 1, 2, 4, 2, 1, 5, 5, 5, 1, 1, 2, 5, 1, 1, 2, 1, 5, 5, 3, 2,
        5, 4, 1, 5, 5, 3, 3]

# średnia arytmetyczna
a = (sum(wartosci))
b = (len(wartosci))
wynik = a / b
print(wynik)


# Pozostałe zadania wyrywają mi włosy z głowy. Nadal nie rozumiem jak przełożyć wzór matematyczny na kod w pętli.
# Czekam na rozwiązanie w/w zadań, fajnie jakbyś opisał krok po kroku co dana linia kodu powoduje.