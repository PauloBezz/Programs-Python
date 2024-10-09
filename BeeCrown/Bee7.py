cont = 0
soma = 0
while cont < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        soma += nota
        cont += 1
    if nota < 0:
        print("nota invalida")
md = soma / 2
print(f"media = {md:.2f}")




X,Y = input().split()
X = int(X)
Y = int(Y)
while X != Y:
    if X < Y:
        print("Crescente")
    else:
        print("Decrescente")
    X,Y = input().split()
    X = int(X)
    Y = int(Y)



senha = int(input())
while senha != 2002:
    print("Senha Invalida")
    senha = int(input())
print("Acesso Permitido")




N = int(input())
for i in range(N):
    num = i + 1
    dobro = num * num
    triplo = num * num * num
    print(num,dobro,triplo)
    print(num,dobro + 1,triplo+1)




N = int(input())
for i in range(N):
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    if X > Y:
        aux = X
        X = Y
        Y = aux

    soma = 0
    for j in range(X + 1,Y):
        if j % 2 != 0 : 
            soma += j
    print(soma)
        



X , Y = input().split()
X = int(X)
Y = int(Y)
while X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print("primeiro")
    elif X < 0 and Y > 0:
        print("segundo")
    elif X > 0 and Y < 0:
        print("quarto")
    else:
        print("terceiro")
    X , Y = input().split()
    X = int(X)
    Y = int(Y)



cont = 0
soma = 0
while cont < 2:
    nota = float(input())
    if 0 <= nota and nota <= 10:
        soma += nota
        cont += 1
    if nota < 0:
        print("nota invalida")
md = soma / 2
print(f"media = {md:.2f}")

N = 1
while N != 2 and N == 1:
    soma = 0
    cont = 0
    while cont < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            soma += nota
            cont += 1
        else:
            print("nota invalida")

        md = soma / 2
    print(f"media = {md:.2f}")

    print("novo calculo (1-sim 2-nao)")
    N = int(input())

    while N < 1 or N > 2:
        print("novo calculo (1-sim 2-nao)")
        N = int(input())


M,N = input().split()
M = int(M)
N = int(N)
while M > 0 and N > 0:
    if M > N:
        aux = M
        M = N
        N = aux

    soma = 0
    for j in range(M,N + 1):
        soma += j 
        print(j, end=" ")
    print(f"Sum={soma}")

    M,N = input().split()
    M = int(M)
    N = int(N)