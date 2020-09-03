from random import randint
#~~~~Oyun random  vaitesiyle bir reqem cixarir. Oyuncu bu reqemi
#~~~~6 gedise tapmalidir.
#~~~~Eyer texmin randomdan yuxari olsa asagi reqem yazilmali oldugu xeberdar edilir.
#~~~~asagi ldugda ise eksine.

on_off = True   # oyunun on ve off olmagini texmin edir.

while on_off:
    tesadufi_reqek = randint(1,100)
    gedis = 6    # istifadece 6 gedise duzgun cavab vermelidir.
    while True:
        #her sehv gedisden 1 say cixir, eyer 0 dan yuxari olarasa oyn davam edir.
        if gedis > 0:
            sorgu = int(input("Reqem daxil ele: "))
        else:
            print("Oyun bitdi. Dzugun cavab {}".format(tesadufi_reqek))
            break
        # Texmin ve random ust uste gelmese awagidaki hisse iwe dusur. ve istifadeciye komek olur
        if tesadufi_reqek != sorgu:
            gedis -= 1
            if sorgu > tesadufi_reqek:
                print("Kicik reqem texmin etmelisen! Qalan gedis {}".format(gedis))
            else:
                print("Boyuk reqem texmin etmelisen! Qalan gedis {}".format(gedis))
        else:
            print("Tebrikler ! Dogru cavab {}".format(tesadufi_reqek))
            break
    # Yeni merhele ucun soru. Istifadeci secim ile davam ede ve ya oyunu bitire biler.
    yeni_merhele = input("Oyun bitdi yeni oyun baslasin? B/X")
    if yeni_merhele == "X":
        on_off = False
        print("Oyun Bitdi!")
        break
    elif yeni_merhele == "B":
        on_off = True
        print("............................Basladiq............................")
    else:
        print("Yanlis secim etdiniz. Oyun bitdi!")
        on_off=False

