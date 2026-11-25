# 1)Escreva um programa que peça à pessoa usuária para fornecer dois 
# números e exibir o número maio

numeros = int(input('Digite dois números separados por espaço:')).split()
maior = max(numeros)

print(f'O maior número digitado é: {maior}')