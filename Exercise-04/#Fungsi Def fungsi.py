#Fungsi Def fungsi

def luas_alas(sisi):
    luas = sisi**2
    print('Luas alas = ', luas)
    return(luas)
def volume(sisi): 
    volume = luas_alas(sisi)*sisi
    print('Volume kubus = ', volume)
    return(volume)
def menu():
    print(" (1) luas bujur sangkar")
    print(" (2) Volume Kubus")

#Program Utama

print('Selamat datang di program matematika')
menu()
pilih = int(input("masukkan pilihan menu = "))
sisi=int(input('Masukkan besaran sisi kubus = '))
print('='*40)
if pilih == 1:
    luas_alas(sisi)
else:
    volume(sisi)
    