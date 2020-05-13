import PySimpleGUI as gui
from Model.Livro import Livro


class LivroListaView:
    def __init__(self, lista:[Livro]):
        gui.theme("black")
        layout = [[gui.Text("Livros:")]]

        for livro in lista:
            layout.append(
                [gui.Text(livro.getTitulo()), gui.Button("Ver mais", key=livro.getId())]
            )

        layout.append([gui.Button("Voltar", key=None)])

        self.window = gui.Window("Livros", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values



