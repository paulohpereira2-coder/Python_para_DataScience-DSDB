try:

    idade = int(input("Digite sua idade: "))
    print(f'Sua idade é {idade} anos.')

except ValueError:

    print('Erro: digite um número inteiro válido.')