from entidades.Cpf import Cpf
from entidades.Identidade import Identidade
from entidades.TituloEleitor import TituloEleitor
from telas.TelaDocumento import TelaDocumento
from telas.TelaSistema import TelaSistema

class ControladorDocumento:
    def __init__(self):
        self.__cpfs = []
        self.__rg = []
        self.__titulo_eleitor = []
        self.__teladocumento = TelaDocumento()
        self.__telasistema = TelaSistema()

    #VERIFICAR COMO ESTÁ O CADASTRO DE DOCUMENTO
    def cadastro_cpf(self):
        dados_cpf = self.__teladocumento.cadastrar_cpf()
        cpfx = Cpf(dados_cpf['cpf'], dados_cpf['nome'])
        self.__cpfs.append(cpfx)
        return self.__telasistema.mostrar_opcoes_apos_login()


    def abre_menu_documento(self):
        opcoes_documento = self.__teladocumento.menu_documentos()
        if(opcoes_documento == 1):
            self.cadastro_cpf()
            print(self.__cpfs)

