from telas.TelaSistema import TelaSistema
from controles.ControladorUsuario import ControladorUsuario
from telas.TelaDocumento import TelaDocumento
from controles.ControladorDocumento import ControladorDocumento


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

    def login_admin(self):
        return self.__controlador_usuario.login_admin()

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
                if self.__controlador_usuario.login_admin():
                    while True:
                        opcao_pos_login_admin = self.__tela_sistema.mostra_opcoes_apos_login_admin()
                        if opcao_pos_login_admin == 1:
                            while True:
                                opcoes_menu_dados_admin = self.__tela_sistema.mostrar_opcoes_dados_admin()
                                if opcoes_menu_dados_admin == 1:
                                    self.__controlador_usuario.lista_usuarios_cadastrados()
                                elif opcoes_menu_dados_admin == 2:
                                    self.__controlador_usuario.listar_cpfs_cadastrados()
                                elif opcoes_menu_dados_admin == 3:
                                    self.__controlador_usuario.listar_emails_cadastrados()
                                elif opcoes_menu_dados_admin == 0:
                                    break
                        elif opcao_pos_login_admin == 0:
                            break
                elif self.login_usuario():
                    while True:
                        opcao_pos_login = self.__tela_sistema.mostrar_opcoes_apos_login()
                        if opcao_pos_login == 1:
                            while True:
                                opcao_dados = self.__tela_sistema.mostrar_opcoes_dados()
                                if opcao_dados == 1:
                                    self.__controlador_usuario.altera_dados()
                                elif opcao_dados == 2:
                                    self.__controlador_usuario.exclui_conta()
                                    break
                                elif opcao_dados == 0:
                                    break
                        elif opcao_pos_login == 2:
                            self.__controlador_usuario.abre_menu_documento()
                        elif opcao_pos_login == 0:
                            break
                else:
                    self.__tela_sistema.nao_e_possivel_logar()
            elif funcao_escolhida == 0:
                break
