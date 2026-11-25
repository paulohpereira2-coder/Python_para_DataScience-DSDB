# Exercício 2 - Análise de vendas por setor e cliente
# Uma empresa comercial possui clientes distribuídos em 
# diferentes setores. O departamento comercial deseja 
# analisar os valores das vendas realizadas e identificar quais 
# setores apresentam maior faturamento.
# Desenvolva um programa que organize os dados utilizando 
# Pandas e apresente um gráfico de barras com o faturamento 
# total por setor.
# --------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "cliente": ["C1","C2","C3",
                "C4","C5","C6",
                "C7","C8","C9",
                "C10"],

    "setor":["Tecnlogia","Indústria","Comércio",
             "Tecnlogia","Indústria","Comércio",
             "Tecnlogia","Indústria","Comércio",
             "Tecnlogia"],

    "vendas":[1500,2500,1200,
              3000,4500,2000,
              3500,5000,2800,
              4000]
}

df = pd.DataFrame(dados)

# --------------------------------------------------------------------------
grupo = df.groupby("setor")["vendas"].sum()
print("grupo")
fig, ax = plt.subplots(figsize=(8,5))
grupo.plot(
    kind="bar",
    ax=ax,
    color="steelblue"
)
ax.set_title("Vendas por setor")
ax.set_xlabel("Setor")
ax.set_ylabel("Vendas")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Exercício 2 - Perguntas
# a)Qual setor apresentou o maior faturamento?
# Os setores Indústria e Tecnologia apresentaram os maiores valores de venda com 12mil cada.

# --------------------------------------------------------------------------
# b)Qual setor apresentou o menor faturamento?
# O setor do comercio teve o menor valor de vendas com total de 6mil.

# --------------------------------------------------------------------------
# c)Qual cliente realizou a compra de maior valor?
# Cliente que realizou a maior compra foi o cliente C8 com o valor de 5000.

grupo2 = df.groupby("cliente")["vendas"].sum()
fig, ax = plt.subplots(figsize=(8,5))
grupo2.plot(
    kind="bar",
    ax=ax,
    color="steelblue"
)
ax.set_title("Vendas por setor")
ax.set_xlabel("Cliente")
ax.set_ylabel("Vendas")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------
# d)Como calcular o faturamento total da empresa utilizando df["vendas"].sum()?
# O faturamento total foi de 30000

total_vendas = df["vendas"].sum()
print(f"O faturamento total foi de {total_vendas}")

# --------------------------------------------------------------------------
# e)Como calcular a média das vendas por setor utilizando groupby() e mean()?
# Resp. Média de vendas por setor.
# Comércio     2000.0
# Indústria    4000.0
# Tecnlogia    3000.0

media_setor = df.groupby("setor")["vendas"].mean()
print(media_setor)