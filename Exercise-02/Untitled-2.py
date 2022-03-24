total_belanja = int(input("berapa nilai pembelian anda?= Rp "))

if total_belanja >= 100000:
    print("Selamat pelanggan mendapatkan discount 10%")
    potongan = total_belanja*10/100
    total_belanja = total_belanja-potongan
print("Total membayar pelanggan sebanyak ", round(total_belanja) )
