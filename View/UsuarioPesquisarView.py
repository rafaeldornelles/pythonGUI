import PySimpleGUI as gui
class UsuarioPesquisarView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Pesquisar Usuário")],
            [gui.InputText(key="nome")],
            [gui.Button("Pesquisar por Nome", key="pesquisar")],
            [gui.Button("Voltar", key="voltar")]
        ]

        self.window = gui.Window("Usuários", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values

    def errorPopUp(self):
        gui.popup("Insira um valor no campo de pesquisa")

    def nenhumEncontrado(self):
        gui.popup("Nenhum usuário encontrado")



