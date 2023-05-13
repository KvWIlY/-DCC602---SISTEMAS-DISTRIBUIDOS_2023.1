import matplotlib.pyplot as plt

tamanhos_testados = [50, 100, 200, 300, 400, 500]

medias = []

for i in tamanhos_testados:
    arquivo = open(f"./logs/use_system_{i}.txt", "r")
    dados = arquivo.readlines()

    uso = 0
    for dado in dados:
        uso += float(dado.split(",")[2])
    medias.append(uso/60)

plt.plot(tamanhos_testados, medias)
# plt.ylim(tamanhos_testados[0], tamanhos_testados[5])
plt.title("Uso da rede por tamanho das mensagens em bytes")
plt.xlabel("tamanho das mensagens em bytes")
plt.ylabel("quantidade media de pacotes recebidos")
plt.savefig("./graficos/uso_medio_rede.png")