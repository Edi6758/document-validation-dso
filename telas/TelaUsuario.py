

class TelaUsuario:
    def cadastro_usuario_dados(self):
        print("------CADASTRO------")

        nome = input('nome:')
        email = input('email:')
        senha = input('senha:')
        telefone = input('telefone:')
        rg = input('rg:')
        cpf = input('cpf:')
        titulo = input('titulo:')

        return {'nome': nome, 'email': email, 'senha': senha, 'telefone': telefone, 'rg': rg, 'cpf': cpf,
                'titulo': titulo}


    def login_usuario_dados(self):
        print("------LOGIN------")

        cpf_login = input('qual o cpf?')
        return cpf_login

    def login_usuario_senha(self):
        print("------SENHA ------")

        senha_login = input('qual a senha?')
        return senha_login