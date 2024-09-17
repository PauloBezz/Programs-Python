print('Programa para medir o volume de latas')
rai = float(input('Digite o raio: '))
alt = float(input('Digite a altura: '))
pi = 3.14159 #constante(pi)
vol = (3.14159 * (rai ** 2)) * alt
print('O volume da lata é {} litros.'.format(vol))