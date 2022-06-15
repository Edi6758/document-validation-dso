from telas.TelaSistema import TelaSistema
from controles.ControladorUsuario import ControladorUsuario
from telas.TelaDocumento import TelaDocumento
from controles.ControladorDocumento import  ControladorDocumento


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuario = ControladorUsuario()
        self.__tela_documento = TelaDocumento()
        self.__controlador_documento = ControladorDocumento()

    def inicia_sistema(self):
        self.abre_tela()

    def cadastra_usuario(self):
        self.__controlador_usuario.cadastro_usuario()

    def login_usuario(self):
        return self.__controlador_usuario.login_usuario()

    def validacao(self):
        pass

    def encerra(self):
        exit(0)

    def abre_tela(self):
        funcao_escolhida = self.__tela_sistema.mostra_opcoes()
        if funcao_escolhida == 1:
            self.cadastra_usuario()
            self.inicia_sistema()
        elif funcao_escolhida == 2:
            if self.login_usuario():
                #printar opções de cadastro ou documento
                self.__controlador_documento.cadastro_documento()

        elif funcao_escolhida == 0:
            self.encerra()
        else:
            print('ESSA NÃO É UMA OPÇÃO VÁLIDA!!!')
            self.inicia_sistema()
