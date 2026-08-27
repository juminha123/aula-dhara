from datetime import datetime
ano_nasc = float(input("me informe a sua data de nascimento: "))
agora = datetime.now()
ano = agora.year

resultado = ano - ano_nasc
print(resultado)