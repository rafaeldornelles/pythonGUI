import PySimpleGUI as gui
from Model.Livro import Livro


class LivroMenuView:
    def __init__(self, lista:[Livro]):
        gui.theme("black")
        layout = [[gui.Text("Livros:")]]

        for livro in lista:
            layout.append(
                [gui.Text(livro.getTitulo()), gui.Button("Ver mais")]
            )

        layout.append([gui.Button("Voltar")])

        self.window = gui.Window("Livros", layout)

    def show(self):
        self.window.read()



LivroMenuView([Livro("Bras cubas", "Machado", 1999, True), Livro("Quincas", "Machado", 1998, False)]).show()
