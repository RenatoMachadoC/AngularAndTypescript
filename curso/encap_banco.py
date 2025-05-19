class Conta:
    def __init__(self, agencia, titular):
        self.__saldo = 0
        self.__limite = 0
        self.agencia = 246
        self.__numero = 123456
        self.__senha = 1234
        self.titular = "Lucas"
        self.__cpf = "123.456.789-00"
        
    def depositar(self, valor):
        if valor > 0: #para evitar valores negativos
            self.__saldo += valor
            print(f"Foi reailzado um deposito de R$ {valor:.2f}")
            print(f"Seu saldo atual é de R$ {self.__saldo:.2f}")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo: #para evitar saques em valores negativos e maiores que o saldo
            self.__saldo -= valor
            print(f"Foi realizado um saque de R$ {valor:.2f}")
            print(f"Seu saldo atual é de R$ {self.__saldo:.2f}")
            
    def consultar_saldo(self):
        return self.__saldo
            

conta = Conta(246, "Lucas")
conta.depositar(1000)
print(conta._Conta__saldo) #acessando o atributo __saldo diretamente
conta.consultar_saldo()
conta.sacar(500)