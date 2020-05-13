import PySimpleGUI as gui


class RootMenuView:

    def __init__(self):
        gui.theme("black")
        layout = [
            [gui.Text("Biblioteca", justification="center", auto_size_text=True)],
            [gui.Text("Escolha a opção: ")],
            [gui.Button("Usuários", key="usuarios"), gui.Button("Livros", key="livros")]
        ]
        self.window = gui.Window("Biblioteca", layout)
    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values

