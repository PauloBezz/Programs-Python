print('-'*20)
print('Pares e ímpares')
print('-'*20)
pares = []
impares = []
nums = []
for i in range(0,20):
    num = int(input(f'Escolha o {i + 1}º número: '))
    nums.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
print(f'Pares:{pares} / Total: {len(pares)}')
print(f'Ímpares:{impares} / Total: {len(impares)}')