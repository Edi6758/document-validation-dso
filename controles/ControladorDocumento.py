from telas.TelaDocumento import TelaDocumento
from telas.TelaSistema import TelaSistema

class ControladorDocumento:
    def __init__(self):
        self.__cpfs = []
        self.__rg = []
        self.__titulo_eleitor = []
        self.__teladocumento = TelaDocumento()
        self.__telasistema = TelaSistema()



