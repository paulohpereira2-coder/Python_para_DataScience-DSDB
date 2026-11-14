# Exemplo 07

nome, idade, cidade = input(
    'Digite nome, idade e cidade separados por espaço:'
).split()

idade = int(idade)

print(f'{nome} tem {idade} anos e mora em {cidade}.')