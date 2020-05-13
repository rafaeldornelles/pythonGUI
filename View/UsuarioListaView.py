import PySimpleGUI as gui

from Model.Usuario import Usuario


class UsuarioListaView:
    def __init__(self, lista):
        gui.theme("black")
        layout = []

        if len(lista) == 0:
            layout.append([gui.Text("Nenhum Usuário cadastrado")])

        for i, usuario in enumerate(lista):
            layout.append(
                [gui.Text(f"{i}. {usuario.getNome().title()}"), gui.Button("Ver mais", key=usuario.getId())],
            )

        layout.append([gui.Button("Voltar")])

        self.window = gui.Window("Usuários", layout)

    def show(self):
        event, values =  self.window.read()
        self.window.close()
        return event, values


