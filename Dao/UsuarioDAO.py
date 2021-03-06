from typing import List

from Db.DBConnector import DBConnector
from Db.Parser.UsuarioParser import UsuarioParser
from Model.Usuario import Usuario


class UsuarioDAO:
    def __init__(self):
        self.db = DBConnector()

    def todos(self) -> List[Usuario]:
        query = "SELECT id, nome FROM Usuario"
        result = self.db.query(query)
        return UsuarioParser.toUsuario(result)

    def inserir(self, usuario: Usuario):
        query = "INSERT INTO Usuario (nome) VALUES (?)"
        params = (usuario.getNome(),)

        newId = self.db.exec(query, params)
        usuario.setId(newId)

    def atualizar(self, usuario: Usuario):
        query = "UPDATE Usuario SET nome = ? WHERE id = ?"
        params = (usuario.getNome(), usuario.getId())

        self.db.exec(query, params)

    def deletar(self, usuario: Usuario):
        query = "DELETE FROM Usuario WHERE id = ?"
        params = (usuario.getId(),)

        self.db.exec(query, params)

    def buscarPorNome(self, nome: str):
        nome = nome.capitalize() + "%"
        query = "SELECT id, nome FROM Usuario WHERE nome LIKE ?"
        params = (nome,)

        result = self.db.query(query, params)

        return UsuarioParser.toUsuario(result)

    def nenhumCadastrado(self):
        return len(self.todos()) == 0


    def pesquisarPorId(self, id):
        query = "SELECT id, nome FROM Usuario WHERE id = ?"
        params = (id, )
        result = self.db.query(query, params)

        return UsuarioParser.toUsuario(result)[0]
