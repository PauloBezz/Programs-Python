print('/*' * 7)
print("Maior de três!")
print('/*' * 7)
for i in range(20):
    num = int(input("Digite um número: "))
    rest = num % 2
    if num > 0 and rest == 0:
        print(f"{num} é par e positivo")
    elif num > 0 and rest > 0:
        print(f"{num} é ímpar e positivo")
    elif num < 0 and rest == 0:
        print(f"{num} é par e negativo")
    else:
        print(f"{num} é ímpar e negativo")