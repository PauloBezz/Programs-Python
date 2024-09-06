print('-+' * 16)
print('Tabuada de qualquer número')
print('-+' * 16)
continuar = True
n = int(input('Digite um número: '))
for i in range(0,11):
    print(f'{n} x {i} = {n * i}')