print("/*/" * 7)
print("Diferença dos números")
print("/*/" * 7)
nm1 = int(input("Digite o primeiro valor: "))
nm2 = int(input("Digite o segundo valor: "))
dif = nm1 - nm2

if nm1 > nm2:
    print(f'A difereça de {nm1} e {nm2} é de {dif}.')
elif nm2 > nm1:
    dif = (nm1 - nm2) * - 1
    print(f'A diferença de {nm1} é {nm2} é de {dif}.')
else:
    dif == 0
    print(f'Os valores são iguais')