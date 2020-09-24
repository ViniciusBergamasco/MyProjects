import sqlite3

banco = sqlite3.connect('registro.db')
cursor = banco.cursor()

def continuar():
    enter = input('Digite "enter"" para continuar...')



def verificarID(idServico):
    cursor.execute(f'SELECT id FROM servicos WHERE id = {idServico}')
    return cursor.fetchone()



def lista():
    for line in cursor.fetchall():
         print('### SERVIÇO ###')
         print(f'ID: {line[0]}')
         print(f'Cliente: {line[1]}')
         print(f'Descrição: {line[2]}')
         print(f'Status: {line[3]}')
         print('_______________________________')



sair = 'n'
while sair == 'n':
 opcao = int(input('''   ### SISTEMA DE SERVIÇOS ###
 
    (1)- Novo serviço
    (2)- Atualizar o status de um serviço
    (3)- Listar serviços
    (4)- Remover um serviço
    (5)- Sair do programa
    
Digite o número da opção desejada: '''))

 if opcao == 1:
     print("### CADASTRO ###")
     inpcliente = input('Cliente: ')
     inprelato = input('Relato: ')
     cursor.execute(f"INSERT INTO servicos (cliente, relato, status) VALUES ('{inpcliente}', '{inprelato}', 'Na fila') ")
     print('Serviço inserido com sucesso!')
     continuar()
     banco.commit()

 elif opcao == 2:
     cursor.execute("SELECT * FROM servicos")
     lista()
     ID = int(input('Digite o ID do serviço para alterar seu status: '))
     retorno = verificarID(ID)
     if not retorno:
         print("Esse ID não existe!")
         continuar()
     else:
         NovoStatus = int(input('''### NOVO STATUS ### 
1- Em manutenção
2- Concluído
     
     Digite o número do novo status desejado: '''))
         if NovoStatus == 1:
            cursor.execute(f"UPDATE servicos SET status = 'Em manutenção' WHERE id = {ID} ")
            banco.commit()
            print('Status atualizado!')
            continuar()
         elif NovoStatus == 2:
            cursor.execute(f"UPDATE servicos SET status = 'Concluído' WHERE id = {ID} ")
            banco.commit()
            print('Status atualizado!')
            continuar()
         else:
            print("Essa opção não existe!")
            continuar()

 elif opcao == 3:
     listagem = int(input('''
(1)-Listar serviços na fila
(2)-Listar serviços em manutenção
(3)-Listar serviços concuídos
     
Digite o número da listagem desejada: '''))

     if listagem == 1:
         cursor.execute("SELECT * FROM servicos WHERE status = 'Na fila'")
         lista()
         continuar()
     elif listagem == 2:
         cursor.execute("SELECT * FROM servicos WHERE status = 'Em manutenção'")
         lista()
         continuar()
     elif listagem == 3:
         cursor.execute("SELECT * FROM servicos WHERE status = 'Concluído'")
         lista()
         continuar()
 elif opcao == 4:
     cursor.execute('SELECT * FROM servicos')
     lista()
     deletar = input('Digite o ID do serviço que deseja excluir: ')
     retorno = verificarID(deletar)
     if not retorno:
         print("Esse ID não existe!")
         continuar()
     else:
        cursor.execute(f'DELETE FROM servicos WHERE id = {deletar}')
        banco.commit()
        print('Serviço deletado com sucesso!')
        continuar()

 elif opcao == 5:
     print("Deseja mesmo sair do programa?")
     sair = input('Digite "s" para sair e "n" para permanecer')

 else:
     input("Essa opção não existe.Aperte enter para continuar...")