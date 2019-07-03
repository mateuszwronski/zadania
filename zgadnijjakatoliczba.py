import random
print("Zagrajmy w grę, jaką? TumbRajder zgadnij jaka ta liczba?")
print("masz tylko 7 szans, nie zmarnuj ich")
liczba = random.randint(0,101)
proba = 1

zgadl = False
while not zgadl:
    zgadywana = int(input("Podaj liczbe: "))
    proba =+ proba + 1
    # pass
    if zgadywana == liczba:
        zgadl = True
        print("Dobrze!")
    elif proba == 8:
        print("No, no... 7 razy strzelać i nie trafić... Jesteś godnym następcą Milika")
        break
    elif zgadywana < liczba:
        print("Za mało, mierz wyżej!")
    elif zgadywana > liczba:
        print("Ale Cię poniosło! Obniż loty!")
