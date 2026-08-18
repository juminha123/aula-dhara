saldo = 1000
while True:
    print("1 - Consultar saldo")
    print("2- sacar")
    print("3 - depositar")
    print("4 - sair")

    opcao = input("escolha:")
    if opcao == "1":
        print("seu saldo é de: ", saldo)
    elif opcao == "2":
        valor = float(input("valor do saque: "))
        if valor <= saldo:
            saldo -= valor
            print("saldo retirado", saldo)
        else:
            print("saldo insuficiente")
    elif opcao == "3":
        valor = float(input("valor do depósito"))
        saldo += valor
        print("o deposito foi realizado, salto atual é: ", saldo)
    elif opcao == "4":
        print("encerrando o sistema....")
        break
    else:
        print("opção inexistente, escolha outra")
