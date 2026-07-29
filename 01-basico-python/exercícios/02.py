nome_produto = input('Digite o nome do produto: ')
preco = input('Digite o preço do produto: ')
quantidade = input('Digite a quantidade do produto: ')
categoria = input('Digite a categoria do produto: ')
promocao = input('O preoduto está em promoção? (S/N): ')
esta_promocao = promocao == 'S' or promocao =='s'

print(f'nome do produto: {nome_produto}')
print(f'preço: {preco}')
print(f'quantidade: {quantidade}')
print(f'categoria: {categoria}')
print(f'o produto esta em promocao?: {esta_promocao}')