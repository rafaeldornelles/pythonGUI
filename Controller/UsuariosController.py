from Dao.UsuarioDAO import UsuarioDAO
from Model.Usuario import Usuario
from View.UsuarioCadastroView import UsuarioCadastroView
from View.UsuarioDetalheView import UsuarioDetalheView
from View.UsuarioMenuView import UsuarioMenuView
from View.UsuarioListaView import UsuarioListaView
from View.UsuarioPesquisarView import UsuarioPesquisarView


class UsuariosController:


    def __init__(self):
        self.dao = UsuarioDAO()
        self.todosUsuarios = self.dao.todos()

        event, _ = UsuarioMenuView().show()

        if event == "cadastro":
            self.cadastrarUsuario()
        elif event == "lista":
            self.listarUsuarios()
        elif event == "pesquisa":
            self.pesquisarUsuario()

    def cadastrarUsuario(self):
        view = UsuarioCadastroView()

        while True:
            event, values = view.show()
            if event == "cadastrar":
                if values["nome"] != None and values["nome"] != "":
                    usuario = Usuario(values["nome"])
                    self.dao.inserir(usuario)
                    self.todosUsuarios.append(usuario)
                    view.confirmationPopUp()
                    break
                view.errorPopUp()
            print("a")
            break



    def listarUsuarios(self, usuarios = None):
        if usuarios == None:
            usuarios = self.dao.todos()
        event, _ = UsuarioListaView(usuarios).show()

        for usuario in usuarios:
            if event == usuario.getId():
                self.mostrarDetalhe(usuario)



    def mostrarDetalhe(self, usuario):
        view = UsuarioDetalheView(usuario)
        event, _ = view.show()

        if event == "editar":
            self.editarUsuario(usuario)

        if event == "excluir":
            self.excluirUsuario(usuario)
            view.confirmaExclusao()


    def pesquisarUsuario(self):
        while True:
            pesquisaView = UsuarioPesquisarView()
            event, values = pesquisaView.show()

            if event == None or event == "":
                break

            elif values["nome"] != None and values["nome"] != "":
                usuarios = self.dao.buscarPorNome(values["nome"])
                if len(usuarios) == 0:
                    pesquisaView.nenhumEncontrado()

                elif len(usuarios) == 1:
                    self.mostrarDetalhe(usuarios[0])

                else:
                    self.listarUsuarios(usuarios)

                break
            else:
                pesquisaView.errorPopUp()

    def editarUsuario(self, usuario):
        while True:
            view = UsuarioCadastroView(usuario)
            event, values = view.show()
            if event == "cadastrar":
                if values["nome"] != "":
                    usuario.setNome(values["nome"])
                    self.dao.atualizar(usuario)
                    view.confirmationPopUp()
                    break
                else:
                    view.__init__()
            else:
                break

    def excluirUsuario(self, usuario):
        self.dao.deletar(usuario)
        self.todosUsuarios = self.dao.todos()




