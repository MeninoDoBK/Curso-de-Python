# (98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois 
# numeros como parâmetro e depois vai retornar a soma de todos os valores no1


# SuperSomador(1,6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15,19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

# numero1 = int(input('Digite um numero: '))
# numero2 = int(input('Digite um numero: '))

# def SuperSomador(numero1,numero2):
#     soma = 0
#     for i in (numero1,numero2):
#         soma += 1

#     return soma

# print(SuperSomador(numero1,numero2))


def SuperSomador(inicio,fim):
    soma = 0
    for i in range(inicio,fim + 1):
        soma += i

    return soma

print(SuperSomador(1,6))
print(SuperSomador(15,19))