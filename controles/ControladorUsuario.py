from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario


class ControladorUsuario:
    def __init__(self):
        self.usuarios = []
        self.__telausuario = TelaUsuario()

    def cadastro_usuario(self):
        dados_usuario = self.__telausuario.cadastro_usuario_dados()
        usuario = Usuario(dados_usuario['nome'], dados_usuario['email'], dados_usuario['senha'],
                          dados_usuario['telefone'], dados_usuario['rg'],
                          dados_usuario['cpf'], dados_usuario['titulo'])
        print(self.usuarios)

        if self.usuarios == None:
            self.usuarios.append(usuario)
            print('primeiro if')
        else:
            for usuario in self.usuarios:
                if usuario not in self.usuarios:
                    self.usuarios.append(usuario)
                    print('segundo if')
                else:
                    print('usuario já cadastrado')
        print(self.usuarios)
