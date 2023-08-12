menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if  opcao == "d":
        valor = float(input("Valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\n Depósito: R$ {valor:.2f}"

        else:
            print("A operação falhou! Valor não informado.")

    elif  opcao == "s":
        valor = float(input("Valor do saque: "))

        if valor > 0:

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("A operação falhou! Você não possui saldo suficiente.")

            elif excedeu_limite:
                print("A operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("A operação falhou! Número máximo de saques excedido.")

            saldo -= valor
            extrato += f"\n Saque: R$ {valor:.2f}"
            numero_saques += 1
        
        else:
            print("A operação falhou! Valor não informado.")

    elif opcao == "e":
        print("\n ================= EXTRATO ================= \n")
        print(" Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R# {saldo:.2f}\n")
        print("=============================================")

    elif  opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida")