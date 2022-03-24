#Pangkat
from re import X

#menghitung pangkat
print("==========================")
angka = int(input("Masukkan nilai angka dasar = "))
pangkat = int(input("Masukkan nilai pangkat = "))
y = 1
#proses looping
while pangkat != 0:
    y = y * angka
    pangkat = pangkat-1
print("==========================")    
print("Hasil perpangkatan yaitu =", y)