saldo = 1000.00
def mostrar_menu():
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def consultar_saldo(saldo):
    return(f'O seu saldo é de R$ {saldo}')
print(consultar_saldo(saldo))

def depositar_saldo(saldo):
    deposito = float(input('Quanto dejesa depositar? '))
    print ('Saque realizado com sucesso.')
    return(saldo + deposito)

print(depositar_saldo(saldo))

def sacar(saldo):
    saque = float(input('Quanto deseja sacar? '))
    if saque > saldo:
        print('Vc não tem dinheiro suficiente seu BETINHA.')
        return saldo
    saldo = saldo - saque
    return(saldo)
print(sacar(saldo))

while True:
    mostrar_menu(saldo)

    opcao = int(input('Digite uma das opções acima: '))

    if opcao == 1:
        print(consultar_saldo(saldo))
    elif opcao == 2:
        saldo = (depositar_saldo(saldo))
    elif opcao == 3:
        saldo = (sacar(saldo))
    elif opcao == 4:
        print('Saindo...')
        break
    else:
        print('Opcao invalida.')

print('Obrigado por utilizar o Banco Python!')