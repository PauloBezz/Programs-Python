import array as arr
from math import factorial

print('Programa do Fatorial de Matrizes')
print('*/' * 16) 
matrizA = arr.array('i', [])
matrizB =arr.array('i', [])

for i in range(0,15):
    num = int(input(f'Digite o {i + 1}º valor inteiro: '))
    matrizA.append(num) 
    fact = factorial(num)
    matrizB.append(fact)

print(matrizA)
print(matrizB)