from entidades.Cpf import Cpf
from entidades.Identidade import Identidade
from entidades.TituloEleitor import TituloEleitor
from telas.TelaDocumento import TelaDocumento

class ControladorDocumento:
    def __init__(self):
        self.__cpfs = []
        self.__rg = []
        self.__titulo_eleitor = []
        self.__teladocumento = TelaDocumento()

    #VERIFICAR COMO ESTÁ O CADASTRO DE DOCUMENTO
    def cadastro_documento(self):
        # documentos_cadastrados = self.__teladocumento()
        # cpf = Cpf(documentos_cadastrados['cpf'])
        # rg = Identidade(documentos_cadastrados['rg'])
        # titulo_eleitor = TituloEleitor(documentos_cadastrados['titulo_eleitor'])
        #
        # print(cpf, rg, titulo_eleitor)
        dados_cpf = self.__teladocumento.cadastrar_cpf()
        cpfx = Cpf(dados_cpf['cpf'], dados_cpf['nome'])
        self.__cpfs.append(cpfx)
        print(self.__cpfs)

    #############################################
