from telas.TelaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def inicia_sistema(self):
        self.__tela_sistema.mostra_opcoes()

    def cadastra_usuario(self):
        pass

    def login_admin(self):
        pass

    def encerra(self):
        exit(0)


