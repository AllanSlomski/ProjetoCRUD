from tkinter import *
import alunos

janela = Tk()
janela.geometry('450x450')
janela.title('Sistema de Cadastro de Alunos')


def limpar_ui():
    for widget in janela.winfo_children():
        widget.destroy()


def cadastrar():
    limpar_ui()
    labelNome = Label(janela, text='Nome:')
    labelNome.grid(row=1, column=1, padx='10', pady='10')
    entryNome = Entry(janela, state='normal')
    entryNome.grid(row=1, column=2, padx='10', pady='10')

    labelIdade = Label(janela, text='Idade:')
    labelIdade.grid(row=2, column=1, padx='10', pady='10')
    entryIdade = Entry(janela, state='normal')
    entryIdade.grid(row=2, column=2, padx='10', pady='10')

    labelTurma = Label(janela, text='Turma:')
    labelTurma.grid(row=3, column=1, padx='10', pady='10')
    entryTurma = Entry(janela, state='normal')
    entryTurma.grid(row=3, column=2, padx='10', pady='10')

    botaoCadastrarBd = Button(janela, text='Cadastrar', command=lambda: alunos.criarAluno(entryNome.get(),
                                                                                          entryIdade.get(),
                                                                                          entryTurma.get()))
    botaoCadastrarBd.grid(row=4, column=3, padx='10', pady='10')

    botaoVoltar= Button(janela, text='Voltar', command=start)
    botaoVoltar.grid(row=4, column=2, padx='10', pady='10')


def pesquisar():
    limpar_ui()

    labelId = Label(janela, text='ID:')
    labelId.grid(row=1, column=1, padx='10', pady='10')
    entryId = Entry(janela, state='normal')
    entryId.grid(row=1, column=2, padx='10', pady='10')

    botaoPesquisar = Button(janela, text='Pesquisar', command=lambda: alunos.Aluno.pesquisarDados(entryId.get()))
    botaoPesquisar.grid(row=2, column=3, padx='10', pady='10')

    botaoVoltar = Button(janela, text='Voltar', command=start)
    botaoVoltar.grid(row=2, column=2, padx='10', pady='10')


def deletar():
    limpar_ui()

    labelId = Label(janela, text='ID:')
    labelId.grid(row=1, column=1, padx='10', pady='10')
    entryId = Entry(janela, state='normal')
    entryId.grid(row=1, column=2, padx='10', pady='10')

    botaoDeletar = Button(janela, text='Deletar', command=lambda: alunos.Aluno.deletarDados(entryId.get()))
    botaoDeletar.grid(row=2, column=3, padx='10', pady='10')

    botaoVoltar = Button(janela, text='Voltar', command=start)
    botaoVoltar.grid(row=2, column=2, padx='10', pady='10')


def atualizar():
    limpar_ui()

    labelId = Label(janela, text='ID:')
    labelId.grid(row=1, column=1, padx='10', pady='10')
    entryId = Entry(janela, state='normal')
    entryId.grid(row=1, column=2, padx='10', pady='10')

    labelNome = Label(janela, text='Nome: ')
    labelNome.grid(row=2, column=1, padx='10', pady='10')
    entryNome = Entry(janela, state='normal')
    entryNome.grid(row=2, column=2, padx='10', pady='10')

    labelIdade = Label(janela, text='Idade: ')
    labelIdade.grid(row=3, column=1, padx='10', pady='10')
    entryIdade = Entry(janela, state='normal')
    entryIdade.grid(row=3, column=2, padx='10', pady='10')

    labelTurma = Label(janela, text='Turma: ')
    labelTurma.grid(row=4, column=1, padx='10', pady='10')
    entryTurma = Entry(janela, state='normal')
    entryTurma.grid(row=4, column=2, padx='10', pady='10')

    botaoAtualizar = Button(janela, text='Atualizar', command=lambda: alunos.Aluno.atualizarDados(entryId.get(),
                                                                                                  entryNome.get(),
                                                                                                  entryIdade.get(),
                                                                                                  entryTurma.get()))
    botaoAtualizar.grid(row=5, column=3, padx='10', pady='10')

    botaoVoltar = Button(janela, text='Voltar', command=start)
    botaoVoltar.grid(row=5, column=2, padx='10', pady='10')


def start():
    limpar_ui()

    botaoCadastrar = Button(janela, text='Cadastrar', command=cadastrar)
    botaoCadastrar.grid(row=2, column=3, padx='10', pady='10')

    botaoPesquisar = Button(janela, text='Pesquisar', command=pesquisar)
    botaoPesquisar.grid(row=3, column=3, padx='10', pady='10')

    botaoDeletar = Button(janela, text=' Deletar ', command=deletar)
    botaoDeletar.grid(row=4, column=3, padx='10', pady='10')

    botaoAtualizar = Button(janela, text='Atualizar', command=atualizar)
    botaoAtualizar.grid(row=5, column=3, padx='10', pady='10')


start()
janela.mainloop()
