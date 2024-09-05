a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o último valor: "))
if a >= b and a >= c and b >= c:
    print(f"Ordem dos valores:{c, b, a}")
elif a >= b and a >= c and c >= b:
    print(f"Ordem dos valores:{b, c, a}")
elif b >= a and b >= c and a >= c:
    print(f"Ordem dos valores:{c, a, b}")
elif b >= a and b >= c and c >= a:
    print(f"Ordem dos valores:{a, c, b}")
elif c >= a and c >= b and a >= b:
    print(f"Ordem dos valores:{b, a, c}")
else:
    c >= a and c >= b and b >= a
    print(f"Ordem dos valores:{a, b, c}")