'''
program cek kelulusan 
dibuat tgl 
Korneles Reymundo Lieubun(20083000064)
kelas 2C
'''
import os
clear = lambda : os.system('cls')
jwb = "y"
while jwb == "Y" or jwb == "y" :
    clear()
    print("---------------------")
    print("PROGRAM CEK KELULUSAN")
    print("---------------------")
    print()
    a = input("Masukkan Nilai = ")
    n = int(a)
    if n < 0 or n > 100 :
        sts = "Inputan hanya boleh 0 sampai 100 saja"
    elif n > 60 :
        sts = "LULUS"
    else :
        sts = "TIDAK LULUS"
    print()
    print(sts)
    print()
    jwb = input("Cek lagi? (y/t) : ")
    if jwb == "t" or jwb == "T":
        break
