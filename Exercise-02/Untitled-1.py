print("Program Konversi Panjang dalan Meter ke Berbagai Satuan")
print("")
length = int(input("Masukkan nilai panjang dalam meter: "))
feet = length / 0.3048
print("")
print(length, "m =", length / 1000, "km") #meter ke kilometer
print(length, "m =", length * 100, "cm") #meter ke centimeter
print(length, "m =", length * 1000, "mm") #meter ke milimeter
print(length, "m =", length * 1000000, "μm") #meter ke mikrometer
print(length, "m =", length / 1000, "nm") #meter ke nanometer
#Round berfungsi untuk menghasilkan hasil ke N angka di belakang koma
print(length, "m =", round(feet * 12, 4), "in") #meter ke inchi
print(length, "m =", round(feet, 4), "ft") #meter ke kaki
print(length, "m =", round(feet / 3, 4), "yard") #meter ke yard
print(length, "m =", round(feet / 5280, 4), "mi") #meter ke mil
print(length, "m =", round(feet / 1852, 4), "nmi") #meter ke mil laut