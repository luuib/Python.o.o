#Objeto e uma unica coleção de dados(Atributos) e comportamentos (metodos)
class contaBancaria:
    #Atriutos são variaveis internas dentro do objeto
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    #Metodos são funções do objeto que produzem algum comportamento 
    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Numero da conta:", self.numero)
        print("Titular", self.titular)
        print("Saldo:", self.saldo)


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("O seu saldo inuficiente")

def exibir_menu():
    print("\nMENU;")
    print("1 - Exibir detalhes da conta:")
    print("2 - Realizar saque")
    print("3 - Realizar deposito")
    print("0 - Sair do Progrma")    


#aqui crio uma instancia do objeto contaBancaris
#como nome conta_do_Usuario

numero_conta = input("Digite o numero da conta")
titular_conta = input("Digite o titular da conta")
saldo_inicial = float(input("Digite o saldo inicial da conta:"))

conta_do_Usuario = contaBancaria(numero_conta, titular_conta , saldo_inicial)

opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o numero da opcao desejado:"))

    if opcao == 1:
        conta_do_Usuario.exibir_detalhes()

    elif opcao == 2:
        valor_depositar = float(input("digite o valor que sera depositado").replace(",","."))
        conta_do_Usuario.depositar(valor_depositar)

    elif opcao == 3:
        valor_saque = float(input("digite o valor que sera sacado").replace(",","."))
        conta_do_Usuario.sacar(valor_saque)


