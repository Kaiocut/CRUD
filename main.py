import mysql.connector

# Cria uma conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asklaskl",
    database="employees",
)

cursor = conexao.cursor() #Cria um cursor para execução de comandos no banco de dados

#---CREATE---
comando1 = 'ALTER TABLE departments ADD COLUMN dept_desc VARCHAR(20)' #Cria uma coluna chamada de dept_desc
cursor.execute(comando1) #Executa o comando
conexao.commit() #Edita o banco de dados

#---READ---
comando2 = 'describe departments' # Mostra a estrutura da tabela departments
cursor.execute(comando2)
resultado = cursor.fetchall() # Faz a leitura do banco de dados
print(resultado) # Mostra o resultado no terminal

#---UPDATE---
comando3 = 'UPDATE departments SET dept_desc = "funcionou" WHERE dept_name = "Marketing"' #Adiciona uma descrição a coluna dept_desc
cursor.execute(comando3) #Executa o comando
conexao.commit() #Edita o banco de dados

#---DELETE---
comando4 = 'ALTER TABLE departments DROP COLUMN dept_desc' #Apaga a coluna
cursor.execute(comando4) #Executa o comando
conexao.commit() #Edita o banco de dados

cursor.close()  #Encerra o cursor
conexao.close() #Encerra a conexão com o banco de dados