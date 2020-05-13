from View.LivroMenuView import LivroMenuView


class LivrosController:
    def __init__(self):
        menuView = LivroMenuView()
        cadastroView = LivroCadastroView()
        detalheView = LivroDetalheView()
        listaView = LivroListaView()
        pesquisaView = LivroPesquisaView()