from db import conectar

def criar_aluno(nome, sobrenome, nascimento, sexo, telefone):
    con = conectar()
    cursor = con.cursor()
    sql = "INSERT INTO alunos (nome, sobrenome, nascimento, sexo, telefone) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, sobrenome, nascimento, sexo, telefone)
    cursor.execute(sql, valores)
    con.commit()
    print("Aluno cadastrado com sucesso!")
    con.close()

def listar_alunos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        print(aluno)
    con.close()

def atualizar_aluno(id, novo_nome):
    con = conectar()
    cursor = con.cursor()
    sql = "UPDATE alunos SET nome = %s WHERE id = %s"
    valores = (novo_nome, id)
    cursor.execute(sql, valores)
    con.commit()
    print("Aluno atualizado com sucesso!")
    con.close()

def deletar_aluno(id):
    con = conectar()
    cursor = con.cursor()
    sql = "DELETE FROM alunos WHERE id = %s"
    cursor.execute(sql, (id,))
    con.commit()
    print("Aluno deletado com sucesso!")
    con.close()

# Menu no terminal
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Deletar aluno")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        nascimento = input("Nascimento (YYYY-MM-DD): ")
        sexo = input("Sexo (M/F): ")
        telefone = input("Telefone: ")
        criar_aluno(nome, sobrenome, nascimento, sexo, telefone)
    elif op == "2":
        listar_alunos()
    elif op == "3":
        id = int(input("ID do aluno: "))
        novo_nome = input("Novo nome: ")
        atualizar_aluno(id, novo_nome)
    elif op == "4":
        id = int(input("ID do aluno: "))
        deletar_aluno(id)
    elif op == "0":
        break
    else:
        print("Opção inválida")
