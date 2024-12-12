from cliente import Cliente
from conexao import Conexao


class ClienteDAO:
    SELECIONAR = 'SELECT * FROM cliente'
    INSERIR = 'INSERT INTO cliente(nome, sobrenome, desconto) VALUES(%s, %s, %s)'
    ATUALIZAR = 'UPDATE cliente SET nome=%s, sobrenome=%s, desconto=%s WHERE id=%s'
    EXCLUIR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def selecionar(cls):
        conexao = None
        try:
            conexao = Conexao.obter_conexao()
            cursor = conexao.cursor()
            cursor.execute(cls.SELECIONAR)
            registros = cursor.fetchall()
            # Mapeamento de classe-tabela cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocorreu um erro ao selecionar clientes: {e}')
        finally:
            if conexao is not None:
                cursor.close()
                Conexao.liberar_conexao(conexao)

    @classmethod
    def inserir(cls, cliente):
        conexao = None
        try:
            conexao = Conexao.obter_conexao()
            cursor = conexao.cursor()
            valores = (cliente.nome, cliente.sobrenome, cliente.desconto)
            cursor.execute(cls.INSERIR, valores)
            conexao.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocorreu um erro ao inserir cliente: {e}')
        finally:
            if conexao is not None:
                cursor.close()
                Conexao.liberar_conexao(conexao)

    @classmethod
    def atualizar(cls, cliente):
        conexao = None
        try:
            conexao = Conexao.obter_conexao()
            cursor = conexao.cursor()
            valores = (cliente.nome, cliente.sobrenome,
                       cliente.desconto, cliente.id)
            cursor.execute(cls.ATUALIZAR, valores)
            conexao.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocorreu um erro ao atualizar cliente: {e}')
        finally:
            if conexao is not None:
                cursor.close()
                Conexao.liberar_conexao(conexao)

    @classmethod
    def excluir(cls, cliente):
        conexao = None
        try:
            conexao = Conexao.obter_conexao()
            cursor = conexao.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.EXCLUIR, valores)
            conexao.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocorreu um erro ao excluir cliente: {e}')
        finally:
            if conexao is not None:
                cursor.close()
                Conexao.liberar_conexao(conexao)

if __name__ == '__main__':
    # Inserir cliente
    # cliente1 = Cliente(nome='Alejandra', sobrenome='Tellez', desconto=300)
    # clientes_inseridos = ClienteDAO.inserir(cliente1)
    # print(f'Clientes inseridos: {clientes_inseridos}')

    # Atualizar cliente
    # cliente_atualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_atualizados = ClienteDAO.atualizar(cliente_atualizar)
    # print(f'Clientes atualizados: {clientes_atualizados}')

    # Excluir cliente
    # cliente_excluir = Cliente(id=3)
    # clientes_excluidos = ClienteDAO.excluir(cliente_excluir)
    # print(f'Clientes excluídos: {clientes_excluidos}')

    # Selecionar clientes
    clientes = ClienteDAO.selecionar()
    for cliente in clientes:
        print(cliente)
