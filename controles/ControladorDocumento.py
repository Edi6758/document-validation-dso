from entidades.Cpf import Cpf
from entidades.Identidade import Identidade
from entidades.TituloEleitor import TituloEleitor
from telas.TelaDocumento import TelaDocumento
from telas.TelaSistema import TelaSistema
from controles.ControladorUsuario import ControladorUsuario
import pytesseract
import cv2
import re

class ControladorDocumento:
    def __init__(self):
        self.__cpfs = []
        self.__rg = []
        self.__titulo_eleitor = []
        self.__teladocumento = TelaDocumento()
        self.__telasistema = TelaSistema()
        self.__controladorusuario = ControladorUsuario()


    #VERIFICAR COMO ESTÁ O CADASTRO DE DOCUMENTO
    def cadastro_cpf(self):
        dados_cpf = self.__teladocumento.cadastrar_cpf()
        cpfx = Cpf(dados_cpf['cpf'], dados_cpf['nome'])
        self.__cpfs.append(cpfx)
        print(self.__cpfs)
        self.lista_cpf_cadastrados()
        self.validar_cpf()
        return self.__telasistema.mostrar_opcoes_apos_login()

    def lista_cpf_cadastrados(self):
        cpf_cadatrados = []
        for cpf in self.__cpfs:
            cpf_cadatrados.append(cpf.cpf)
        print(cpf_cadatrados)

    def validar_cpf(self):
        cpf_cadatrados = []
        for cpf in self.__cpfs:
            cpf_cadatrados.append(cpf.cpf)
        print(cpf_cadatrados[0])
        imagem = cv2.imread(cpf_cadatrados[0])
        caminho = r"C:\Program Files\Tesseract-OCR"

        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(imagem)

        filtroCpf = re.compile(r'\d{3}\.\d{3}\.\d{3}\-\d{2}')
        tratativaCpf = filtroCpf.findall(texto)
        valorCpf = "".join(tratativaCpf).replace('.','').replace('-','')

        self.__controladorusuario.funcao_usuarios_cadastrados_cpf()

        print("tipo do validador ",type(valorCpf))
        print("valor do validador ", valorCpf)
        self.__controladorusuario.funcao_usuarios_cadastrados_cpf()
        print(self.__controladorusuario.funcao_usuarios_cadastrados_cpf())

        for i in self.__controladorusuario.funcao_usuarios_cadastrados_cpf():
            if(i == valorCpf):
                print("finalmente...")
            else:
                print("me mata")


    def abre_menu_documento(self):
        opcoes_documento = self.__teladocumento.menu_documentos()
        if(opcoes_documento == 1):
            self.cadastro_cpf()


