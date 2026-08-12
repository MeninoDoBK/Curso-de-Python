# Calcule a media das notas e mostre o print
# notas = [5.5,8,9.2,5]
# nota1 = notas[0]
# nota2 = notas[1]
# nota3 = notas[2]
# nota4 = notas[3]
# soma_notas = (nota1 + nota2 + nota3 + nota4) / len(notas)
# print(f'A sua média é de:',{round(soma_notas,1)})



# carros = ['Fusca','Kombi','Golfe','Ferrari','BMW']

# for i in carros:
#     print(f'Carro: {i}')


# carrinho_compras = [150, 260, 100, 50, 60]
# soma = 0
# for i in carrinho_compras:
#     soma = soma + i

# print(f'A soma total dos produtos foi de: R$ {soma},00')

notas = [5.5 , 8 , 9.2 ,5]
soma = 0
for i in notas:
    soma = soma + i

media = soma / len(notas)
print(f'A sua média é de: {media}')