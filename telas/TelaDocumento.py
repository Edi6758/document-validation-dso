class TelaDocumento:
    def cadastrar_documento(self):
        print("------CADASTRO DE DOCUMENTO------")

        cpf = input("envie seu arquivo CPF")
        rg = input("envie seu arquivo de Identidade")
        titulo_eleitor = input("envie seu arquivo de título de eleitor")


        return {'cpf':cpf, 'rg':rg, 'titulo':titulo}