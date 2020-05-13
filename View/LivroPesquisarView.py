import PySimpleGUI as gui
class LivroPesquisarView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Pesquisar Usuário")],
            [gui.InputText()],
            [gui.Button("Pesquisar por Título")],
            [gui.Button("Pesquisar por Autor")],
            [gui.Button("Pesquisar por Ano")],
            [gui.Button("Voltar")]
        ]

        self.window = gui.Window("Usuários", layout)

    def show(self):
        self.window.read()



LivroPesquisarView().show()
