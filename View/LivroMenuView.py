from PySimpleGUI import PySimpleGUI as gui
class LivroMenuView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Listar")],
            [gui.Button("Pesquisar")],
            [gui.Button("Devolver")],
            [gui.Button("Doar")],
            [gui.Button("Voltar")]
        ]

        self.window = gui.Window("Livros", layout)

    def show(self):
        self.window.read()



LivroMenuView().show()
