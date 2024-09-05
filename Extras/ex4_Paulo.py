print('/*' * 7)
print("Será Bissexto?")
print('/*' * 7)
ano = int(input("Digite um ano: "))
sera = ano % 4
if sera == 0 and ano > 2023:
    print(f"O ano {ano} será bissexto")
elif sera > 0 and ano > 2023:
    print(f"O ano {ano} não será bissexto")
elif ano == 2023:
    print(f"O ano atual não é bissexto")
elif sera == 0 and ano < 2023:
    print(f"O ano {ano} foi bissexto")
elif sera > 0 and ano < 2023:
    print(f"O ano {ano} não foi bissexto")