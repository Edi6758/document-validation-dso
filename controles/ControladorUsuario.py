from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from telas.TelaDocumento import TelaDocumento


class ControladorUsuario:
    def __init__(self):
        self.usuarios = []
        self.__telausuario = TelaUsuario()
        self.__teladocumento = TelaDocumento()
        self.__telasistema = TelaSistema()
        self.usuario_atual = None


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


    def lista_usuarios_cadastrados(self):
        lista_usuarios_cadastrados = []
        for usuario in self.usuarios:
            lista_usuarios_cadastrados.append(usuario.nome)

        print(lista_usuarios_cadastrados)

    def exclui_conta(self):
        print('confirme seu login')
        usuario_login = self.__telausuario.login_usuario_dados()
        usuario_senha = self.__telausuario.login_usuario_senha()
        for usuario in self.usuarios:
            if usuario.cpf == self.usuario_atual.cpf and usuario.senha == self.usuario_atual.senha:
                self.usuarios.remove(usuario)

    def altera_dados(self):
        opcao = self.__telasistema.mostra_opcoes_para_alterar()
        for usuario in self.usuarios:
            if usuario.cpf == self.usuario_atual.cpf and usuario.senha == self.usuario_atual.senha:
                if opcao == 1:
                    usuario.nome = input('digite o novo dado')
                elif opcao == 2:
                    usuario.email = input('digite o novo dado')
                elif opcao == 3:
                    usuario.senha = input('digite o novo dado')
                elif opcao == 4:
                    usuario.telefone = input('digite o novo dado')
                elif opcao == 5:
                    usuario.rg = input('digite o novo dado')
                elif opcao == 6:
                    usuario.cpf = input('digite o novo dado')
                elif opcao == 7:
                    usuario.titulo = input('digite o novo dado')
