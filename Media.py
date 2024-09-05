print("/*/" * 8)
print("Qual é a sua média final?")
print("/*/" * 8)
n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
n3 = float(input("Digite a 3º nota: "))
n4 = float(input("Digite a 4º nota: "))
md1 = (n1 + n2 + n3 + n4) / 4

if md1 > 10:
    print(f"A média de {md1} está acima de 10.0. Por favor, refaça")
elif md1 >= 7 or md1 <= 10:
    print(f"Aprovado\n 1ºnota: {n1}\n 2ºnota: {n2}\n 3ºnota: {n3}\n 4ºnota: {n4} \n Média final: {md1}")
elif md1 >= 6.9:
    print("Exame necessário")
    ne = float(input("Digite a nota do exame: "))
    md2 = (n1 + n2 + n3 + n4 + ne) / 5
    if md2 >= 5:
        print(f"Aprovado em exame\n 1ºnota: {n1}\n 2ºnota: {n2}\n 3ºnota: {n3}\n 4ºnota: {n4}\n Exame: {ne}\n Média final: {md2}")
    else:
        print(f"Reprovado\n 1ºnota: {n1}\n 2ºnota: {n2}\n 3ºnota: {n3}\n 4ºnota: {n4}\n Exame: {ne}\n Média final: {md2}")