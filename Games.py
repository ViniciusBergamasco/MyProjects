import random

def continuar():
    tecla = input('Aperte qualquer tecla para continuar...')

def jogarNov():
    global sair
    playAgain = input("""Deseja jogar novamente? Digite [s] para continuar jogando e [n] para sair do programa
       Resposta: """).lower()
    if playAgain == 's':
        sair = 'n'
    elif playAgain == 'n':
        sair = 's'
    else:
        print('Essa opção não existe!')
        continuar = input('Aperte qualquer tecla para continuar...')
    return sair



sair = 'n'
while sair == 'n':
    print('''    ### JOGOS ###
1- Pedra, papel ou tesoura
2- Adivinhe o número
3- Ímpar ou par 
''')
    jogo = input('Digite o número do jogo desejado: ')
    if jogo == '1':
        print("    ### JOGO PEDRA, PAPEL OU TESOURA ###")
        opcao = input("Faça a sua escolha: ").lower()
        pc = ['pedra', 'papel', 'tesoura']
        excolhaPc = random.choice(pc)
        if excolhaPc == 'pedra' and opcao == 'pedra' or excolhaPc == 'papel' and opcao == 'papel' or excolhaPc == 'tesoura' and opcao == 'tesoura':
            print(f''' Computador: {excolhaPc}
    EMPATOU!''')
        elif excolhaPc == 'pedra' and opcao == 'papel' or excolhaPc == 'tesoura' and opcao == 'pedra' or excolhaPc == 'papel' and opcao == 'tesoura':
            print(f'''Computador: {excolhaPc}
    VOCÊ GANHOU!''')
        elif excolhaPc == 'pedra' and opcao == 'tesoura' or excolhaPc == 'papel' and opcao == 'pedra' or excolhaPc == 'tesoura' and opcao == 'papel':
            print(f'''Cmputador: {excolhaPc}
        VOCÊ PERDEU!''')
        else:
            print('Essa opcão não existe!')
            continuar()
        sair = jogarNov()
    elif jogo == '2':
        print('    ### ADIVINHE O NÚMERO ###')
        escolhaPc = random.randint(0, 11)
        escolhaUs = int(input('Tente adivinhar um número de 0 a 10: '))
        if escolhaUs < 0 or escolhaUs > 10:
            print('O número digitado não está dentro do intervalo proposto')
            continuar()
        else:
            print(f'O número era {escolhaPc}')
            if escolhaPc == escolhaUs:
                print('Você acertou!')
            else:
                print('Você errou!')
            continuar()
            sair = jogarNov()
    elif jogo == '3':
        print('    ### ÍMPAR OU PAR ###')
        escolhaPc = random.randint(0, 11)
        imparOuPar = input('Escolha entre ímpar ou par: ').lower()
        if imparOuPar != 'ímpar' and imparOuPar != 'par':
            print('Essa opção não existe.')
            continuar()
        numero = int(input('Escolha um número:'))
        resultado = (escolhaPc + numero)%2
        if imparOuPar == 'ímpar'  and resultado == 1 or imparOuPar == 'par' and resultado == 0:
            print(f'O computador escolheu o número {escolhaPc}')
            print('Você ganhou!')
        else:
            print(f'O computador escolheu o número {numero}')
            print('Você perdeu!')
        continuar()
        sair = jogarNov()
    else:
        print('Essa opção de jogo não existe!')
        continuar()