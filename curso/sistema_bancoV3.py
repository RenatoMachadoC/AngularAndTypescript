from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco, contas=None):
        self.endereco = endereco
        self.contas = contas if contas is not None else []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def realizar_transacao(self, transacao, conta):
        transacao.registro(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco=None, contas=None):
        super().__init__(endereco, contas)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property        
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico  
    
    def sacar(self, valor):
        if valor > self._saldo:
            print("Valor inserido é inválido para saque, saldo insuficiente.")
            return False
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Saldo atual: R$ {self._saldo:.2f}")
            return True
        else:
            print("Valor inserido é inválido para saque.")
            return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Saldo atual: R$ {self._saldo:.2f}")
            return True
        else:
            print("Valor inválido para depósito.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saques = len([t for t in self.historico.transacoes if t["tipo"] == "Saque"])
        
        if valor > self.limite:
            print("Valor excede o limite de saque.")
            return False
        elif numero_saques >= self.limite_saque:
            print("Limite de saques atingido.")
            return False
        else:
            return super().sacar(valor)
    
    def __str__(self):
        return f"Conta Corrente - Número: {self.numero}, Agência: {self.agencia}, Cliente: {self._cliente.nome}, Saldo: R$ {self.saldo:.2f}"

class Historico:
    def __init__(self):
        self.transacoes = []
        
    def registrar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registro(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registro(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.registrar_transacao(self)
            print("Saque registrado com sucesso!")
        else:
            print("Saque não realizado.")

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registro(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.registrar_transacao(self)
            print("Depósito registrado com sucesso!")
        else:
            print("Depósito não realizado.")
            
#menu do sistema

def menu():
    menu = """
    
    ===========Menu============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuário
    [q]\t Sair
    ==========================
    
    """
    return input(textwrap.dedent((menu)))

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if hasattr(c, "cpf") and c.cpf == cpf), None)
    if not cliente:
        print("Cliente não encontrado.")
        return
    if not cliente.contas:
        print("Cliente não possui contas.")
        return
    for i, conta in enumerate(cliente.contas):
        print(f"{i}: {conta}")
    idx = int(input("Escolha o número da conta para depósito: "))
    if idx < 0 or idx >= len(cliente.contas):
        print("Conta inválida.")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    cliente.realizar_transacao(transacao, cliente.contas[idx])

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if hasattr(c, "cpf") and c.cpf == cpf), None)
    if not cliente:
        print("Cliente não encontrado.")
        return
    if not cliente.contas:
        print("Cliente não possui contas.")
        return
    for i, conta in enumerate(cliente.contas):
        print(f"{i}: {conta}")
    idx = int(input("Escolha o número da conta para saque: "))
    if idx < 0 or idx >= len(cliente.contas):
        print("Conta inválida.")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    cliente.realizar_transacao(transacao, cliente.contas[idx])

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            depositar(clientes)
        
        elif opcao == "s":
            sacar(clientes)
        
        elif opcao == "e":
            exibir_extrato(clientes)
        
        elif opcao == "nu":
            criar_usuario(clientes)
        
        elif opcao == "nc":
            criar_conta(clientes, contas)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            print("Sistema encerrado.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if hasattr(c, "cpf") and c.cpf == cpf), None)
    if not cliente:
        print("Cliente não encontrado.")
        return
    if not cliente.contas:
        print("Cliente não possui contas.")
        return
    for i, conta in enumerate(cliente.contas):
        print(f"\nExtrato da Conta {i}:")
        if not conta.historico.transacoes:
            print("Nenhuma transação realizada.")
        else:
            for transacao in conta.historico.transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

def criar_conta(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if hasattr(c, "cpf") and c.cpf == cpf), None)
    if not cliente:
        print("Cliente não encontrado.")
        return
    numero = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente, numero)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {conta.numero}")

def criar_usuario(clientes):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço: ")
    if any(c for c in clientes if hasattr(c, "cpf") and c.cpf == cpf):
        print("Usuário já cadastrado.")
        return
    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso!")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(conta)