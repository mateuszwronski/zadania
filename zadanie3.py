# """
# Zlicz wystąpienia literek w danym tekście. Użyj słownika do przechowywania
# wyniku. Zdefiniuj funkcję, która obliczy wystąpienia i zwróci ten słownik.
# Może Ci się przydać: sprawdzenie czy dana literka jest kluczem w słowniku można
# wykonać w następujący sposób:
#     if 'a' in wystapienia:
# """

# def wystapienia_literek(tekst):
#     wystapienia = dict()
#     # ...
#     return wystapienia


# # oczekiwane wyniki:
# print(wystapienia_literek("mama"))  # {"m": 2, "a": 2}
# print(wystapienia_literek("aamm"))  # {"m": 2, "a": 2}
# print(wystapienia_literek("onomatopeja"))  # {"a": 2, "m": 1, "o": 3, "n": 1, "t": 1, "p": 1, "e": 1, "j": 1}
# print(wystapienia_literek(""))  # {}

def wystapienia_literek(tekst):
    wystapienia = dict()
    x = 1
    for slowo in tekst:
        # Ta petla wypisze slowo z tekstu
        for letter in slowo:
                #Ta petla rozbije slowo na litery
                wystapienia[letter]=x+1
                print (wystapienia) # teraz zadziała, wypisze wynik i zliczy wystąpienia, ale linię 33 muszę przesunąc pod tą pętlę i na koniec wywali błąd.
                # return wystapienia <--- gdy dam return to wykona tylko jedną pętle?!
# print(wystapienia_literek("mama"))  # {"m": 2, "a": 2}
# print(wystapienia_literek("aamm"))  # {"m": 2, "a": 2}
            print(wystapienia_literek("onomatopeja"))  # {"a": 2, "m": 1, "o": 3, "n": 1, "t": 1, "p": 1, "e": 1, "j": 1}
# print(wystapienia_literek(""))  # {}