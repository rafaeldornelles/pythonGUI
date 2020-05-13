import PySimpleGUI as gui
class LivroPesquisarView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Pesquisar Usuário")],
            [gui.InputText(key="pesquisa")],
            [gui.Button("Pesquisar por Título", key="porTitulo")],
            [gui.Button("Pesquisar por Autor", key="porAutor")],
            [gui.Button("Pesquisar por Ano", key="porAno")],
            [gui.Button("Voltar", key=None)]
        ]

        self.window = gui.Window("Usuários", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values



