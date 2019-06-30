# Wykorzystując pętlę FOR wypisz liczby od 10 do 30 (włącznie), ich kwadraty
# i pierwiastki.
# Przy wypisywaniu użyj formatu:
# {liczba}: {kwadrat} {pierwiastek}
# (klamry oznaczają wypisanie wartości, np. zmiennej)
# Użyj:
# 1. Pętli FOR
# 2. Instrukcji range()
# 3. Operatora **
# Uwaga: od wersji v3.6 Python wspiera tzw. f-stringi, które pozwalają na
# bezpośrednie wstawianie zmiennych do stringów. żeby ich użyć należy "zwykły"
# string poprzedzić literką "f", a wewnątrz napisać w klamrach nazwę zmiennej.
# Przykład pod tym tekstem:
# """
# # liczba = 12
# # print(f"{liczba}")

########### 

import math

liczby = range(10, 31)
for liczba in liczby:
    if liczba >= 10:
        print(liczba, liczba**2, math.sqrt(liczba))
    elif liczba % 3 == 0:
        print(liczba, "jest podzielna przez 3")
