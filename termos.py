num = int(input('Digite quantos termos: '))
anterior = 0
atual = 1
print(f'{anterior}, {atual}', end=' ')
cont = 3
while cont <= num:
    proximo = anterior + atual 
    print(f', {proximo}', end=' ')
    anterior = atual 
    atual = proximo
    cont += 1
print('... Fim')