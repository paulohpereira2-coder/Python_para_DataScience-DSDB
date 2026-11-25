# Exercício 1 - Crie uma pasta chama Aula01-Ex1
# Uma indústria utiliza sensores para monitorar a temperatura de uma máquina durante seu funcionamento. Os registros são 
# coletados em intervalos de uma hora.
# Desenvolva um programa em Python que organize os dados em # um DataFrame e apresente um gráfico de linhas, permitindo 
# visualizar a variação da temperatura ao longo do tempo.

import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "tempo": ["08:00","09:00","10:00","11:00","12:00",
              "13:00","14:00","15:00","16:00","17:00"],
    "temperatura": [25,28,32,35,38,42,45,41,37,33]
}

df = pd.DataFrame(dados)

df.plot(
    x="tempo",
    y="temperatura",
    kind="bar",
    legend=False
)

plt.title("Temperatura por hora")
plt.ylabel("Temperatua C")
plt.show()

# ----------------------------------------------------------------------
# Perguntas:
# a)Em qual horário foi registrada a maior temperatura?
# A maior temperatura foi registrada as 14:00 horas com 45 C.

# ----------------------------------------------------------------------
# b) Qual foi a menor temperatura registrada?
# A menor temperatura regístrada foi 25C as 08:00.

# ----------------------------------------------------------------------
# c) Em qual intervalo ocorreu a maior elevação de temperatura?
# A maior elevação foi de 4.0C entre 09:00 e 10:00.

# Calcula a variação de temperatura entre uma linha e a anterior
df["variacao"] = df["temperatura"].diff()

# Descobre o maior valor de elevação
maior_elevacao = df["variacao"].max()

# Localiza a linha onde ocorreu a maior elevação
linha_maior = df[df["variacao"] == maior_elevacao]
hora_fim = linha_maior["tempo"].values[0]
# Pega o horário anterior para formar o intervalo
idx = linha_maior.index[0]
hora_inicio = df.loc[idx - 1, "tempo"]

print(
    f"A maior elevação foi de {maior_elevacao}C entre {hora_inicio} e"
    f" {hora_fim}."
)

# ----------------------------------------------------------------------
# d)Como calcular a temperatura média utilizando 
media =  df["temperatura"].mean()
print(
    f"A média de temperatura foi de {media} C")
