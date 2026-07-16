# OPERACOES ARITIMETICAS
# SOMA
# numero1 = 16
# numero2 = 20
# soma = numero1 + numero2
# print('a soma de',numero1, '+',numero2,'=',soma)

# MULTIPLICAÇÂO
# numero3 = 10
# numero4 = 10
# soma = numero3 * numero4
# print('A multiplicação entre',numero3,'*',numero4,'é =',soma)

# DIVISÃO EXATA
# numero5 = 30
# numero6 = 15
# soma = numero5 / numero6
# print('A divisão exata entre',numero5,'/',numero6,'é =',soma)

# DIVISÃO ARREDONDADA
# numero5 = 30
# numero6 = 15
# soma = numero5 // numero6
# print('A divisão arredondada entre',numero5,'//',numero6,'é =',soma)

# SUBTRAÇÂO
# numero7 = 150
# numero8 = 20
# soma = numero7 - numero8
# print('A subtração entre',numero7,'-',numero8,'é =',soma)

# RESTO DA DIVISÂO
# numero7 = 147
# numero8 = 13
# soma = numero7 % numero8
# print('O resto da divisão entre',numero7,'%',numero8,'é =',soma)

#POTENCIA
# numero9 = 2
# numero10 = 10
# soma = numero9 ** numero10
# print('A potência entre',numero9,'**',numero10,'é =',soma)


# PERGUNTANDO ALGO AO USUÁRIO input()
# CONVERTENDO O VALOR DO input PARA float OU int
# nota1 = float(input('digite a sua primeira nota: '))
# nota2 = float(input('digite a sua segunda nota: '))
# media = 0.0
# media = (nota1 + nota2) / 2
# print('a media do aluno é',media)

# PERGUNTE AO USUARIO O NOME,IDADE,ALTURA E MOSTRE O PRINT FINAL(FRASE)
# nome = input('Qual é o seu nome: ')
# idade = int(input('Quantos anos você tem: '))
# altura = float(input('Qual é a sua altura: '))
# print('Entendi seu nome é',nome,'você tem',idade,'anos,e tem',altura,'de altura,certo?')

# Perguntar ao usuairo peso, altura, e no final o IMC
nome = input('Qual é o seu nome? ')
peso = float(input('Quanto você pesa: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / (altura **2)
print('Olá',nome,'O seu IMC é de:',round(imc,2))