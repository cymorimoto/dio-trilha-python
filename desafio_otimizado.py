import textwrap

class sistema_bancario:

    def __init__(self, historico, usuarios,contas, saldo=0):
        self.historico = historico
        self.saldo = saldo
        self.LIMITE = 500
        self.LIMITE_SAQUES = 3
        self.numero_saques = 0
        self.usuarios = usuarios
        self.AGENCIA='0001'
        self.contas = contas

   
    def historico_transacao(self, operacao, valor=0):
        self.historico.append((operacao, valor,))
    
    def transacao(self, operacao, valor=0):
        if operacao == "Saque": 
           self.saque(operacao=operacao, valor=valor) # keywords onlly
        elif operacao == "Depósito": 
            self.deposito(operacao, valor) #position only
        elif operacao == "Extrato":
            self.extrato(self.saldo,hist=self.historico)  # keyword and position
        elif operacao == "Novo Usuário":
            self.cadastrar_cliente()
        elif operacao == "Nova Conta":
            self.cadastrar_conta()
        elif operacao == "Listar Contas":
            self.listar_contas()
        else:
            print("Operação Invalida")   

    def saque(self,*, operacao, valor):
        if valor > self.LIMITE:
                print ("Limite de saque excedido!")
        else:
            if self.numero_saques <= self.LIMITE_SAQUES:
                self.saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                self.historico_transacao(operacao, valor)
                self.numero_saques +=1
            else:
                print("Número máximo de saques excedido!")

    def deposito(self, operacao, valor ,/):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        self.historico_transacao(operacao, valor)

    def extrato(self, saldo,/,*, hist):
        if(len(hist)>0):
                print("Extrato: \n")
                print("Saldo: ", saldo)
                print(f"\n".join(f"{op}: R$ {val:.2f}" for op, val in hist))    
        else:
            print("Nenhuma movimentação realizada.") 

    def cadastrar_cliente(self):
        cpf = input("Informe o CPF (somente número): ")
        usuario = False
        if len(self.usuarios)>0:
            usuario = self.filtrar_usuario(cpf, self.usuarios)
                    
        if usuario:
            print("\n Já existe cliente com esse CPF!")
            return
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print(" Usuário criado com sucesso!")

    def filtrar_usuario(self, cpf, usuarios):           
                usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
                return usuarios_filtrados[0] if usuarios_filtrados else None

    def cadastrar_conta(self):
        
        cpf = input("Informe o CPF do usuário: ")
        usuario = False
        if len(self.usuarios)>0:
            usuario = self.filtrar_usuario(cpf, self.usuarios)
        if usuario:
            print("\n Conta criada com sucesso!")
            num_conta = len(self.contas) + 1
            self.contas.append({"agencia": self.AGENCIA, "numero_conta":  num_conta, "usuario": usuario})
            print(f"\n Agência:{self.AGENCIA}, Conta: {num_conta}")
        else:    
            print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")

    def listar_contas(self):
         for conta in self.contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

    def menu(self):
        operacao = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [c] Nova conta
        [l] Listar contas
        [u] Novo usuário
        [q] Sair

        :
        """
        return input(textwrap.dedent(operacao))


SB = sistema_bancario([],[],[],0)

while True:

    menu = SB.menu()

    if menu == "d":
        valor = float(input("Informe o valor do depósito: \n"))
        if valor > 0:
            SB.transacao("Depósito", valor)
        else: 
            print("Valor informado inválido!")    
    elif menu == "s":
        valor = float(input("Informe o valor do saque: \n"))
        if valor > 0:
            SB.transacao("Saque", valor)        
        else: 
            print("Valor informado inválido!")  
    elif menu == "e":
              SB.transacao("Extrato")   
    elif menu == "u":
              SB.transacao("Novo Usuário")   
    elif menu == "c":
              SB.transacao("Nova Conta")        
    elif menu == "l":
              SB.transacao("Listar Contas")        
  
    elif menu == "q":
        break
    else:
        print("Erro!")
