from typing import Tuple, List

from Dao import UsuarioDAO
from Model.Livro import Livro


class LivroParser:
    @staticmethod
    def toLivro(lista: List[Tuple]) -> List[Livro]:
        livros = []
        for tupla in lista:
            id:int = tupla[0]
            titulo:str = tupla[1]
            autor:str = tupla[2]
            ano:int = tupla[3]
            status:bool = tupla[4]
            locatario_id:int = tupla[5]
            locatario = UsuarioDAO().pesquisarPorId(locatario_id)

            livro = Livro(titulo, autor, ano, status, locatario, id)
            livros.append(livro)

        return livros

