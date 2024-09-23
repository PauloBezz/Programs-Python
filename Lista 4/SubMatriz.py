import array as arr

print('Programa da Subtração de Matrizes')
print('*/' * 16) 
matrizA = arr.array('i', [])
matrizB = arr.array('i', [])
matrizC =arr.array('i', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# vamos percorrer as matrizes A e B  e somar cada elemento correspondente 
for i in range(0, 20):
    num = int(input(f'Digite o {i + 1}º valor inteiro: '))
    matrizA.append(num)
    
for i in range(0, 20):
    numb = int(input(f'Digite o {i + 1}º valor inteiro: '))
    matrizB.append(numb)
        
for i in range(len(matrizA)):
        matrizC[i] = matrizA[i] - matrizB[i]

print(matrizA)
print(matrizB)
print(matrizC)