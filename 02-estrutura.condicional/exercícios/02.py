# Exercício — Classificando
# Triângulos
# Um programa deve receber o comprimento dos três lados de um possível
# triângulo.
# Primeiro, verifique se os valores informados podem formar um triângulo.

lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if (lado1 + lado2) < (lado3) or (lado3 + lado2) < (lado1):
    print('Os valores informados não formam um triângulo.')
elif (lado1) == (lado2) == (lado3):
    print('Triângulo Equilátero')
elif (lado1) == (lado2) != (lado3):
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')