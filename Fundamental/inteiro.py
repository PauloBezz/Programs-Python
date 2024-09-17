num = int(input("Digite o inteiro: "))
soma = num
maior = num
menor = num
if num > 0:
    while num != 0 and num > 0:
        num = int(input("Digite o inteiro: "))
        if maior < num:
            maior = num
        if num > 0 and num < menor:
            menor = num
        soma += num
    print(f"Maior: {maior}, Menor: {menor} Soma: {soma}")
print("Fim do programa!")


num = int(input("Digite o inteiro: "))
while num != 0:
    if num % 2 != 0:
        print("Primo")
    else:
        print("Não Primo")
    num = int(input("Digite o inteiro: "))