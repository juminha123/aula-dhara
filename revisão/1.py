import datetime
import random
participantes = []
for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º participante: ")
    participantes.append(nome)

vencedor = random.choice(participantes)
data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M")

arquivo = open("resultado.txt", "w",)
arquivo.write(f"Vencedor do sorteio: {vencedor}\n")
arquivo.write(f"Data e hora do sorteio: {data_formatada}\n")
arquivo.close()
arquivo_leitura = open("resultado.txt", "r",)
conteudo_resultado = arquivo_leitura.read()
arquivo_leitura.close()
print("\n--- RESULTADO LIDO DO ARQUIVO ---")
print(conteudo_resultado)
