from PySimpleGUI import PySimpleGUI as gui
class LivroCadastroView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Cadastro de Livro")],
            [gui.Text("Título:")],
            [gui.InputText(key="titulo")],
            [gui.Text("Autor:")],
            [gui.InputText(key="autor")],
            [gui.Text("Ano:")],
            [gui.InputText(key="ano")],
            [gui.Button("Cadastrar", key="cadastrar")],
            [gui.Button("Voltar", key=None)]
        ]

        self.window = gui.Window("Cadastro de Usuário", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values


