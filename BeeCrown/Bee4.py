#Intervalo
num = float(input())
if num < 0 or num > 100:
    print("Fora de intervalo")
elif num <= 25:
    print("Intervalo [0,25]")
elif num <= 50:
    print("Intervalo (25,50]")
elif num <= 75:
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")

# Salário
renda = float(input())
if renda <= 400:
    perce = 15
    imposto = renda * (perce / 100)
    renda = renda + imposto
elif renda <= 800:
    perce = 12
    imposto = renda * (perce / 100)
    renda = renda + imposto
elif renda <= 1200:
    perce = 10
    imposto = renda * (perce / 100)
    renda = renda + imposto
elif renda <= 2000:
    perce = 7
    imposto = renda * (perce / 100)
    renda = renda + imposto
else:
    perce = 4
    imposto = renda * (perce / 100)
    renda = renda + imposto
print(f"Novo renda: {renda:.2f}\nReajuste ganho: {imposto:.2f}\nEm percentual: {perce} %")

# DDD
mes = int(input())
if mes == 61:
    print("Brasilia")
elif mes == 71:
    print("Salvador")
elif mes == 11:
    print("Sao Paulo")
elif mes == 21:
    print("Rio de Janeiro")
elif mes == 32:
    print("Juiz de Fora")
elif mes == 19:
    print("Campinas")
elif mes == 27:
    print("Vitoria")
elif mes == 31:
    print("Belo Horizonte")
else:
    print("mes não cadastrado")

# Imposto de Renda
renda = float(input())
if renda <= 2000:
    print("Isento")
elif renda <= 3000:
    imposto = (renda - 2000) * 0.08
    print(f"R$ {imposto:.2f}")

elif renda <= 4500:
    imposto = (1000 * 0.08) + ((renda - 3000) * 0.18)
    print(f"R$ {imposto:.2f}")
else:
    imposto = (1000 * 0.08) + (1500 * 0.18) + ((renda - 4500) * 0.28)
    print(f"R$ {imposto:.2f}")

# Mês
mes = int(input())
if mes == 1:
    print("January")
elif mes == 2:
    print("February")
elif mes == 3:
    print("March")
elif mes == 4:
    print("April")
elif mes == 5:
    print("May")
elif mes == 6:
    print("June")
elif mes == 7:
    print("July")
elif mes == 8:
    print("August")
elif mes == 9:
    print("September")
elif mes == 10:
    print("October")
elif mes == 11:
    print("November")
else:
    print("December")