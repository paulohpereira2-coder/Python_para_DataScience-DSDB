# Exemplo 02 - Tipos de prints com os tipos de dados em Python

# variavel para armazenar o nome do aluno

nome_aluno = 'Rocky' # declara a variavel
idade_aluno = 15 # variavel com a idade do aluno
media_aluno = 8.45 # declaração de variavel

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno,idade_aluno,media_aluno))
print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno,idade_aluno,media_aluno))
print('Nome do aluno é {}, ele tem {} anos e sum média é {}.'.format(nome_aluno,idade_aluno,media_aluno))
print(f'Nome do aluno é {nome_aluno}, ele tem {idade_aluno} anos e sua média é {media_aluno:.2f}')