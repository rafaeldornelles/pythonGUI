from View.RootMenuView import RootMenuView
from Controller.UsuariosController import UsuariosController
from Controller.LivrosController import LivrosController

class RootMenuControloler:
    def __init__(self):
        while True:
            event, _ = RootMenuView().show()

            if event == "usuarios":
                UsuariosController()

            elif event == "livros":
                LivrosController()

            else:
                break


RootMenuControloler()