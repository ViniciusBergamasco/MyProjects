def enter():
    input('Pressione ENTER para continuar...')


def numbersinput(operacao):
    n1 = int(input('Digite o primero número: '))
    n2 = int(input('Digite o segundo número: '))
    if operacao == '1':
        print(f'O resultado é: {n1 + n2}')
    elif operacao == '2':
        print(f'O resultado é: {n1 - n2}')
    elif operacao == '3':
        print(f'O resultado é: {n1 * n2}')
    else:
        print(f'O resultado é: {n1 / n2}')

sair = 'n'
while sair == 'n':
    opcao =input('''    ### CALCULADORA ###
    
    [1]- Adição
    [2]- Subtração
    [3]- Multiplicação
    [4]- Divisão
    [5]- Sair
    
Digite o número da opção desejada: 
    ''')
    if opcao == '1':
        numbersinput(opcao)
        enter()
    elif opcao == '2':
        numbersinput(opcao)
        enter()
    elif opcao == '3':
        numbersinput(opcao)
        enter()
    elif opcao == '4':
        numbersinput(opcao)
        enter()
    elif opcao == '5':
        sair = input('''Você deseja realmente sair do programa?
        Digite [s] para sair e [n] para continuar nele.
        Resposta: ''').lower()
    else:
        print('Essa opção não existe.')
        enter()


    
