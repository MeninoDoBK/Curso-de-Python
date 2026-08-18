CarrinhoCompra = [5,5,5]
ListaCompra = [10,10,10]

# def soma(carrinho):
#     return(carrinho + i)
# for i in CarrinhoCompra:
#     CarrinhoCompra = 0
#     resultado = soma(CarrinhoCompra + i)
#     print(resultado)

CarrinhoCompra = [5,5,5]
def soma_listas(lista):
    soma = 0
    for i in lista:
        soma += i
        return soma

soma_carrinho = soma_listas(CarrinhoCompra)
print(f'A soma do carrinho é de: {soma_carrinho}')