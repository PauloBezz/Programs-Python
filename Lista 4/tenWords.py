import array

print('Programa para ler 10 palavras')
print('/*' * 15)
namae = []

for i in range(10):
    nome = input(f'Escreva a {i+1}º palavra: ')
    namae.append(nome)
    
print(*namae, sep = ' ')