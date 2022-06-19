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
        funcao_escolhida = self.__tela_sistema.mostra_opcoes()
        if funcao_escolhida == 1:
            self.cadastra_usuario()
            self.inicia_sistema()
        elif funcao_escolhida == 2:
            if self.login_usuario():
                opcao_pos_login = self.__tela_sistema.mostrar_opcoes_apos_login()
                if opcao_pos_login == 1:
                    opcao_dados = self.__tela_sistema.mostrar_opcoes_dados()
                    if opcao_dados == 1:
                        print('Listar usuários')
                        self.abre_menu_dados()
                    elif opcao_dados == 2:
                        print('Alterar dados usuario')
                        self.abre_menu_dados()
                    elif opcao_dados == 3:
                        print('Excluir conta')
                        self.abre_menu_dados()
                    elif opcao_dados == 0:
                        self.abre_menu_dados_ou_documentos()
                elif opcao_pos_login == 2:
                    self.__controlador_documento.abre_menu_documento()
                elif opcao_pos_login == 0:
                    return
            else:
                print('Não foi possivel logar, tente novamente!')
                self.inicia_sistema()
        elif funcao_escolhida == 0:
            self.encerra()
        else:
            print('ESSA NÃO É UMA OPÇÃO VÁLIDA!!!')
            self.inicia_sistema()
