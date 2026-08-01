#Crie um programaque solicite o peso e a altura da pessoa e mostre o calculo
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = peso / altura ** 2

if (imc < 18.5):
    print('Voce está abaixo do peso')

elif (imc >= 18.5) and (imc <= 24.9):
    print('O seu peso esta normal')

elif (imc >= 25.0) and (imc <= 29.9):
    print('Excesso de peso')

elif (imc >= 30.0) and (imc <= 34.9):
    print('Obesidade classe 1')

elif (imc >= 35.0) and (imc <= 39.9):
    print('Obesidade classe 2')

else:
    print('Obesidade classe 3 (Grave)')

print(f'E o seu IMC é de: {round(imc,2)}')