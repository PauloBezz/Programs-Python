print("-/" * 13)
print("Equação de 2º grau completa")
print("/-" * 13)
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delt = (b ** 2) - 4 * a * c

if a == 0 or b == 0 or c == 0:
    print("Preciso de valores diferentes de zero.")
elif delt < 0:
    print("Não há solução real.")
elif delt > 0:
    print("Existe duas soluções reais e diferentes.")
else:
    delt == 0
    print("Existe apenas uma solução real.")