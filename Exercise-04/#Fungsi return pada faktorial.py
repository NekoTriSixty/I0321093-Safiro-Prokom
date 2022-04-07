#Fungsi return
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

nilai = int(input('Masukkan nilai untuk difaktorialkan = '))
print('='*50)
print('nilai faktorial dari ', nilai, 'adalah = ', faktorial(nilai))
print('='*50)       