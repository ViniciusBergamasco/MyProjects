quartos_reservados = {}
opcao = ''

while opcao != 's':
    print('''
    =-=-=-= OPÇÕES DO SISTEMA =-=-=-=
        [N] = Nova reserva
        [D] = Remover reserva
        [R] = Exibir Relatório 
        [S] = Sair do Programa 
    ''')
    opcao = input('Opção: ').lower()
    if opcao == 'n':
        quarto = int(input('Informe o número do quarto: '))
        if quarto in quartos_reservados:
            print('Este quarto está ocupado. Escolha outro!')
        else:
            hospede = input('Informe o nome do hospede: ')
            quartos_reservados[quarto] = hospede
    elif opcao == 'd':
        print('+++QUARTOS RESERVADOS+++')
        for quarto, hospede in quartos_reservados.items():
            print(f'Quarto número {quarto}: {hospede}')
        excluir_reserva = int(input('Digite o número do quarto para excluir a reserva: '))
        if excluir_reserva in quartos_reservados:
            quartos_reservados.pop(excluir_reserva)
            print('A reserva foi excluída com sucesso!.')
        else:
            print('Quarto não encontrado')
    elif opcao == 'r':
        print('=-=-=-=-= RELATÓRIO DOS QUARTOS =-=-=-=-=')
        for quarto, hospede in quartos_reservados.items():
            print(f'QUARTO Nº {quarto} = {hospede.upper()}')
    else:
        print('Essa opção não existe!')