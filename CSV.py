import csv

# with open('przykladowy.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open('przykladowy.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"{row['Year']}\t{row['Score']}\t\"{row['Title']}\"")

baza = []

with open('przykladowy.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(f"{row['Year']}\t{row['Score']}\t\"{row['Title']}\"")
        baza.append(
            {
                'year': int(row['Year']),
                'score': int(row['Score']),
                'title': row['Title'],
                'czy_po_angielsku': True
                }
        )

#######

maks_poz = 0
maks = baza[maks_poz]['score']

for indeks, liczba in enumerate(baza):
    if liczba['score'] > maks:
        maks = liczba['score']
        maks_poz = indeks

print(baza[maks_poz])

minimum_poz = 0
minimum = baza[minimum_poz]['score']

for indeks, liczba in enumerate(baza):
    if liczba['score'] < minimum:
        minimum = liczba['score']
        minimum_poz = indeks

print(baza[minimum_poz])