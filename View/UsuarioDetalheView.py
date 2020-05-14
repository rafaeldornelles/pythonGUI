import PySimpleGUI as gui

from Dao.LivroDAO import LivroDAO
from Model.Usuario import Usuario


class UsuarioDetalheView:
    def __init__(self, usuario:Usuario, devolver = False):
        emprestimos = LivroDAO().livrosRetiradosPor(usuario)
        layout = [
            [gui.Text(usuario.getNome())],
            [gui.Text("Empréstimos:")]
        ]

        if len(emprestimos) >0:
            for i,livro in enumerate(emprestimos):
                row = [gui.Text(f"{i}. {livro}")]
                if devolver:
                    row.append(gui.Button("Devolver", key=livro.getId()))

                layout.append(row)
        else:
            layout.append([gui.Text("nenhum livro retirado")])

        layout += [
            [gui.Button("Editar", key="editar")],
            [gui.Button("Excluir", key ="excluir")],
            [gui.Button("Voltar", key=None)]
        ] if not devolver else [gui.Button("Voltar", key=None)]

        self.window = gui.Window("Usuários", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values

    def confirmaExclusao(self):
        gui.popup("Usuário excluido")


    def confirmaDevolucao(self):
        gui.popup("Livro devolvido com sucesso")

