

class TelaSistema:
    def mostra_opcoes(self):
        print("---------MENU-----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Usuario")
        print("2 - Logar como Usuario")
        print("0 - finalizar")
        opcoes_menu_cadastro_ou_login = int(input("escolha uma opcao:"))
        return opcoes_menu_cadastro_ou_login

    def mostrar_opcoes_apos_login(self):
        print('------ BEM VINDO ------')

        print('1 - Alterar ou listar Dados')
        print('2 - validar documentos')
        print('0 - retornar')
        opcoes_menu_dados_ou_documentos = int(input('digite sua opção'))
        return opcoes_menu_dados_ou_documentos

    def mostrar_opcoes_dados(self):
        print('------ DADOS ------')

        print('1 - listar usuarios cadastrados')
        print('2 - alterar dados')
        print('3 - excluir conta')
        print('0 - retornar')
        opcoes_menu_dados = int(input('digite sua opção'))
        return opcoes_menu_dados
