from entidades.Documento import Documento


class Cpf(Documento):
    def __init__(self, cpf: str, nome: str):
        super().__init__(cpf, nome)
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def cpf(self, nome: str):
        self.__nome = nome

