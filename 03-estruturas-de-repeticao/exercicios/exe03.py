saldo = 10

while saldo > 0:
    saque = float(input('Dejesa sacar quanto? Ou 0 para encerrar. '))
    if saque == 0:
        print('Não é possivel sacar 0 R$')
        break

    if saque > saldo:
        print('Voce não tem o dinheiro suficiente')
        continue

    saldo = saldo - saque
    print(f'Saldo restante: {saldo}')
else:
    print('Saldo zerado.')