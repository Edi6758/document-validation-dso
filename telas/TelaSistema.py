class TelaSistema:
    def mostra_opcoes(self):
        print("---------MENU-----------"
              "\nEscolha a opcao"
              "\n1 - Cadastrar Usuario"
              "\n2 - Logar como Usuario"
              "\n0 - Finalizar")
        try:
            opcoes_menu_cadastro_ou_login = int(input("Escolha uma opcao: "))
        except ValueError:
            print('somente numeros inteiros por favor')
        else:
            return opcoes_menu_cadastro_ou_login

    def mostrar_opcoes_apos_login(self):
        print('------ BEM VINDO ------'
              '\n1 - Alterar ou listar Dados'
              '\n2 - validar documentos'
              '\n0 - Fechar o programa')
        try:
            opcoes_menu_dados_ou_documentos = int(input('Digite sua opção: '))
        except ValueError:
            print('somente numeros inteiros por favor')
        else:
            return opcoes_menu_dados_ou_documentos

    def mostrar_opcoes_dados(self):
        print('------ DADOS ------'
              '\n1 - Listar usuarios cadastrados'
              '\n2 - Alterar dados'
              '\n3 - Excluir conta'
              '\n0 - Retornar')
        try:
            opcoes_menu_dados = int(input('digite sua opção'))
        except ValueError:
            print('somente numeros inteiros por favor')
        else:
            return opcoes_menu_dados

    def mostra_opcoes_para_alterar(self):
        print('------ ALTERAR ------'
              '\n1 - alterar nome '
              '\n2 - alterar email'
              '\n3 - alterar senha'
              '\n4 - alterar telefone'
              '\n5 - alterar rg'
              '\n6 - alterar cpf'
              '\n7 - alterar titulo de eleitor')
        try:
            opcao_escolhida = int(input('qual a opção?'))
        except ValueError:
            print('somente numeros inteiros por favor')
        else:
            return opcao_escolhida

    def nao_e_possivel_logar(self):
        print('não foi possivel logar, tente novamente')
