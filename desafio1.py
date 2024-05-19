menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso")

        else:
            print("Operação inválida! O valor informado não pode ser depositado. Tente novamente informando um valor válido")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente para realizar o saque informado. Consulte seu extrato e tente novamente")

        elif excedeu_limite:
            print("Operação falhou! O valor informado para saque excede o seu limite.")

        elif excedeu_saque:
            print("Operação falhou! O seu número máximo de saque diário foi excedido. Tente novamente amanhã!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque +=1
            print(f"Saque de R$ {valor:.2f} foi realizado com sucesso")

        else:
            print("Operação inválida! O valor informado não é possível de ser sacado")
        
    elif opcao == "e":
        print("\n================ EXTRATO DE TRANZAÇÕES ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")