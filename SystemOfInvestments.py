import sqlite3
banco = sqlite3.connect('bancoInv.db')
cursor = banco.cursor()


def continuar():
    input('Aperte ENTER para continuar...')


def tabela():
    for line in cursor.fetchall():
        print('   INVESTIMENTO')
        print(f'ID: {line[0]}')
        print(f'Investimento: {line[1]}')
        print(f'Quantidade: {line[2]}')
        print(f'Valor: {line[3]}')
        print(f'Tipo: {line[4]}')
        print('-----------------------------------')



sair = 'n'
while sair == 'n':
    opcao= int(input('''    ### SISTEMA DE INVESTIMENTOS ### 
    
[1]- Cadastrar um novo investimento
[2]- Deletar um investimento
[3]- Exibir os investimentos por categoria
[4]- Sair do programa

Digite o número da opção desejada: '''))
    if opcao == 1:
        investimento = input('Investimento: ')
        quantidade = input('Quantidade: ')
        valor = input('Valor: ')
        tipo = input('Tipo: ').lower()
        cursor.execute(f"INSERT INTO registro (investimento, quantidade, valor, tipo) VALUES ('{investimento}', {quantidade}, {valor}, '{tipo}')")
        banco.commit()
        print('Investimento registrado!')
        continuar()
    elif opcao == 2:
        cursor.execute('SELECT * FROM registro')
        tabela()
        ID = int(input('Digite o ID para deleltar o investimento: '))
        cursor.execute(f"DELETE FROM registro WHERE id = {ID}")
        banco.commit()
        print('Investimento deletado!')
        continuar()
    elif opcao == 3:
        exibir1 = input('''    ### TIPOS DE INVESTIMENTO ###
1- Renda fixa
2- Renda variável
3- Caixa
4- EUA
Digite o número do tipo de investimento desejado: ''')
        if exibir1 == 1:
            cursor.execute("SELECT * FROM registro WHERE tipo = 'renda fixa' ")
            tabela()
            continuar()
        elif exibir1 == 2:
            cursor.execute("SELECT * FROM registro WHERE tipo = 'renda variável' ")
            tabela()
            continuar()
        elif exibir1 == 3:
            cursor.execute("SELECT * FROM registro WHERE tipo = 'caixa' ")
            tabela()
            continuar()
        elif exibir1 == 4:
            cursor.execute("SELECT * FROM registro WHERE tipo = 'eua' ")
            tabela()
            continuar()
        else:
            print('Esse tipo de investimento não existe!')
            continuar()
    elif opcao == 4:
        sair = input('''Deseja mesmo sair do programa? Digite [s] para sair e [n] para continuar nele.
        Resposta: ''')