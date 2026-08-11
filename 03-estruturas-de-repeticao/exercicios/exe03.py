saldo = 500

while saldo > 0:
    saque = float(input('Dejesa sacar quanto? Ou 0 para encerrar:0 '))
    if saque == 0:
        print('Saque encerrado')
        break

    if saque > saldo:
        print('Voce não tem o dinheiro suficiente')
        continue

    saldo = saldo - saque
    print(f'Saldo restante: {saldo}')
else:
    print('Saldo zerado.')