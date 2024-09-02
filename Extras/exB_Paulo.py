print('Programa de eleição')
cndA = int(input('Digite o número de votos do candidato A: '))
cndB = int(input('Digite o número de votos do candidato B: '))
cndC = int(input('Digite o número de votos do candidato C: '))
nul = int(input('Digite o número de votos nulo: '))
bran = int(input('Digite o número de votos em branco: '))
vali = cndA + cndB + cndC  #Votos válidos.

all = cndA + cndB + cndC + nul + bran  #Total de votos.
print('Total de votos: ', all)

pervali = vali / all * 100
print('Votos válidos: {}, sendo {:.2f}% do total.'.format(vali,pervali))

valiA = cndA / all * 100
print('Candidato A: {} votos, sendo {:.2f}% do total.'.format(cndA,valiA))

valiB = cndB / all * 100
print('Candidato B: {} votos, sendo {:.2f}% do total.'.format(cndB,valiB))

valiC = cndC / all * 100
print('Candidato C: {} votos, sendo {:.2f}% do total.'.format(cndC,valiC))

perNu = nul / all * 100  #Percentual de votos nulos.
print('Votos nulos: {}, sendo {:.2f}% do total.'.format(nul,perNu))

perBra = bran / all * 100  #Percentual de votos brancos.
print('Votos brancos: {}, sendo {:.2f}% do total.'.format(bran,perBra))