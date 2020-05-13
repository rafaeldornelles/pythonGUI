from typing import Tuple, List

from Model.Usuario import Usuario


class UsuarioParser:
    @staticmethod
    def toUsuario(lista:List[Tuple]) -> List[Usuario]:
        usuarios = []
        for tupla in lista:
            id = tupla[0]
            nome = tupla[1]

            usuario = Usuario(nome, id)
            usuarios.append(usuario)

        return usuarios
