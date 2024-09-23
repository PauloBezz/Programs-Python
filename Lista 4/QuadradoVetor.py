import array as arr

print('Programa do quadrado de array')
print('/*' * 15)
vetorA = arr.array('i', [])
vetorB = arr.array('i', [])
for i in range(15):
    num = int(input(f'Digite o {i + 1}º valor inteiro: '))
    vetorA.append(num)
    multi = num ** 2
    vetorB.append(multi)
        
print(vetorA)
print(vetorB)