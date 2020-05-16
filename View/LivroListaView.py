import PySimpleGUI as gui
from Model.Livro import Livro


class LivroListaView:
    def __init__(self, lista:[Livro]):
        gui.theme("black")
        layout = []

        if len(lista) == 0:
            layout.append([gui.Text("Nenhum Livro cadastrado")])

        for i, livro in enumerate(lista):
            layout.append(
                [gui.Text(f"{i + 1}. {livro.getTitulo().title()}"), gui.Button("Ver mais", key=livro.getId())],
            )

        layout.append([gui.Button("Voltar", key=None)])

        self.window = gui.Window("Livros", layout)

    def show(self):
        event, values = self.window.read()
        self.window.close()
        return event, values



