# powkładaj z listy wartości do odpowiednich "worków"

import random

owoce = ["jablko"] * 4 + ["pomarancz"] * 3 + ["mandarynka"] * 4 + \
        ["gruszka"] * 3 + ["pomidor"] * 4

random.shuffle(owoce)
# print(owoce)


jablka = []
pomarancze = []
mandarynki = []
gruszki = []
pomidory = []

for owoc in owoce:
    if "jablko" in owoc:
        jablka.append(owoc)
    elif "pomarancz" in owoc:
        pomarancze.append(owoc)
    elif "mandarynka" in owoc:
        mandarynki.append(owoc)
    elif "gruszka" in owoc:
        gruszki.append(owoc)
    elif "pomidor" in owoc:
        pomidory.append(owoc)
        

print(jablka)
print(pomarancze)
print(mandarynki)
print(pomidory)