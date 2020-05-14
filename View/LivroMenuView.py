from PySimpleGUI import PySimpleGUI as gui
class LivroMenuView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Listar", key="listar")],
            [gui.Button("Pesquisar", key="pesquisar")],
            [gui.Button("Devolver", key="devolver")],
            [gui.Button("Cadastrar", key="cadastrar")],
            [gui.Button("Voltar", key=None)]
        ]

        self.window = gui.Window("Livros", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values
