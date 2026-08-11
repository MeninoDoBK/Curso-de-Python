contador = 0
while contador < 10:
    entrada = int(input('Quantos produtos voce deseja colocar, limite 10: '))
    if entrada == 0 or entrada < 0:
        print('Limite exedido.')
        continue

    if contador > 10:
        print('Não a espaço no estoque. Digite um número menor.')
        continue

    if contador + entrada > 10:
        print(f'limite exedido, vc ainda tem {contador}, digite um número menor.')
        continue

    contador = contador + entrada
    print(f'Estoque cheio {contador}')
    