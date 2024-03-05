import sqlite3

con = sqlite3.connect('alunos.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS alunos
                (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade TEXT, turma TEXT)""")
class Aluno:
    def __init__(self, nome, idade, turma):
        self.id = cur.execute('''SELECT id FROM alunos (id)''')
        self.nome = nome
        self.idade = idade
        self.turma = turma

    def mostrarDados(self):
        print(self.nome, self.idade, self.turma)

    def inserirDados(self):
        cur.execute('''INSERT INTO alunos (nome, idade, turma) VALUES (?, ?, ?)''', (self.nome, self.idade, self.turma))
        con.commit()

    def atualizarDados(self):
        cur.execute('''UPDATE alunos SET (nome, idade, turma) VALUES (?, ?, ?) WHERE (id) VALUES (?)''')
        con.commit()

    @staticmethod
    def pesquisarDados(Id):
        cur.execute('''SELECT * FROM alunos WHERE id=?''', (Id))
        aluno = cur.fetchone()
        con.commit()
        if aluno:
            print(aluno)
            return aluno
        else:
            msg = 'Não há dados cadastrados.'
            print(msg)
            return msg


def criarAluno(nome, idade, turma):
    novoAluno = Aluno(nome, idade, turma)
    novoAluno.mostrarDados()
    novoAluno.inserirDados()

def atualizarAluno(id, nome, idade, turma):
    novoAluno = Aluno(id, nome, idade, turma)
    novoAluno.mostrarDados()
    novoAluno.atualizarDados()

def pesquisarAluno(Id):
    novoAluno = Aluno()
    #id.mostrarDados()
    novoAluno.pesquisarDados(Id)

