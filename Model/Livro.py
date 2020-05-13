from Model import Usuario


class Livro:
    def __init__(self, titulo:str, autor:str, ano:int, status = True, locatario:Usuario= None, id:int=-1):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        # Ao cadastrar o livro, seu status será disponível e ele não terá nenhum locatário
        self.__status = status #True = disponivel. False = indisponivel
        self.__locatario = locatario


    def getId(self):
        return self.__id

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAno(self):
        return self.__ano

    def getStatus(self):
        return self.__status

    def getLocatario_id(self):
        return self.__locatario

    def setId(self, id):
        self.__id = id

    def setStatus(self, status:bool):
        self.__status = status

    def setLocatario(self, locatario):
        self.__locatario = locatario

    def __str__(self):
        return f"{self.getTitulo()}, de {self.getAutor()} ({self.getAno()})"
