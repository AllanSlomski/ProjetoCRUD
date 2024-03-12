import sqlite3
from tkinter import *

con = sqlite3.connect('alunos.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS alunos
                (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade TEXT, turma TEXT)""")
class Aluno:
    def __init__(self, nome, idade, turma):
        self.nome = nome
        self.idade = idade
        self.turma = turma


    def inserirDados(self):
        cur.execute('''INSERT INTO alunos (nome, idade, turma) VALUES (?, ?, ?)''', (self.nome, self.idade, self.turma))
        con.commit()


    @staticmethod
    def atualizarDados(Id, nome, idade, turma):
        cur.execute('''UPDATE alunos SET nome=?, idade=?, turma=? WHERE id=?''', (nome, idade, turma, Id))
        con.commit()

    @staticmethod
    def pesquisarDados(Id):
        cur.execute('''SELECT * FROM alunos WHERE id=?''', (Id))
        aluno = cur.fetchone()
        con.commit()
        if aluno:
            janela = Tk()
            labelAluno = Label(janela, text=f'{aluno}')
            labelAluno.grid(row=1, column=1, padx='15', pady='15')
            return aluno
        else:
            msg = 'Não há dados cadastrados.'
            janela = Tk()
            labelNada = Label(janela, text=f'{msg}')
            labelNada.grid(row=1, column=1, padx='15', pady='15')
            return msg

    @staticmethod
    def deletarDados(Id):
        cur.execute('''DELETE FROM alunos WHERE id=?''', (Id))
        aluno = con.commit()
        if aluno:
            janela = Tk()
            labelAluno = Label(janela, text=f'{aluno[1]} deletado.')
            labelAluno.grid(row=1, column=1, padx='15', pady='15')
            return aluno
        else:
            msg = 'Não há dados cadastrados.'
            janela = Tk()
            labelNada = Label(janela, text=f'{msg}')
            labelNada.grid(row=1, column=1, padx='15', pady='15')
            print(msg)
            return msg


def criarAluno(nome, idade, turma):
    novoAluno = Aluno(nome, idade, turma)
    novoAluno.inserirDados()


def atualizarAluno(Id, nome, idade, turma):
    novoAluno = Aluno()
    novoAluno.atualizarDados(Id, nome, idade, turma)


def pesquisarAluno(Id):
    novoAluno = Aluno()
    novoAluno.pesquisarDados(Id)


def deletarAluno(Id):
    novoAluno = Aluno()
    novoAluno.deletarDados(Id)
