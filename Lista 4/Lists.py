num = int(input("Digite um número: "))
positivo = []

while num > 0:
    positivo.append(num)
    num = int(input("Digite um número: "))
print(positivo)



num = int(input("Digite um número: "))
positivo = []

while num > 0:
    positivo.append(num)
    num = int(input("Digite um número: "))
novo = positivo
for num in novo:
    print(num)



numeros = []
cont = 0
while cont < 10:
    num = int(input(f"Digite {cont + 1}º número: "))
    numeros.insert(0, num)
    cont += 1
print(numeros)



listA = []
listB = []
cont = 0
while cont < 10:
    num = int(input(f"Digite {cont + 1}º número: "))
    listA.append(num)
    cont += 1
    print("ListA",listA)
while cont < 20:
    numb = int(input(f"Digite {cont + 1}º número: "))
    listB.append(numb)
    cont += 1
    print("ListB",listB)
listC = listA + listB
print(listC)