class TelaDocumento:

    def menu_documentos(self):
        print('------ o que deseja fazer? ------'
              '\n1 - enviar Arquivo de CPF: '
              '\n2 - enviar Arquivo de RG: '
              '\n3 - enviar Arquivo de título de eleitor: ')
        try:
            opcoes_documento_selecionado = int(input('Digite sua opção: '))
        except ValueError:
            print('somente numeros inteiros por favor')
        else:
            return opcoes_documento_selecionado

    def cadastrar_cpf(self):
        print("------ CADASTRO DE CPF ------")
        cpf = input("Envie seu arquivo CPF")
        nome = 'CPF'
        return {'cpf': cpf, 'nome': nome}

    def cadastrar_rg(self):
        print("------ CADASTRO DE RG ------")
        rg = input("Envie o seu arquivo de Identidade")
        nome = "RG"
        return {'rg': rg, 'nome': nome}

    def cadastrar_titulo_eleitor(self):
        print("------ CADASTRO DE TÍTULO DE ELITOR ------")
        titulo_eleitor = input("Envie o seu arquivo de título de eleitor")
        nome = "TÍTULO DE ELITOR"
        return {'titulo_eleitor': titulo_eleitor, 'nome': nome}
