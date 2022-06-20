

class TelaUsuario:

    def cadastro_usuario_dados(self):
        print("------ CADASTRO DE PESSOAS ------")

        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite uma senha forte:')
        telefone = input('Digite seu telefone:')
        rg = input('Digite seu rg:')
        cpf = input('Digite seu cpf:')
        titulo = input('Digite seu título de eleitor:')

        return {'nome': nome, 'email': email, 'senha': senha, 'telefone': telefone, 'rg': rg, 'cpf': cpf,
                'titulo': titulo}


    def login_usuario_dados(self):
        print("------ LOGIN ------")

        cpf_login = input('Qual é o seu cpf?')
        return cpf_login

    def login_usuario_senha(self):
        print("------ SENHA ------")

        senha_login = input('Qual é a senha?')
        return senha_login

    def login_sucesso(self):
        print('foi logado com sucesso')

    def login_incorreto(self):
        print('usuario ou senha incorretos')

    def cpf_duplicado(self):
        print('cpf já cadastrado')

    def conta_excluida_sucesso(self):
        print('conta excluida com sucesso')

    def alteracao_dados(self):
        novo_dado = input('digite o novo dado')
        return novo_dado

    def mostrar_cpfs(self):
        pass

    def cpf_validado(self):
        print("\n======== PARABÉNS!! CPF VALIDADO COM SUCESSO ========\n")

    def cpf_nao_validado(self):
        print("\n======== INFORMAÇÕES DIVERGENTES ======== "
              "\n======== porfavor revise seus dados ========")

    def mostrar_rgs(self):
        pass

    def rg_validado(self):
        print("\n======== PARABÉNS!! RG VALIDADO COM SUCESSO ========\n")

    def rg_nao_validado(self):
        print("\n======== INFORMAÇÕES DIVERGENTES ======== "
              "\n======== porfavor revise seus dados ========")

    def mostrar_titulos(self):
        pass

    def titulo_validado(self):
        print("\n======== PARABÉNS!! RG VALIDADO COM SUCESSO ========\n")

    def titulo_nao_validado(self):
        print("\n======== INFORMAÇÕES DIVERGENTES ======== "
              "\n======== porfavor revise seus dados ========")
