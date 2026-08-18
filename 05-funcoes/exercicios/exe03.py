# Crie uma funcao par ou impar que recebe um numero
# e retorne se o numero é par ou impar
# pergunte ao usuario o numero



numero = int(input('Digite um numero: '))

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'Impar'

print(par_ou_impar(numero))
    
