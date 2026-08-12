print('===== MINIGAME NUMERO SECRETO =====')
import random

numero_secreto = random.randint(1,100)
tentativas = 1

while tentativas <= 5:
    print(f'Tentativa {tentativas} de 5')
    chute = int(input('Chute um número de 1 a 100: '))

    if chute == numero_secreto:
        print('Parabens vc acerou o numero secreto! ')
        break

    if chute > numero_secreto:
        print('Chute incorreto, o número secreto é menor que seu chute, tente novamente: ')
    else: 
        print('Chute incorreto, o número secreto é maior que seu chute, tente novamente: ')
    
    tentativas += 1

else:

    print('GAME OVER - NOOOBBBBB ')
    print(f'O numero secreto era: {numero_secreto}')