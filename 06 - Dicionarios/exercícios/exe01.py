produtos = [
    {
        'nome': 'Notebook',
        'preco': 4500
    },
    {
        'nome': 'Celular',
        'preco': 1800.50
    },
    {
        'nome': 'Mouse',
         'preco': 45
    },
    {
        'nome': 'Monitor',
        'preco': 670
    },
    {
        'nome': 'Teclado',
                'preco': 67
    },
]
# Somar todos os valores dos produtos.

soma = 0
for i in produtos:
    soma = soma + i['preco']

print(f'A soma total é de: {soma}')