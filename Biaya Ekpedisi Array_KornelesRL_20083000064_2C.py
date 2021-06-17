import os
clear = lambda : os.system('cls')
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    Kota  = ['Surabaya','Bandung']
    Jarak = ['269','452']
    Ongkirperkm = ['2500','4000']
    b = "t"
    while b == "t"  or b == "T" :
        clear()
        print("-------------------------")
        print("TRANSAKSI EKSPEDISI")
        print("-------------------------")
        print("PILIH KOTA")
        print("Kota 0 = Surabaya")
        print("Kota 1 = Bandung ")
        print('-------------------------')
        print('>> 1 = ',Kota[0],'Jarak= ',Jarak[0],'Ongkir perKM= ',Ongkirperkm[0])
        print('>> 2 = ',Kota[1],'Jarak= ',Jarak[1],'Ongkir perKM= ',Ongkirperkm[1])
        pil = int(input('input pilihan kota= '))
        b = input('Transaksi? (y/t) : ')
        if b == 'Y' or b == 'Y' :
            break
    idx = 0
    while idx >=0 and idx < 2 :
        idx = idx + 1
        if idx == 0 :
            pil = 1
            break
        else:
            idx = pil - 1
            break 
    Ongkir = Jarak[idx]*Ongkirperkm[idx]
    print('=======================================')
    print('>> Kota       =  ', Kota[idx])
    print('>> Jarak      =  ', Jarak[idx],'km')
    print('>> ongkir/km  =  ',format(Ongkirperkm[idx],',2f'))
    print('=======================================')
    print('>>  Total Harga  =  ',format(Ongkir,', 2f'))
    print('=======================================')
    jwb = input('Beli Lagi? (y/t)  : ')
    if jwb == 't' or  jwb == 'T' :
        break
