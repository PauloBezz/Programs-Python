print('Programa de troca dos valores')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
aux = a
a = b
b = aux
print(' A -> entrou {} e saiu {}.' .format(b,a))
print(' B -> entrou {} e saiu {}.' .format(a,b))