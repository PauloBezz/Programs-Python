print('/*' * 20)
print("Idade nas versões humana, canina e felina")
print('/*' * 21)
age = int(input("Digite a idade: "))
escolha = input("H-Humano, C-Cachorro ou G-Gato? ").upper()
if escolha == 'H':
    if age >= 60:
        print("Idoso, aposentadoria em processo...")
    elif age >= 18:
        print("Maior de idade, bom pra trabalhar.")
    elif age <= 18:
        print("Menor de idade, aproveite.")
    elif age <= 12:
        print("Infância, brinque mais.")
    else:
        age <= 2
        print("Bebê ainda.")
elif escolha == 'C':
    if age == 1:
        print("Seu doguinho tem 7 anos caninos")
    elif age == 2:
        print("Seu admirador tem 14 anos caninos")
    else:
        age > 2
        dog = age * 7
        print(f"Seu melhor amigo tem {dog} anos")
elif escolha == 'G':
    if age == 1:
        print("Seu gatinho tem 16 anos") 
    elif age == 2:
        print("Seu gatucho tem 24 anos")
    elif age > 2:
        cat = 24 + (age * 4) 
    print(f"Seu psipsipsi tem {cat}")
else:
    escolha == 'S'
    print("Até mais, amigo")