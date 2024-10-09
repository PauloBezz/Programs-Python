for i in range(2,102,2):
    print(i)



positivo = 0
media = 0
soma = 0
for i in range(6):
    num = float(input("Diga: "))
    if num > 0:
        positivo += 1
        soma += num
        media = soma / positivo
    else:
        positivo = positivo
print(positivo ,"valores positivos")
print(f"{media:.1f}")



par = 0
imp = 0
pos= 0
neg = 0
for i in range(5):
    num = int(input())
    if num > 0:
        pos += 1
        if num % 2 == 0:
            par += 1
        else:
            imp += 1
    elif num < 0:
        neg += 1
        if num % 2 == 0:
            par += 1
        else:
            imp += 1
    else:
        par += 1
        pos = pos

print(par ,"valor(es) par(es)")
print(imp ,"valor(es) impar(es)")
print(pos ,"valor(es) positivo(s)")
print(neg ,"valor(es) negativo(s)")



pri = int(input())
seg = int(input())
imp = 0

if pri >= seg:
    pri, seg = seg, pri

for i in range (pri + 1, seg):
    if i % 2 != 0:
        imp += i
print(imp)



N = int(input())
dentro = 0
fora = 0
for i in range (N):
    X = int(input())
    if 10 <= X <= 20:
        dentro += 1
    elif X <0:
        fora = fora
    else:
        fora += 1
print(dentro,"in")
print(fora,"out")



N = int(input())
md = 0
cont = 0
resultado = []
for i in range (N):
    N1, N2, N3 = input("").split()
    N1 = float(N1)
    N2 = float(N2)
    N3 = float(N3)
    md = ((N1 * 2) + (N2 * 3) + (N3 * 5)) / 10 
    resultado.append(md) 
for md in resultado:
    print(f"{md:.1f}")



indice = -1
maior = 0
for i in range(100):
    num = int(input())
    if num >= maior:
        maior = num
        indice = i + 1
print(maior)
print(indice)



N = int(input())
coelho = 0
rato = 0
sapo = 0
for i in range(N):
    qtd, tipo = input("").split()
    qtd = int(qtd)
    tipo = str(tipo)
    if tipo == 'C':
        coelho += qtd
    if tipo == 'R':
        rato += qtd
    if tipo == 'S':
        sapo += qtd
    total = coelho + rato + sapo
    perCo = 100 * coelho / total 
    perRa = 100 * rato / total 
    perSa = 100 * sapo / total 
print("Total:",total,"cobaias")
print("Total de coelhos:",coelho)
print("Total de ratos:",rato)
print("Total de sapos:",sapo)
print(f"Percentual de coelhos: {perCo:.2f} %")
print(f"Percentual de ratos: {perRa:.2f} %")
print(f"Percentual de sapos: {perSa:.2f} %")