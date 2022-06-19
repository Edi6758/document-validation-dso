from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from telas.TelaDocumento import TelaDocumento


class ControladorUsuario:
    def __init__(self):
        self.usuarios = []
        self.__telausuario = TelaUsuario()
        self.__teladocumento = TelaDocumento()

    def cadastro_usuario(self):
        dados_usuario = self.__telausuario.cadastro_usuario_dados()
        usuario = Usuario(dados_usuario['nome'], dados_usuario['email'], dados_usuario['senha'],
                          dados_usuario['telefone'], dados_usuario['rg'],
                          dados_usuario['cpf'], dados_usuario['titulo'])
        if self.usuarios:
            for usuario_lista in self.usuarios:
                if usuario_lista.cpf == usuario.cpf:
                    print('cpf ja cadastrado')
                    break
            else:
                self.usuarios.append(usuario)
        else:
            self.usuarios.append(usuario)

        print(self.usuarios)

    def funcao_usuarios_cadastrados_cpf(self):
        lista_usuarios_cadastrados_cpf = []
        for usuario in self.usuarios:
            lista_usuarios_cadastrados_cpf.append(usuario.cpf)

        return lista_usuarios_cadastrados_cpf

    def login_usuario(self):
        usuario_login = self.__telausuario.login_usuario_dados()
        usuario_senha = self.__telausuario.login_usuario_senha()

        if self.usuarios:
            for usuario_lista in self.usuarios:
                if usuario_lista.cpf == usuario_login and usuario_lista.senha == usuario_senha:
                    print('Foi logado com sucesso!!!') #mudar para a tela
                    return True
            else:
                print('Usuário ou senha incorreto\nDigite novamente!!')
                return False


