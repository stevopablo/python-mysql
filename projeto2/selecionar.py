import mysql.connector

# Conectar ao banco de dados MySQL
pessoas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pessoas_db",
)

cursor = pessoas_db.cursor()

# Exibir todos os dados da tabela clientes
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
print("Clientes na tabela (ID, Nome, Membresia):")
for pessoa in resultado:
    print(pessoa)

# Inserir um novo cliente
adicionar_sql = 'INSERT INTO clientes (nome, membresia) VALUES (%s, %s)'
dados = ('Pedro', '200')

cursor.execute(adicionar_sql, dados)
pessoas_db.commit()  # Commit para salvar a inserção

print(f"\nNovo cliente inserido com sucesso!")

# Atualizar um cliente
atualizar_sql = 'UPDATE clientes SET nome=%s, membresia=%s WHERE id=%s'
dados2 = ('Vitoria', '500', 1)  # Aqui você precisa fornecer o ID também
cursor.execute(atualizar_sql, dados2)
pessoas_db.commit()  # Commit para salvar a atualização

print(f"\nCliente atualizado com sucesso!")

# Remover um cliente
remover_sql = 'DELETE FROM clientes WHERE id=%s'
valor = (2,)  # O valor precisa ser uma tupla, então a vírgula é importante
cursor.execute(remover_sql, valor)
pessoas_db.commit()  # Commit para salvar a exclusão

print(f"\nCliente removido com sucesso!")

# Exibir os dados após a inserção, atualização e remoção
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
print("\nClientes na tabela após alterações:")
for pessoa in resultado:
    print(pessoa)

# Fechar a conexão
pessoas_db.close()
