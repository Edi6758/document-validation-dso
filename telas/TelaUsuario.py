

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