'''
Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu.
 O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

1-A quantidade de números pares e ímpares.
2-A quantidade de números positivos e negativos.
3-A quantidade de números inseridos.
4-O maior e o menor número.
5-A média de números pares.
6-A média de números ímpares.
7-A média de todos os números inseridos.
8-Mostrar os números lidos na ordem inversa.

'''

import os 
os.system("cls || clear")

# Variáveis para armazenar os números
numeros = []
numeros_pares = []
numeros_impares = []


for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Variáveis para armazenar as estatísticas
numeros_pares = 0
quantidade_de_pares = 0
quantidade_de_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = numeros[0]
menor_numero = numeros[0]
soma_pares = 0
soma_impares = 0
soma_geral = 0


for numero in numeros:
    if numero % 2 == 0:
        quantidade_de_pares += 1
        soma_pares += numero
    else:
        quantidade_de_impares += 1
        soma_impares += numero

    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1

    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)

    soma_geral += numero



# Calculando as médias
media_pares = soma_pares / quantidade_de_pares if quantidade_de_pares > 0 else 0
media_impares = soma_impares / quantidade_de_impares if quantidade_de_impares > 0 else 0
media_geral = soma_geral / 5

# Mostrando números na ordem inversa
inverter_numeros = numeros [::-1]

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_de_pares}")
print(f"Quantidade de ímpares: {quantidade_de_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Os números invertidos :{numeros}")