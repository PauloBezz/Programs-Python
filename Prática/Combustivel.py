
print('Programa para calcular o gasto de combustível.')
vm = int(input('Digite a velocidade média: '))
tem = int(input('Digite o tempo em horas: '))

dist = (vm * tem)
print('A velocidade média foi de {} km/h.'.format(vm))
print('O tempo gasto foi de {} horas'.format(tem))
print('A distância percorrida foi de {} km'.format(dist))

lit = dist / 12
print('Você gastou {:.2f} litros de combustível'.format(lit))