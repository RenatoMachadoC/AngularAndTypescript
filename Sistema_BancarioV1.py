#refazer o sistema bancario
# Sistema Bancário Simples

# Menu do sistema!

menu = """

[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair

"""

#fim do menu

# Sistema do valor em conta do cliente

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

# fim do sistema do valor em conta do cliente.

# Função de loop do sistema bancário

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Por favor, digite o valor a ser depositado: ")) 
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n" # Adiciona o depósito ao extrato
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido! O valor deve ser maior que zero.")
    
    elif opcao == "s":
        
        valor = float(input("Qual o valor a ser sacado? "))
        if valor > saldo:
            print("Valor inválido! O valor deve ser menor que o saldo.")
            
        elif valor > limite:
            print("Valor inválido! O valor deve ser menor que o limite.")
            
        elif numero_saques >= limite_saques:
            print("Número de saques excedido! O número máximo de saques é 3.")
    
    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Limite: R$ {limite:.2f}")
        print(f"Número de saques realizados: {numero_saques}")
    
    elif opcao == "q":
        print("Finalizando o sistema bancário... tenha um bom dia!")
        break # Encerra o loop e o programa

#fim do sistema bancário.

