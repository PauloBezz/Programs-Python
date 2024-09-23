print('-+' * 8)
print('Soma de 1 ao 100')
print('-+' * 8)
grupo = []
for i in range(1,101):
    grupo.append(i)
print(*grupo, end='.' )
print(f'\n A soma resulta em {sum(grupo)}')