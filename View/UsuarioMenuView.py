import PySimpleGUI as gui
class UsuarioMenuView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Usuários")],
            [gui.Button("Cadastrar", key="cadastro")],
            [gui.Button("Listar", key="lista")],
            [gui.Button("Pesquisar", key="pesquisa")],
            [gui.Button("Voltar", key=None)]
        ]

        self.window = gui.Window("Usuários", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values



