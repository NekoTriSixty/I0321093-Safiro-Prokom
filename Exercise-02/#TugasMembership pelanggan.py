#Tugas
#Membership perbelanjaan dan penghitungan discount bagi member

print("====Total Biaya Pembayaran 'PetraMart'====")
print("==========================================")
membership = (input("Apakah pelanggan adalah member 'PetraMart'? "))
total_belanja = int(input("Silahkan masukkan total belanja pelanggan = Rp "))

if membership == "ya":
    if total_belanja >= 500000:
        diskon = total_belanja * 25 / 100
        print("Selamat, Anda mendapatkan potongan harga sebesar Rp", round(diskon))
        total_belanja = total_belanja - diskon
        print("==========================================")   
        print("Total harga yang harus dibayar = Rp",round(total_belanja))
    elif total_belanja >= 100000:
        diskon = total_belanja * 20 / 100
        print("Selamat, Anda mendapatkan potongan harga sebesar Rp", round(diskon))
        total_belanja = total_belanja - diskon
        print("==========================================")   
        print("Total harga yang harus dibayar = Rp",round(total_belanja))
    else:
        diskon = total_belanja * 10 / 100
        print("Selamat, Anda mendapatkan potongan harga sebesar Rp", round(diskon))
        total_belanja = total_belanja - diskon
        print("==========================================")   
        print("Total harga yang harus dibayar = Rp",round(total_belanja))        
else:
    if total_belanja >= 100000:
        diskon = total_belanja * 10 / 100
        print("Selamat, Anda mendapatkan potongan harga sebesar Rp", round(diskon))
        total_belanja = total_belanja - diskon
        print("==========================================")   
        print("Total harga yang harus dibayar = Rp",round(total_belanja))
    else:
        print("==========================================")   
        print("Total harga yang harus dibayar = Rp",round(total_belanja))
print("==========================================")        
print("Terima Kasih Telah Berbelanja di PetraMart")                