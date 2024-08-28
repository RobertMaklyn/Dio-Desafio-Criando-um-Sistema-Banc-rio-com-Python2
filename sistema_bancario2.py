import textwrap

def exibir_menu():
    menu = """\n
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair
    => """
    return input(textwrap.dedent(menu))


def realizar_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso! ")
    else:
        print("\n Operação falhou! Valor inválido! ")
    return saldo, extrato


def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n Saldo insuficiente! ")
    elif valor > limite:
        print("\n Limite de saque excedido! ")
    elif numero_saques >= limite_saques:
        print("\nNúmero máximo de saques atingido! ")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso! ")
    else:
        print("\n Valor inválido para saque! ")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = localizar_usuario(cpf, usuarios)
    if usuario_existente:
        print("\n Usuário com esse CPF já cadastrado! ")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário cadastrado com sucesso! ===")


def localizar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta_bancaria(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = localizar_usuario(cpf, usuarios)
    if usuario:
        print("\nConta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado. Criação de conta encerrada! ")


def listar_todas_contas(contas):
    for conta in contas:
        detalhes_conta = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(detalhes_conta))


def executar_banco():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()
        if opcao == "1":
            valor = float(input("Informe o valor para depósito: "))
            saldo, extrato = realizar_deposito(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor para saque: "))
            saldo, extrato = realizar_saque(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "6":
            cadastrar_usuario(usuarios)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta_bancaria(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_todas_contas(contas)
        elif opcao == "7":
            break
        else:
            print("Operação inválida. Tente novamente.")

executar_banco()
