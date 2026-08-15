numero = []
for i in range(5):
    pergunta = int(input('Digite um numero: '))
    numero.append(pergunta)

print('\n')
print('====SOMA DOS QUADRADOS====\n')

soma_dos_quadrados = 0

for i in numero:
    quadrado = i * i
    print(f'O quadrado é: {quadrado}')
    soma_dos_quadrados += quadrado

print('\n')
print(f'A soma total dos quadrados é: {soma_dos_quadrados}')
