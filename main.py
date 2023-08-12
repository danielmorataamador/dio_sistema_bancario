
import textwrap

def menu():
    menu = """\n
    ============== MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return  input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n Depósito: +R$ {valor:.2f}"
    else:
        print("A operação falhou! Valor não informado.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("A operação falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("A operação falhou! Número máximo de saques excedido.")

        saldo -= valor
        extrato += f"\n Saque: -R$ {valor:.2f}"
        numero_saques += 1


        return saldo, extrato
    
    else:
        print("A operação falhou! Valor não informado.")


def exibir_extrato(saldo, /, *, extrato):
    print("\n ================= EXTRATO ================= \n")
    print(" Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo Atual: R# {saldo:.2f}\n")
    print("=============================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("O CPF informado já esta cadastrado!")
        return
    
    nome = input("informe o nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço ( logradouro, nr - bairro - cidade e uf)")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        lista = f"""\
            AG: \t{conta['agencia']}
            C\C: \t{conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(lista))

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0]if usuarios_filtrados else None

def main():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()

        if  opcao == "d":
            valor = float(input("Valor para depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif  opcao == "s":
            valor = float(input("Valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione uma opção válida")

main()