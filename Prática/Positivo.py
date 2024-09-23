print("/*/" * 6)
print("Seja mais positivo!")
print("/*/" * 6)
n = int(input("Digite um número: "))

if n > 0:
    print(f"O número é {n}")
elif n < 0:
    saldo = n * - 1
    print(f"O número {n} retornou {saldo}")