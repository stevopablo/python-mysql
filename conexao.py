from mysql.connector import pooling
from mysql.connector import Error

class Conexao:
    DATABASE = 'clientes_db'
    USUARIO = 'root'
    SENHA = 'root'
    PORTA_DB = '3306'
    HOST = 'localhost'
    TAMANHO_POOL = 5
    NOME_POOL = 'clientes_db_pool'
    pool = None

    @classmethod
    def obter_pool(cls):
        if cls.pool is None:  # Cria o objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.NOME_POOL,
                    pool_size=cls.TAMANHO_POOL,
                    host=cls.HOST,
                    port=cls.PORTA_DB,
                    database=cls.DATABASE,
                    user=cls.USUARIO,
                    password=cls.SENHA
                )
                # print(f'Nome do pool: {cls.pool.pool_name}')
                # print(f'Tamanho do pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocorreu um erro ao obter o pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obter_conexao(cls):
        return cls.obter_pool().get_connection()

    @classmethod
    def liberar_conexao(cls, conexao):
        conexao.close()

if __name__ == '__main__':
    # Criação do objeto pool
    # pool = Conexao.obter_pool()
    # print(pool)
    # Obter um objeto de conexão
    cnx1 = Conexao.obter_conexao()
    print(cnx1)
    Conexao.liberar_conexao(cnx1)
