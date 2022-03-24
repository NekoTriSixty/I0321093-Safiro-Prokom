#faktorial

n = int(input('Masukkan nilai n: '))
Y = 1

for i in range(1, n + 1):
  Y *= i

print(f'{n}! = {Y}')
