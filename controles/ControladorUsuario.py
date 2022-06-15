from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from telas.TelaDocumento import TelaDocumento
from entidades.Cpf import Cpf

class ControladorUsuario:
    def __init__(self):
        self.usuarios = []
        self.__telausuario = TelaUsuario()
        self.__teladocumento = TelaDocumento()

    #REMOVER 'cadastro_documento' DO CONTROLADOR DE USUÁRIO...
    def cadastro_documento(self):
        dados_cpf = self.__teladocumento.cadastrar_cpf()
        cpfx = Cpf(dados_cpf['cpf'], dados_cpf['nome'])
        print(cpfx)
    #########################################################

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

    def login_usuario(self):
        usuario_login = self.__telausuario.login_usuario_dados()
        usuario_senha = self.__telausuario.login_usuario_senha()

        if self.usuarios:
            for usuario_lista in self.usuarios:
                if usuario_lista.cpf == usuario_login and usuario_lista.senha == usuario_senha:
                    print('Foi logado com sucesso!!!')
                    self.cadastro_documento()

                return True
            else:
                print('Usuário ou senha incorreto\nDigite novamente!!')
                return False


