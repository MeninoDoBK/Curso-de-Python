numero = []
for i in range(5):
    pergunta = int(input('Digite um numero: '))
    numero.append(pergunta)

print('\n')
print('====PRODUTOS CADASTRADOS====\n')

for i in numero:
    print(i)


soma = 0
for i in numero:
    soma = soma + i
    print(soma)