from Cliente import Cliente


nome = input("digite o nome:")
email = input("digite o nome:")
telefone = input("digite o nome:")

cliente = Cliente(nome, email, telefone)
cliente.cadastrar()

idBusca = int(input("digite o ID para buscar: "))
resultado = Cliente.buscar_por_id(idBusca)

if resultado:
    print("cliente encontrado")
    print(f"ID: {resultado[0]}")
    print(f"nome: {resultado[1]}")
    print(f"e-mail: {resultado[2]}")
    print(f"telefone: {resultado[3]}")
else:
    print("hjgvhjv")    