from PySimpleGUI import PySimpleGUI as gui

from Model.Livro import Livro


class LivroDetalheView:
    def __init__(self, livro: Livro):
        layout = [
            [gui.Text(livro.getTitulo())],
            [gui.Text("Autor:"), gui.Text(livro.getAutor())],
            [gui.Text("Ano:"), gui.Text(livro.getAno())]
        ]

        layout += [
            [gui.Button("Editar")],
            [gui.Button("Excluir")],
            [gui.Button("Voltar")]
        ]

        self.window = gui.Window("Livro", layout)

    def show(self):
        self.window.read()

LivroDetalheView(Livro("bras cubas", "machado", 1989)).show()
