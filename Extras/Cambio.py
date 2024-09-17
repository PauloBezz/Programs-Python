print('/*' * 15)
print("Vamos com o real para o mundo!" )
print('/*' * 15)
for i in range(100):
    real = float(input("Digite o valor em real: "))
    print("Dólar: 5.09 \nEuro: 5.56 \nLibra esterlina: 6.32 \nPeso Argentino: 0.024")
    moeda = input("D-Dólar, E-Euro, L-Libra, P-peso, C-Câmbio ou S-Sair: ").upper()
    if moeda == 'D':
        dolar = real * 5.09
        print("{:.2f} reais são {:.2f} dólares.".format(real,dolar))
    elif moeda == 'E':
        euro = real * 5.56
        print("{:.2f} reais são {:.2f} euros.".format(real,euro))
    elif moeda == 'L':
        libra = real * 6.32
        print("{:.2f} reais são {:.2f} libras esterlinas.".format(real,libra))
    elif moeda == 'P':
        peso = real * 0.024
        print("{:.2f} reais são {:.2f} pesos argentinos.".format(real,peso))
    elif moeda == 'C':
        cambio = float(input("Digite a taxa de câmbio"))
        sera = real * cambio
        print("{:.2f} reais são {:.2f} na moeda escolhida.".format(real,sera))
    else:
        moeda == 'S'
        print("Desligando conversor...")
        break