print('-'*20)
print('Maior / Menor / Soma / Média')
print('-'*20)
nums = []
for i in range(0,10):
    num = int(input(f'Escolha o {i + 1}º número: '))
    nums.append(num)

print(f'Maior: {max(nums)}')
print(f'Mínimo: {min(nums)}')
print(f'Soma: {sum(nums)}')
print(f'Média: {sum(nums) / len(nums)}')