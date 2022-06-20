from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from telas.TelaDocumento import TelaDocumento
from telas.TelaSistema import TelaSistema


from entidades.Identidade import Identidade
from entidades.Cpf import Cpf
from entidades.TituloEleitor import TituloEleitor
import pytesseract
import cv2
import re

class ControladorUsuario:
    def __init__(self):
        self.__rgs = []
        self.__cpfs = []
        self.__titulos = []
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
                    self.__telausuario.cpf_duplicado()
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
                    self.usuario_atual = usuario_lista
                    self.__telausuario.login_sucesso()
                    return True
            else:
                self.__telausuario.login_incorreto()
                return False

    #VERIFICAR COMO ESTÁ O CADASTRO DE CPF
    def cadastro_cpf(self):
        dados_cpf = self.__teladocumento.cadastrar_cpf()
        cpfx = Cpf(dados_cpf['cpf'], dados_cpf['nome'])
        self.__cpfs.append(cpfx)
        print(self.__cpfs)
        self.validar_cpf()
        return self.__telasistema.mostrar_opcoes_apos_login()

    def validar_cpf(self):
        cpf_cadatrados = []
        for cpf in self.__cpfs:
            cpf_cadatrados.append(cpf.cpf)
        print(cpf_cadatrados[0])
        imagem = cv2.imread(cpf_cadatrados[0])
        caminho = r"C:\Program Files\Tesseract-OCR"

        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(imagem)

        filtroCpf = re.compile(r'\d{3}\.\d{3}\.\d{3}\-\d{2}')
        tratativaCpf = filtroCpf.findall(texto)
        valorCpf = "".join(tratativaCpf).replace('.', '').replace('-', '')

        lista_cpf_cadastrados = []
        for usuario in self.usuarios:
            lista_cpf_cadastrados.append(usuario.cpf)

        print("O CPF registrado é: ", lista_cpf_cadastrados[0])
        print("O CPF do documento é", valorCpf)

        if(valorCpf == lista_cpf_cadastrados[0]):
            self.__telausuario.cpf_validado()
        else:
            self.__telausuario.cpf_nao_validado()
            self.__telasistema.mostrar_opcoes_apos_login()

    #VERIFICAR COMO ESTÁ O CADASTRO DE RG
    def cadastro_rg(self):
        dados_rg = self.__teladocumento.cadastrar_rg()
        rgx = Identidade(dados_rg['rg'], dados_rg['nome'])
        self.__rgs.append(rgx)
        print(self.__rgs)
        self.validar_rg()
        return self.__telasistema.mostrar_opcoes_apos_login()

    def validar_rg(self):
        rg_cadatrados = []
        for rg in self.__rgs:
            rg_cadatrados.append(rg.rg)
        print(rg_cadatrados[0])
        imagem = cv2.imread(rg_cadatrados[0])
        caminho = r"C:\Program Files\Tesseract-OCR"

        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(imagem)

        filtroRg = re.compile(r'\d{7}')
        tratativaRg = filtroRg.findall(texto)
        valorRg = "".join(tratativaRg).replace(' ', '')

        lista_rg_cadastrados = []
        for usuario in self.usuarios:
            lista_rg_cadastrados.append(usuario.rg)

        print("\nO RG registrado é",lista_rg_cadastrados[0])
        print("O RG do documento é", valorRg)

        if(valorRg == lista_rg_cadastrados[0]):
            self.__telausuario.rg_validado()
        else:
            self.__telausuario.rg_nao_validado()
            self.__telasistema.mostrar_opcoes_apos_login()

    # VERIFICAR COMO ESTÁ O CADASTRO DE TÍTULO DE ELEITOR

    def cadastro_titulos(self):
        dados_titulo = self.__teladocumento.cadastrar_titulo_eleitor()
        titulox = Identidade(dados_titulo['titulo_eleitor'], dados_titulo['nome'])
        self.__titulos.append(titulox)
        print(self.__titulos)
        self.validar_titulo()
        return self.__telasistema.mostrar_opcoes_apos_login()

    def validar_titulo(self):
        titulo_cadatrados = []
        for titulo in self.__titulos:
            titulo_cadatrados.append(titulo.rg)
        print(titulo_cadatrados[0])
        imagem = cv2.imread(titulo_cadatrados[0])
        caminho = r"C:\Program Files\Tesseract-OCR"

        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(imagem)

        filtroTitulo = re.compile(r'\d{4}\ \d{4}\ \d{4}')
        tratativaTitulo = filtroTitulo.findall(texto)
        valorTitulo = "".join(tratativaTitulo).replace(' ','')

        lista_titulo_cadastrados = []
        for usuario in self.usuarios:
            lista_titulo_cadastrados.append(usuario.titulo)

        print("\nO TÍTULO DE ELEITOR registrado é",lista_titulo_cadastrados[0])
        print("O TÍTULO DE ELEITOR do documento é", valorTitulo)

        if(valorTitulo == lista_titulo_cadastrados[0]):
            self.__telausuario.titulo_validado()
        else:
            self.__telausuario.titulo_nao_validado()
            self.__telasistema.mostrar_opcoes_apos_login()

    # fim de validar docs

    def abre_menu_documento(self):
        opcoes_documento = self.__teladocumento.menu_documentos()
        if(opcoes_documento == 1):
            self.cadastro_cpf()
        elif(opcoes_documento == 2):
            self.cadastro_rg()
        elif(opcoes_documento == 3):
            self.cadastro_titulos()

    def lista_usuarios_cadastrados(self):
        lista_usuarios_cadastrados = []
        for usuario in self.usuarios:
            lista_usuarios_cadastrados.append(usuario.nome)

        print(lista_usuarios_cadastrados)

    def exclui_conta(self):
        for usuario in self.usuarios:
            if usuario.cpf == self.usuario_atual.cpf and usuario.senha == self.usuario_atual.senha:
                self.usuarios.remove(usuario)
                self.__telausuario.conta_excluida_sucesso()

    def altera_dados(self):
        opcao = self.__telasistema.mostra_opcoes_para_alterar()
        for usuario in self.usuarios:
            if usuario.cpf == self.usuario_atual.cpf and usuario.senha == self.usuario_atual.senha:
                if opcao == 1:
                    usuario.nome = self.__telausuario.alteracao_dados()
                elif opcao == 2:
                    usuario.email = self.__telausuario.alteracao_dados()
                elif opcao == 3:
                    usuario.senha = self.__telausuario.alteracao_dados()
                elif opcao == 4:
                    usuario.telefone = self.__telausuario.alteracao_dados()
                elif opcao == 5:
                    usuario.rg = self.__telausuario.alteracao_dados()
                elif opcao == 6:
                    usuario.cpf = self.__telausuario.alteracao_dados()
                elif opcao == 7:
                    usuario.titulo = self.__telausuario.alteracao_dados()
