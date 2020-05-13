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
            [gui.Button("Editar", key="editar")],
            [gui.Button("Excluir", key="excluir")],
            [gui.Button("Voltar", key=None)]
        ]

        self.window = gui.Window("Livro", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values

