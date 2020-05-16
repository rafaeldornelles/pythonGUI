from PySimpleGUI import PySimpleGUI as gui
class LivroCadastroView:
    def __init__(self, livro = None):
        gui.theme("black")
        titulo = ""
        autor = ""
        ano = ""
        try:
            titulo = livro.getTitulo()
            autor = livro.getAutor()
            ano = livro.getAno()
        except:
            pass

        layout = [
            [gui.Text("Cadastro de Livro")],
            [gui.Text("Título:")],
            [gui.InputText(default_text=titulo,key="titulo")],
            [gui.Text("Autor:")],
            [gui.InputText(default_text=autor,key="autor")],
            [gui.Text("Ano:")],
            [gui.InputText(default_text=ano,key="ano")],
            [gui.Button("Cadastrar", key="cadastrar")],
            [gui.Button("Voltar", key="voltar")]
        ]

        self.window = gui.Window("Cadastro de Usuário", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values

    def campoVazio(self):
        gui.popup("Preencha todos os campos")

    def confirmaCadastro(self):
        gui.popup("Livro adicionado com sucesso")


