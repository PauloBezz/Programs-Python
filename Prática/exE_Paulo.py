print('Programa para cálculo de juros')
tax = float(input('Digite o valor da taxa mensal: '))
mes = int(input('Digite o número de meses em atraso: '))
parce = float(input('Digite o valor da parcela: '))

prest = parce + (parce * (tax / 100) * mes)
print('A prestação custará {:.2f} reais, devido ao atraso de {} meses.' .format(prest,mes))
print('Valor da taxa: {} %'.format(tax))