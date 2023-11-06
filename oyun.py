import random

def tahta_goster(tahta):
    for row in tahta:
        print(" | ".join(row))
        print("-" * 9)

def kazanan(tahta, oyuncu):
    # Satır ve sütunları kontrol et
    for i in range(3):
        if all([tahta[i][j] == oyuncu for j in range(3)]) or all([tahta[j][i] == oyuncu for j in range(3)]):
            return True

    # Köşegenleri kontrol et
    if tahta[0][0] == tahta[1][1] == tahta[2][2] == oyuncu or tahta[0][2] == tahta[1][1] == tahta[2][0] == oyuncu:
        return True

    return False

def berabere(tahta):
    return all(tahta[i][j] != ' ' for i in range(3) for j in range(3))

def minmax(tahta, derinlik, maksimum):
    oyuncu = 'X' if maksimum else 'O'
    
    if kazanan(tahta, 'X'):
        return 1
    if kazanan(tahta, 'O'):
        return -1
    if berabere(tahta):
        return 0

    if maksimum:
        en_iyi_deger = -float('inf')
        for i in range(3):
            for j in range(3):
                if tahta[i][j] == ' ':
                    tahta[i][j] = 'X'
                    deger = minmax(tahta, derinlik + 1, False)
                    tahta[i][j] = ' '
                    en_iyi_deger = max(en_iyi_deger, deger)
        return en_iyi_deger
    else:
        en_iyi_deger = float('inf')
        for i in range(3):
            for j in range(3):
                if tahta[i][j] == ' ':
                    tahta[i][j] = 'O'
                    deger = minmax(tahta, derinlik + 1, True)
                    tahta[i][j] = ' '
                    en_iyi_deger = min(en_iyi_deger, deger)
        return en_iyi_deger

def bilgisayar_hamlesi(tahta):
    en_iyi_hamle = None
    en_iyi_deger = -float('inf')
    for i in range(3):
        for j in range(3):
            if tahta[i][j] == ' ':
                tahta[i][j] = 'X'
                deger = minmax(tahta, 0, False)
                tahta[i][j] = ' '
                if deger > en_iyi_deger:
                    en_iyi_deger = deger
                    en_iyi_hamle = (i, j)
    
    satir, sutun = en_iyi_hamle
    tahta[satir][sutun] = 'X'
    print(f"Bilgisayarın hamlesi: Satır {satir}, Sütun {sutun} (X)")

def insan_hamlesi(tahta):
    while True:
        satir = int(input("Satır seçin (0, 1, 2): "))
        sutun = int(input("Sütun seçin (0, 1, 2): "))
        if tahta[satir][sutun] == ' ':
            tahta[satir][sutun] = 'O'
            break
        else:
            print("Bu hücre dolu, lütfen başka bir hücre seçin.")

def oyun():
    tahta = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        tahta_goster(tahta)
        insan_hamlesi(tahta)
        if kazanan(tahta, 'O'):
            tahta_goster(tahta)
            print("Tebrikler, insan kazandı!")
            break
        if berabere(tahta):
            tahta_goster(tahta)
            print("Berabere!")
            break

        bilgisayar_hamlesi(tahta)
        if kazanan(tahta, 'X'):
            tahta_goster(tahta)
            print("Bilgisayar kazandı!")
            break
        if berabere(tahta):
            tahta_goster(tahta)
            print("Berabere!")
            break

if __name__ == "__main__":
    oyun()
