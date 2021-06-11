'''
    program menampilkan nilai huruf x
    Oleh Korneles Reymundo Lieubun (20083000064)
    kelas 2A
'''
import os
clear = lambda : os.system("cls")
jwb = "y"
while jwb == "y" or jwb == "Y":
    clear()
    print("=============================================")
    print("----- PROGRAM MENAMPILKAN NILAI HURUF X -----")
    print("=============================================")
    print()
    a = input("Masukkan Nilai = ")
    n = int(a)
    if n < 0 or n > 100 :
        sts = "Inputan hanya boleh 0 sampai 100 saja "
    elif n > 91 and n <= 100 :
        sts = "A"
    elif n >= 81 and n < 91 :
        sts = "B"
    elif n >= 71 and n < 81 :
        sts = "C"
    else :
        sts = "D"
    print()
    print(sts)
    print()
    jwb = input("Cek lagi? (Y/T) = ")
    if jwb == "t" or jwb == "T":
        break