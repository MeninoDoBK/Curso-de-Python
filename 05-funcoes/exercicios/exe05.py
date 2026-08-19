# Crie um programa que tenha uma funcao Media(), que vai receber as 3 notas
# de um aluno e retornar a sua média para o programa principal.
n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))
n3 = int(input('Digite a sua terceira nota: '))

def media_notas(n1,n2,n3):
    soma_media = (n1 + n2 + n3) / 3
    return soma_media

def avaliacao(soma_media): 

    if soma_media >= 7: 
        return f'Sua média é de: {soma_media} - Parabéns ganhou 1000 de aura + ego, APROVADO!'
     
    elif soma_media >= 5 and soma_media <= 6.9: 
        return f'Sua média é de: {soma_media} - Se conseguir passar, ganha 500 de aura + ego, RECUPERAÇÃO'
    
    else: 
        return f'Sua média é de: {soma_media}  - 1000 DE AURA + EGO, REPROVADOOOOOOO'

print(avaliacao(n1))