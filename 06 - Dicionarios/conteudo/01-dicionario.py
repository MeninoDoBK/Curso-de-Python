# Criando um dicionario 
pessoa = {
    'nome': 'Bernardo',
    'altura': '1.60',
    'peso': '42',
    'anoNascimento':2012,
    'time': 'Flamengo' 
}

# Acessar um valor no dicionario
print(pessoa['anoNascimento'])

# comprimento(Quantas propriedade)
print(len(pessoa))

# Podemos guardar um valor dentro de uma variavel
nome = pessoa['nome']
print(nome)

# Alterar valor dentro de um dicionario
pessoa['peso'] = 67
print(pessoa)

# Criar novo valor no dicionario
pessoa['corCabelo'] = 'preto'
print(pessoa)

# Criando array de dicionario
jogadores = [
    {
        'nome': 'Neymar',
        'idade': 34,
        'Habilidade': 'Drible/passe',
    },
    {
        'nome': 'Cr7',
        'idade': 41,
        'Habilidade': 'Chute/acrobacia',
    },
    {
        'nome': 'Vozinha',
        'idade': 40,
        'habilidade': 'Defesa/reflexo'
    }
]

# Mostrar o nome Cr7 dentro do print
print(jogadores[1]['nome'])

# Mostrar todos os nomes das chaves (propriedades)
for i in pessoa:
    print(i)

# Mostrar todos os valores do dicionario
for i in pessoa.values():
    print(i)

# Mostra valores de um array de dicionarios
for t in jogadores:
    # Pegando todos os nomes:
    print(t['nome'])