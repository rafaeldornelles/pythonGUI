from Dao.LivroDAO import LivroDAO
from Dao.UsuarioDAO import UsuarioDAO
from Model.Livro import Livro
from View.LivroCadastroView import LivroCadastroView
from View.LivroDetalheView import LivroDetalheView
from View.LivroListaView import LivroListaView
from View.LivroMenuView import LivroMenuView
from View.LivroPesquisarView import LivroPesquisarView
from View.UsuarioDetalheView import UsuarioDetalheView
from View.UsuarioListaView import UsuarioListaView
from View.UsuarioPesquisarView import UsuarioPesquisarView


class LivrosController:

    dao = LivroDAO()
    todosLivros = dao.todos()

    def __init__(self):
        event, _ = LivroMenuView().show()

        while True:
            if event == "listar":
                self.listarLivros(self.todosLivros)
            elif event == "pesquisar":
                self.pesquisarLivro()
            elif event == "devolver":
                self.devolverLivro()
            elif event == "cadastrar":
                self.cadastrarLivro()

    def listarLivros(self, livros):
        event, _ = LivroListaView(livros).show()

        for livro in livros:
            if event == livro.getId():
                LivroDetalheView(livro).show()

    def pesquisarLivro(self):
        while True:
            view = LivroPesquisarView()
            event, values = view.show()

            if event == None:
                break
            elif values["pesquisa"] == "":
                view.campoVazio()
            else:
                pesquisa = values["pesquisa"]
                result = None
                if event == "porTitulo":
                    result = self.dao.pesquisarPorTitulo(pesquisa)
                elif event == "porAutor":
                    result = self.dao.pesquisarPorAutor(pesquisa)
                elif event == "porAno":
                    result = self.dao.pesquisarPorAno(pesquisa)

                if len(result) == 0:
                    view.nenhumEncontrado()
                elif len(result) == 1:
                    self.mostrarLivro(result[0])
                elif len(result) >1:
                    self.listarLivros(result)
                break

    def efetuarDevolucao(self,livro:Livro):
        livro.setStatus(True)
        livro.setLocatario(None)
        self.dao.atualizar(livro)
        self.todosLivros = self.dao.todos()

    def devolverLivro(self):
        #escolher o usuario
        usuarioDao = UsuarioDAO()
        while True:
            view = UsuarioPesquisarView("Digite o nome do usuário que vai devolver o livro")
            event, values = view.show()
            if event=="None":
                break
            elif values["nome"] == "":
                view.errorPopUp()
                continue

            result = usuarioDao.buscarPorNome(values["nome"])

            if len(result) == 0:
                view.nenhumEncontrado()
            elif len(result) == 1:
                self.mostraLivrosParaDevolucao(result[0])
                break
            else:
                event, values = UsuarioListaView(result, "Escolher").show()
                if event == None:
                    break

                usuario = usuarioDao.pesquisarPorId(event)
                self.mostraLivrosParaDevolucao(usuario)
                break


    def mostraLivrosParaDevolucao(self, usuario):
        detalheView = UsuarioDetalheView(usuario, True)
        event, result = detalheView.show()
        if event == None:
            return

        for livro in self.todosLivros:
            if event == livro.getId():
                self.efetuarDevolucao(livro)
                detalheView.confirmaDevolucao()
                break

    def cadastrarLivro(self):
        while True:
            view = LivroCadastroView()
            event, values = view.show()

            if event == None:
                break

            if values["titulo"] == None or values["autor"] == None or values["ano"] == None:
                view.campoVazio()
                continue

            livro = Livro(values["titulo"], values["autor"], values["ano"])
            self.dao.inserir(livro)
            self.todosLivros = self.dao.todos()
            view.confirmaCadastro()
            break

    def mostrarLivro(self, livro):
        while True:
            view = LivroDetalheView(livro)
            event, result = view.show()

            if event == None:
                break

            elif event == "editar":
                self.editarLivro(livro)
                break

            elif event == "excluir":
                self.excluirLivro(livro, view)
                break

    def editarLivro(self, livro):
        while True:
            view = LivroCadastroView(livro)
            event, values = view.show()
            if event == None:
                break

            if values["titulo"] == "" or values["autor"] == "" or values["ano"] == "":
                view.campoVazio()
                continue

            livro.setTitulo(values["titulo"])
            livro.setAutor(values["autor"])
            livro.setAno(values["ano"])

            self.dao.atualizar(livro)
            self.todosLivros = self.dao.todos()
            view.confirmaCadastro()
            break

    def excluirLivro(self, livro, view:LivroDetalheView):
        self.dao.deletar(livro)
        self.todosLivros = self.dao.todos()
        view.confirmaExclusao()





















