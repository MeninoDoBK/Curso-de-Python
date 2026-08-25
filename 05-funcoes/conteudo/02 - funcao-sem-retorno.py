
def menu():
    print('Digite: 1 ,Para falar com a atendente')
    print('Digite: 2, Para trocar de musica')
    print('Digite: 3, Para mudar de plano')
    print('Digite: 4, Para sair')

def melhoria(opcao):
        if opcao == 1:
            print('Falando com a atendente...')
            print('\n')
            return True
            
        elif opcao == 2:
            print('Trocando de musica...')
            print('\n')
            return True
            
        elif opcao == 3:
            print('Mudando de plano...')
            print('\n')
            return True
            
        elif opcao == 4:
            print('Saindo...')
            print('\n')
            return False
            
        else:
            print('Opcao inválida, tente novamente.')
            print('\n')
            return True    
        
while True:
    menu()
    
    opcao = int(input('Digite um numero de (1 a 4): '))

    encerrar = melhoria(opcao)
    if encerrar == False:
        break
