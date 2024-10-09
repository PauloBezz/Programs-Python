# Exemplo 1

lista = []
for i in range(10):
    element = input(f"Digite {i + 1}º elemento: ")
    lista.append(element)

for element in lista:
    print(element)

# Exemplo 2

lista = []
for i in range(10):
    element = input(f"Digite {i + 1}º elemento: ")
    lista.insert(0, element)

for element in lista:
    print(element)

# Exercício 3
N = int(input("Quantas as vezes: "))
lista = []
if N > 0 and N < 50:
    for i in range(N):
        num = float(input(f"Digite {i + 1}º  número real: "))
        lista.append(num)
    for num in lista:
        print(num)
else:
    print('Fim do programa')

# Exercício 4
from random import randint
N = int(input("Quantas as vezes: "))
lista = []
if N > 0 and N < 50:
    for i in range(N):
        num = randint(0, 1000)
        lista.append(num)
    for num in lista:
        print(num)
else:
    print('Fim do programa')

# Exercício 5
A = []
NEG = []
POS = []
N = int(input("Quantas vezes: "))
while N > 0 and N < 50:
    for i in range(N):
        num = float(input(f"Digite {i + 1}º  número real: "))
        A.append(num)
        if num >= 0:
                POS.append(num)
        else:
                NEG.append(num)
    print(f"{NEG} contém {len(NEG)} negativos" )
    print(f"{POS} contém {len(POS)} positivos" )
    A = []
    POS = []
    NEG = []
    N = int(input("Quantas vezes: "))
print('Fim do programa')

#Exercício 6
LMin = int(input("Início: "))
LMax = int(input("Final: "))
A = []

if LMax < LMin:
    LMax, LMin = LMin, LMax

for i in range(4):
    num = int(input(f"Digite {i + 1}º valor: "))
    if num >= LMin and num <= LMax:
        A.append(num)
    else:
        print(A)
print(A)
print(LMin)
print(LMax)

#Exercício 7
LMin = int(input("Início: "))
LMax = int(input("Final: "))
qtd = int(input("Quantas números? "))
A = []

if LMax < LMin:
    LMax, LMin = LMin, LMax

for i in range(qtd):
    num = int(input(f"Digite {i + 1}º valor: "))
    if num >= LMin and num <= LMax:
        A.append(num)
    else:
        print(A)
print(A)
print(LMin)
print(LMax)

#Exercício 8
LMin = int(input("Início: "))
LMax = int(input("Final: "))
qtd = int(input("Quantas números? "))
A = []
R = []

if LMax < LMin:
    LMax, LMin = LMin, LMax

for i in range(qtd):
    num = int(input(f"Digite {i + 1}º valor: "))
    if num >= LMin and num <= LMax:
        A.append(num)
    else:
        R.append(num)
print(A)
print(R)