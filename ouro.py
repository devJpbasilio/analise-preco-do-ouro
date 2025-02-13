import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


dfs = [] # Cria uma lista vazia

df = pd.read_csv('/home/joao/PycharmProjects/preco-historico-do-ouro/ouro_limpo.csv') # Passa o Caminho e leitura do arquivo

# print(df.isnull().sum())
# df.info()
# df.describe()

df['Data'] = pd.to_datetime(df['Data']) # Conversão para o tipo datetime

# Filtragem dos dados
for ano in range(2019, 2025):
    df_ano = df[df['Data'].dt.year == ano] 
    dfs.append(df_ano)

df = pd.concat(dfs) # Adiciona a lista dfs


# Renomeando colunas
df = df.rename(columns= {
    "Data": "data",
    "Fechamento": "preço"
})

df["preço"] = df["preço"].round(2) # Arredondamento dos valores do preço

#Criação do grafico
fig = plt.figure()
ax = fig.add_subplot()

ax.plot(df["data"], df["preço"], color="gold")
ax.fill_between(df["data"], df["preço"], color="gold", alpha = 0.5) 

ax.set_xlim(df["data"].iloc[0], df["data"].iloc[-1])
ax.set_ylim(0, df["preço"].max() * 1.1)

# Adicionando rótulos e título
ax.set_title("Grama do Ouro (2019-2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("Preço (R$)")

ax.xaxis.set_major_locator(mdates.YearLocator()) # Exibe apenas anos no eixo X
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

plt.show()
print(df)