#Harga Tiket Penumpang dan Kendaraan  

Jumlah_Dewasa = int(input("Jumlah Penumpang Dewasa = "))
Jumlah_Anak = int(input ("Jumlah Anak-Anak = "))
Harga_Tiket_Penumpang = Jumlah_Dewasa * 15000 + Jumlah_Anak * 8000
print("Total Harga Tiket Penumpang adalah Rp", round(Harga_Tiket_Penumpang))  

Jenis_Kendaraan = print("Jenis Kendaraan yang dipakai = ")
Jenis_Kendaraan = ["sepeda", "motor", "motor roda 3", "avanza dan sejenisnya", "pick up", "bus sedang",
                    "colt diesel", "bus besar", "truk besar", "tronton", "trailer", "trailer besar"]
Golongan_I = "Sepeda"
Golongan_II = "Sepeda Motor"
Golongan_III = "Motor Roda 3"
Golongan_IVA = "Avanza dan sejenisnya"
Golongan_IVB = "Pick Up"
Golongan_VA = "Bus Sedang < 7m"
Golongan_VB = "Colt Diesel"
Golongan_VIA = "Bus Besar > 7m"
Golongan_VIB = "Truck Besar"
Golongan_VII = "Tronton"
Golongan_VIII = "Trailer"
Golongan_IX = "Trailer Besar"

print(input("Kendaraan masuk dalam golongan = "))



if Jenis_Kendaraan == "sepeda" or "Sepeda" :
    Biaya_Kendaraan = 22000
    print("Kendaraan Anda masuk ke dalam golongan I")
elif Jenis_Kendaraan == "motor" or "Sepeda motor" or "Sepeda Motor" or "sepeda motor":
    Biaya_Kendaraan = 51000
    print("Kendaraan Anda masuk ke dalam golongan II")
elif Jenis_Kendaraan == "Motor Roda 3" or "motor roda 3":
    Biaya_Kendaraan = 114000
    print("Kendaraan Anda masuk ke dalam golongan III")
elif Jenis_Kendaraan[3]:
    Biaya_Kendaraan = 374000
    print("Kendaraan Anda masuk ke dalam golongan IV A")
elif Jenis_Kendaraan[4]:
    Biaya_Kendaraan = 326000
    print("Kendaraan Anda masuk ke dalam golongan IV B")
elif Jenis_Kendaraan[5]:
    Biaya_Kendaraan = 774000
    print("Kendaraan Anda masuk ke dalam golongan V A")
elif Jenis_Kendaraan[6]:
    Biaya_Kendaraan = 645000
    print("Kendaraan Anda masuk ke dalam golongan V B")
elif Jenis_Kendaraan[7]:
    Biaya_Kendaraan = 1301000
    print("Kendaraan Anda masuk ke dalam golongan VI A")
elif Jenis_Kendaraan[8]:
    Biaya_Kendaraan = 998000
    print("Kendaraan Anda masuk ke dalam golongan VI B")
elif Jenis_Kendaraan[9]:
    Biaya_Kendaraan = 1406000
    print("Kendaraan Anda masuk ke dalam golongan VII")
elif Jenis_Kendaraan[10]:
    Biaya_Kendaraan = 2080000
    print("Kendaraan Anda masuk ke dalam golongan VIII")
else:
    Biaya_Kendaraan = 3251000
    print("Kendaraan Anda masuk ke dalam golongan IX")
print("Total Harga Tiket Kendaraan adalah Rp", round(Biaya_Kendaraan))
Total_diBayar = Harga_Tiket_Penumpang + Biaya_Kendaraan
print("Total biaya yang harus dibayar = ", Total_diBayar)

Usia = int(input("Berapa Usia Anda? "))
if Usia >= 18:
    Biaya_Penumpang = 15000
else:
    Biaya_penumpang = 8000
