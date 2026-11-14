# Exercício 3 - 
# Uma empresa de investimentos deseja analisar a evolução 
# dos preços das ações de uma companhia negociada na 
# Bolsa de Valores.
# Durante 10 dias, foram registrados os preços de fechamento 
# das ações. O objetivo é utilizar Python, Pandas e Matplotlib 
# para organizar os dados e visualizar a variação dos preços 
# ao longo do período.

# Exercício 3 - Desenvolva um programa que crie um DataFrame 
# com os valores das ações e apresente um gráfico de linhas, 
# permitindo identificar períodos de valorização e desvalorização. 


import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "dia": ["D1","D2","D3",
            "D4","D5","D6",
            "D7","D8","D9",
            "D10"],
    "preco": [25.50,26.20,25.80,
              27.00,28.50,27.80,
              29.20,30.50,29.80,
              31.00]
}

df = pd.DataFrame(dados)

print(df)

fig, ax = plt.subplots(figsize=(9, 5))

df.plot(
    x = "dia",
    y = "preco",
    kind = "line",
    ax = ax,
    marker = "o",
    color = "royalblue",
    linewidth = 2,
    legend = True,
)

# Loop para adicionar o rótulo de dados em cima de cada ponto
for x, y in zip(range(len(df)), df["preco"]):
  ax.annotate(
      f"R$ {y:.2f}",  # Texto formatado com o valor (ex: R$ 25.50)
      (x, y),  # Coordenada (X, Y) do ponto
      textcoords="offset points",  # Como o deslocamento será medido
      xytext=(0, 8),  # Deslocamento em pixels (0 para os lados, 8 para cima)
      ha="center",  # Alinhamento horizontal centralizado
      fontsize=9,
      fontweight="bold",
      color="darkblue",
  )

ax.set_title("Evolução do Preço das Ações", fontsize=12, fontweight="bold")
ax.set_xlabel("Dias", fontsize=10)
ax.set_ylabel("Preço (R$)", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------
# Perguntas
# a) Qual foi o maior preço registrado durante os 10 dias?
# Resp. O maior preço registrado no período foi de 31R$

# -------------------------------------------------------------------------
# b)Qual foi o menor preço registrado?
# Resp. O menor preço registrado no período foi de R$25,50

# -------------------------------------------------------------------------
# c)Em quais dias ocorreram quedas no preço das ações?
# Resp. Tivemos queda de preço nos dias D3(25.8), D6(27.8) e D9(29.8).

# -------------------------------------------------------------------------
# d)Qual foi a média dos preços de fechamento?
# Resp. A média de preços foi 28.13.

media_preco = df["preco"].mean()
print(f"Resp. Questão d) A média de preços foi {media_preco:.2f}.")
# -------------------------------------------------------------------------
# e)Se um investidor comprou 100 ações no primeiro dia e vendeu todas no último dia, qual seria o lucro 
# obtido, desconsiderando taxas e impostos?
# Resp.
# Preço de compra em (D1): R$25.5 (Total: R$ 2550.00)
# Preço de venda (D10): R$ 31.00 (Total: R$ 3100.00)
# Lucro líquido obtido: R$ 550.00


# Variável de ações compradas
qtd_ac = 100

# Vamos localizar o preço do primeiro dia e do último dia.
preco_compra = df["preco"].iloc[0]
preco_venda = df["preco"].iloc[-1]

# Calculo do lucro

valor_investido = preco_compra * qtd_ac
valor_final = preco_venda * qtd_ac
lucro_total = valor_final - valor_investido

print(
  f"Resp. Questão e) Preço de compra em (D1): R${preco_compra} (Total: R$"
  f" {valor_investido:.2f})"
)

print(f"Preço de venda (D10): R$ {preco_venda:.2f} (Total: R$ {valor_final:.2f})")
print(f"Lucro líquido obtido: R$ {lucro_total:.2f}")