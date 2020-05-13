import PySimpleGUI as gui
class UsuarioCadastroView:
    def __init__(self, usuario = None):
        gui.theme("black")

        nome = ""
        try:
            nome = usuario.getNome()
        except:
            pass

        layout = [
            [gui.Text("Cadastro de Usuário")],
            [gui.Text("Nome:")],
            [gui.InputText(default_text=nome, key="nome")],
            [gui.Button("Cadastrar", key="cadastrar")],
            [gui.Button("Voltar", key="voltar")]
        ]

        self.window = gui.Window("Cadastro de Usuário", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values

    def errorPopUp(self):
        gui.popup("Preencha todos os campos")
    def confirmationPopUp(self):
        gui.popup("Usuário Cadastrado com sucesso")
