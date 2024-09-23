import array as arr

print('Programa da multiplicação por 3')
print('/*' * 15)
vetorA = arr.array('i', [])
vetorB = arr.array('i', [])
for i in range(8):
    num = int(input(f'Digite o {i + 1}º valor inteiro: '))
    vetorA.append(num)
    multi = num * 3
    vetorB.append(multi)
        
print(vetorA)
print(vetorB)