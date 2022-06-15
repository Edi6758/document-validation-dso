from entidades.Documento import Documento

class TituloEleitor(Documento):
    def __init__(self, titulo_eleitor: str, nome: str):
        super().__init__(titulo_eleitor, nome)
        self.__titulo_eleitor = titulo_eleitor
        self.__nome = "TITULO DE ELEITOR"

    @property
    def titulo_eleitor(self):
        return self.__titulo_eleitor

    @titulo_eleitor.setter
    def nome(self, titulo_eleitor: str):
        self.__titulo_eleitor = titulo_eleitor
