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

    def abre_menu_dados_ou_documentos(self):
        self.__tela_sistema.mostrar_opcoes_apos_login()

    def abre_menu_dados(self):
        self.__tela_sistema.mostrar_opcoes_dados()

    def encerra(self):
        exit(0)

    def abre_tela(self):
        while True:
            funcao_escolhida = self.__tela_sistema.mostra_opcoes()
            if funcao_escolhida == 1:
                self.cadastra_usuario()
            elif funcao_escolhida == 2:
                if self.login_usuario():
                    while True:
                        opcao_pos_login = self.__tela_sistema.mostrar_opcoes_apos_login()
                        if opcao_pos_login == 1:
                            while True:
                                opcao_dados = self.__tela_sistema.mostrar_opcoes_dados()
                                if opcao_dados == 1:
                                    self.__controlador_usuario.lista_usuarios_cadastrados()
                                elif opcao_dados == 2:
                                    self.__controlador_usuario.altera_dados()
                                elif opcao_dados == 3:
                                    self.__controlador_usuario.exclui_conta()
                                elif opcao_dados == 0:
                                    break
                        elif opcao_pos_login == 2:
                            self.__controlador_usuario.abre_menu_documento()
                        elif opcao_pos_login == 0:
                            break
                else:
                    print('não foi possivel logar, tente novamente')
            elif funcao_escolhida == 0:
                break
            #else:
                #print('ESSA NÃO É UMA OPÇÃO VÁLIDA!!!')
