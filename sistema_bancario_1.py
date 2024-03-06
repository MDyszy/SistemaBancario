menu = """
    [1]Depósito
    [2]Saque
    [3]Extrato
    [0]Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("\n===Depósito===")
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito --- R$ {valor_deposito:.2f}\n"

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            print("\n===Saque===")
            valor_saque = float(input("Informe o valor do saque: "))

            if valor_saque > limite:
                print("Operação inválida! Não é possível fazer um saque acima de R$500,00.")

            elif valor_saque < 0:
                print("Operação inválida! Não é possível sacar valores negativos.")

            elif valor_saque > saldo:
                print("Operação inválida! O saldo é menor do que o valor de saque informado.")

            else:
                saldo -= valor_saque
                extrato += f"Saque --- R$ {valor_saque:.2f}\n"
                numero_saques += 1

        else:
            print("\nNão é possível realizar mais de 3 saques por dia!")

    elif opcao == "3":
        verificador = len(extrato)

        if verificador > 0:
            print("\n=============Extrato=============")
            print(f"{extrato}")
            print(f"Saldo Atual --- R$ {saldo:.2f}")
            print("=================================")
        
        else:
            print("Não foi realizada nenhuma movimentação bancária em sua conta.")
        
    elif opcao == "0":
        break;

    else:
        print("\n Operação inválida! Insira novamente a operação desejada.")