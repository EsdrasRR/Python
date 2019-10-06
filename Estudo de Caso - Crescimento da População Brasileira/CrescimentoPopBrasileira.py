# Cresimento da População Brasileira 1980-2016
# DataSus
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

title = "Crescimento da População Brasileira 1980-2016"
xlabel = "Ano"
ylabel = "População x100.000.000"

for i in range(len(dados)) : 
    if i !=0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)


plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color="k", linestyle="--")
plt.show()
plt.savefig("PopulacaoBrasileira.png", dpi=300)