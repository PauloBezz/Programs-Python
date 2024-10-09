import numpy as np

print('Programa da Concatenação de Matrizes')
print('*/' * 16) 


matrizA = np.array([4, 5, 6, 7, 4, 4, 2, 5, 4, 3, 4, 3, 5, 2, 4])
matrizB = np.array([6, 7, 4, 3, 5, 7, 9, 0, 3, 2, 4, 4, 6, 4, 5])


result = np.concatenate((matrizA, matrizB))
print(matrizA)
print(matrizB)
print(result)
print(sorted(result))