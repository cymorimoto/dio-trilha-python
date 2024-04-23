class sistema_bancario:

    def __init__(self, transacao, saldo=0):
        self.transacao = transacao
        self.saldo = saldo
        self.LIMITE = 500
        self.LIMITE_SAQUES = 3
        self.numero_saques = 0


    def saldo(self):
        print("Saldo: ", self.saldo)
    
    def historico_transacao(self, operacao, valor=0):
        self.transacao.append((operacao, valor,))
    
    def transacao(self, operacao, valor=0):
        if operacao == "Saque":
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
        elif operacao == "Depósito":
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            self.historico_transacao(operacao, valor)
        elif operacao == "Extrato":
            if(len(self.transacao)>0):
                print("Extrato: ")
                print(f"\n".join(f"{op}: R$ {val:.2f}" for op, val in self.transacao))    
            else:
                print("Nenhuma movimentação realizada.") 
        else:
            print("Operação Invalida")   






SB = sistema_bancario([],0)

operacao = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

:
"""

while True:

    menu = input(operacao)

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
    elif menu == "q":
        break
    else:
        print("Erro!")
