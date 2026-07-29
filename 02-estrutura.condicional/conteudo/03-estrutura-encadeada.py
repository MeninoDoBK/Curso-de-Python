#Permite varias condiçoes
# nota = float(input('Qual foi a sua nota: '))

# if nota >= 18:
#     print('Parabens voce foi aprovado')
# elif nota <= 5:
#     print('Voce esta de recuperação')
# else:
#     print('Você foi reprovado')

# print('======Exemplo======')
# idade = int(input('Quantos anos voce tem: '))

# if idade < 12:
#     print('Você é uma criança')
# elif idade < 18:
#     print('Você é um adolescente')
# elif idade < 60:
#     print('Você é um aduto')
# else:
#     print('Você esta na melhor idade')

print('====EXEMPLO, operador lógico')

usuario = input('O cadastro esta correto? (S/N)').upper()
senha = input('A senha esta correta? (S/N)').upper()

if usuario == 'S' and senha == 'S':
    print('Acesso liberado')
else:
    print('Acesso negado')