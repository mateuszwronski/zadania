# narysuj tabliczkę mnożenia
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16
# itd.
# postaraj się ładnie to wyświetlać
# użyj znaku "\t" do wyświetlania tabulatora

# print('Co mnożymy?')
# x = input()
# print('Przez ile mnożymy?')
# y = input()
# xi = int(x)
# yi = int(y)
# z = xi * yi
# print(z)

pierwsze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for liczba in pierwsze:
    # print(liczba)
    for liczba2 in pierwsze:
        print(liczba * liczba2, end='\t')
    print()
