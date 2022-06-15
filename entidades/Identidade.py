from entidades.Documento import Documento


class Identidade(Documento):
    def __init__(self, rg: str, nome: str):
        super().__init__(rg, nome)
        self.__rg = rg
        self.__nome = "IDENTIDADE"

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg: str):
        self.__rg = rg
