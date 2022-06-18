

class TelaSistema:
    def mostra_opcoes(self):
        print("---------MENU-----------"
              "\nEscolha a opcao"
              "\n1 - Cadastrar Usuario"
              "\n2 - Logar como Usuario"
              "\n0 - Finalizar")
        opcoes_menu_cadastro_ou_login = int(input("Escolha uma opcao: "))
        return opcoes_menu_cadastro_ou_login

    def mostrar_opcoes_apos_login(self):
        print('------ BEM VINDO ------'
              '\n1 - Alterar ou listar Dados'
              '\n2 - validar documentos'
              '\n0 - Fechar o programa')
        opcoes_menu_dados_ou_documentos = int(input('Digite sua opção: '))
        return opcoes_menu_dados_ou_documentos

    def mostrar_opcoes_dados(self):
        print('------ DADOS ------'
              '\n1 - Listar usuarios cadastrados'
              '\n2 - Alterar dados'
              '\n2 - Alterar dados'
              '\n3 - Excluir conta'
              '\n0 - Retornar')
        opcoes_menu_dados = int(input('digite sua opção'))
        return opcoes_menu_dados
