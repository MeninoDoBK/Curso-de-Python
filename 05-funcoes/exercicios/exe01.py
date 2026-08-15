# Pedir ao usuario dois numeros, e com esses numeros
# calcular a soma, subtracao, divisao, e multiplicacao
# e tambem pedir ao usuario um nome e sauda-lo
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
nome = input('Qual é o seu nome: ')
print('\n')


def soma(numero):                       # OBS: (RECEBO DOIS VALORE, E DEPOIS SOMO OS DOIS VALORES.)
    return(numero)
adicao = soma(numero1 + numero2)
print(f'A soma dos valores foi de: {adicao}')
print('\n')

def subtrair(numero):
    return(numero)
subtracao = soma(numero1 - numero2)
print(f'A subtracao dos valores foi de: {subtracao}')
print('\n')

def multiplicar(numero):
    return(numero)
multiplicacao = soma(numero1 * numero2)
print(f'A multiplicacao dos valores foi de: {multiplicacao}')
print('\n')

def dividir(numero):
    return(numero)
divisao = soma(numero1 / numero2)
print(f'A divisao dos valores foi de: {divisao}')
print('\n')

def usuario(nome):
    return(nome)
name = usuario(nome)
print(f'Olá {nome}, seja bem vindo(a)!')                 # (Eu que fiz)