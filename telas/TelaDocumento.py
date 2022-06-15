class TelaDocumento:


    def cadastrar_cpf(self):
        print("------ CADASTRO DE CPF ------")
        cpf = input("Envie seu arquivo CPF")
        nome = 'CPF'
        return {'cpf': cpf, 'nome': nome}

    def cadastrar_rg(self):
        print("------ CADASTRO DE RG ------")
        rg = input("Envie o seu arquivo de Identidade")
        return rg

    def cadastrar_titulo_eleitor(self):
        print("------ CADASTRO DE RG ------")
        titulo_eleitor = input("Envie o seu arquivo de título de eleitor")
        return titulo_eleitor