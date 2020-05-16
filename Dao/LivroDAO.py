from Db.DBConnector import DBConnector
from Db.Parser.LivroParser import LivroParser
from Model.Livro import Livro
from Model.Usuario import Usuario


class LivroDAO:
    db = DBConnector()

    def todos(self):
        query = "SELECT id, titulo, autor, ano, status, locatario_id \
        FROM Livro"

        result = self.db.query(query)

        return LivroParser.toLivro(result)

    def inserir(self, livro:Livro):
        query = "INSERT INTO Livro (titulo, autor, ano, status, locatario_id) VALUES (?,?,?,?,?)"
        params = (livro.getTitulo(), livro.getAutor(), livro.getAno(), livro.getStatus(), None)

        newId = self.db.exec(query, params)
        livro.setId(newId)


    def atualizar(self, livro:Livro):
        query = "UPDATE Livro SET titulo = ?, autor = ?, ano = ?, status = ?, locatario_id = ? WHERE id = ?"
        locatario = livro.getLocatario().getId() if livro.getLocatario() != None else None
        params = (livro.getTitulo(), livro.getAutor(), livro.getAno(), livro.getStatus(), locatario, livro.getId())

        self.db.exec(query, params)


    def deletar(self, livro):
        query = "DELETE FROM Livro WHERE id = ?"
        params = (livro.getId(), )

        self.db.exec(query, params)

    def pesquisarPorTitulo(self, titulo):
        query = "SELECT id, titulo, autor, ano, status, locatario_id FROM Livro WHERE titulo LIKE ?"
        params = (titulo + "%", )

        result = self.db.query(query, params)
        return LivroParser.toLivro(result)

    def pesquisarPorAutor(self, autor):
        query = "SELECT id, titulo, autor, ano, status, locatario_id FROM Livro WHERE autor LIKE ?"
        params = (autor + "%",)

        result = self.db.query(query, params)
        return LivroParser.toLivro(result)

    def pesquisarPorAno(self, ano):
        query = "SELECT id, titulo, autor, ano, status, locatario_id FROM Livro WHERE ano = ?"
        params = (ano, )

        result = self.db.query(query, params)
        return LivroParser.toLivro(result)

    def livrosRetiradosPor(self, usuario:Usuario):
        query = "SELECT id, titulo, autor, ano, status, locatario_id FROM Livro WHERE locatario_id = ?"
        params = (usuario.getId(), )

        result = self.db.query(query, params)
        try:
            return LivroParser.toLivro(result)
        except:
            return None

    def consultarEmprestimoPorUsuario(self, usuario):
        query = "SELECT l.id, l.titulo, l.autor, l.ano, l.status, l.locatario_id FROM Livro l JOIN Usuario u ON l.locatario_id = u.id WHERE u.id = ?"
        params = (usuario.getId(), )

        result = self.db.query(query, params)
        return LivroParser.toLivro(result)



