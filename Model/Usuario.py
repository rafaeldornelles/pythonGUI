class Usuario:
    def __init__(self, nome, id=0):
        self.__id = id
        self.__nome = nome

    def getId(self) -> int:
        return self.__id

    def getNome(self) -> str:
        return  self.__nome

    def setId(self, id):
        self.__id = id

    def setNome(self, nome):
        self.__nome = nome