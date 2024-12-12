from cliente import Cliente
from cliente_dao import ClienteDAO

print('*** Clientes de Zona Fit (Academia)')
opcao = None
while opcao != 5:
    print('''Menu:
    1. Listar clientes
    2. Adicionar cliente
    3. Modificar cliente
    4. Excluir cliente
    5. Sair
    ''')
    opcao = int(input('Digite sua opção (1-5): '))
    if opcao == 1:  # Listar clientes
        clientes = ClienteDAO.selecionar()
        print('\n*** Lista de Clientes ***')
        for cliente in clientes:
            print(cliente)
        print()
    elif opcao == 2:  # Adicionar cliente
        nome_var = input('Digite o nome: ')
        sobrenome_var = input('Digite o sobrenome: ')
        desconto_var = input('Digite o desconto: ')
        cliente = Cliente(nome=nome_var, sobrenome=sobrenome_var,
                          desconto=desconto_var)
        clientes_inseridos = ClienteDAO.inserir(cliente)
        print(f'Clientes inseridos: {clientes_inseridos}\n')
    elif opcao == 3:  # Modificar cliente
        id_cliente_var = int(input('Digite o ID do cliente a ser modificado: '))
        nome_var = input('Digite o nome: ')
        sobrenome_var = input('Digite o sobrenome: ')
        desconto_var = input('Digite o desconto: ')
        cliente = Cliente(id_cliente_var, nome_var, sobrenome_var, desconto_var)
        clientes_atualizados = ClienteDAO.atualizar(cliente)
        print(f'Clientes atualizados: {clientes_atualizados}\n')
    elif opcao == 4:  # Excluir cliente
        id_cliente_var = int(input('Digite o ID do cliente a ser excluído: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_excluidos = ClienteDAO.excluir(cliente)
        print(f'Clientes excluídos: {clientes_excluidos}\n')
else:
    print('Saindo da aplicação...')
