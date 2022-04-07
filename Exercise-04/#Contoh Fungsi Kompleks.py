#Contoh Fungsi Kompleks 
#Access, oracle, dll-->tinggal define tabel
from email import header


hewan_peliharaan = ["kucing", 'anjing', 'kura-kura', 'ikan', 'kelinci']

#Fungsi untuk menampilkan data base
def show_data():
    print('Daftar hewan peliharaan ')
    if len(hewan_peliharaan) == 0:
        print("Belum ada data yang masuk")
    else:
        for indeks in range(len(hewan_peliharaan)):
            print('no = ', indeks, "  ", hewan_peliharaan[indeks])

#Fungi untuk menambah anggota data base
def insert_data():
    peliharaan_tambahan = input('Masukkan nama hewan peliharaan = ')
    hewan_peliharaan.append(peliharaan_tambahan)
    show_data

#Fungsi untuk mengedit data base
def edit_data():
    show_data()
    indeks = int(input('masukkan ID hewan peliharaan yang akan diedit = '))
    if (indeks > len(hewan_peliharaan)):
        print('ID tidak ditemukan')
    else:
        peliharaan_baru=input('Nama hewan peliharaan baru = ')
        hewan_peliharaan[indeks] = peliharaan_baru
    show_data

#Fungsi untuk menghapus data base
def delete_data():
    indeks = int(input('masukkan ID hewan peliharaan yang akan dihapus = '))
    if (indeks > len(hewan_peliharaan)):
        print('ID tidak ditemukan')
    else:
        hewan_peliharaan.remove(hewan_peliharaan[indeks])
        show_data()

#Menu Data Base
def menu():
    print('=================================')
    print(' [1] Show data hewan peliharaan')
    print(' [2] Insert data hewan peliharaan')
    print(' [3] Edit data hewan peliharaan')
    print(' [4] Delete data hewan peliharaan')
    print('=================================')

#program utama
print('Selamat Datang di Sistem Informasi Hewan Peliharaan')
print('================================================')
menu()
pilih = int(input('Masukkan pilihan menu = '))
print('================================================')

if pilih==1:
    show_data()
elif pilih==2:
    insert_data()
elif pilih==3:
    edit_data()
elif pilih==4:
    edit_data()
else:
    print('Salah pilih menu')