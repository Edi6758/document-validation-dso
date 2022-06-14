from entidades.Documento import Documento

class TituloEleitor(Documento):
    def __init__(self, titulo_eleitor:str, nome:str):
        super().__init__(titulo_eleitor, nome)
        self.__titulo_eleitor = titulo_eleitor
        self.__nome = nome

    @property
    def titulo_eleitor(self):
        return self.__titulo_eleitor

    @titulo_eleitor.setter
    def nome(self, titulo_eleitor):
        self.__titulo_eleitor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome
