from PySimpleGUI import PySimpleGUI as gui
class LivroCadastroView:
    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Cadastro de Livro")],
            [gui.Text("Título:")],
            [gui.InputText()],
            [gui.Text("Autor:")],
            [gui.InputText()],
            [gui.Text("Ano:")],
            [gui.InputText()],
            [gui.Button("Cadastrar")],
            [gui.Button("Voltar")]
        ]

        self.window = gui.Window("Cadastro de Usuário", layout)

    def show(self):
        self.window.read()


LivroCadastroView().show()
