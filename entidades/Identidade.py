from documento import Documento

class Identidade(Documento):
    def __init__(self, rg:str, nome:str):
        super().__init__(rg,nome)
        self.__rg = rg
        self.__nome = nome

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, cpf:str):
        self.__rg = rg

    @property
    def nome(self):
        return nome.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome