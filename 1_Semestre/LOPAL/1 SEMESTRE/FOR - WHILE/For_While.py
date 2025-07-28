# ex 5
'''
n = int(input("Digite o tamanho da lista: "))

numeros = []
soma = 0

for _ in range(n):
    numero = float(input("Digite um número: "))
    numeros.append(numero) # adição de um elemento no final da lista
    soma = soma + numero
media = soma / n
print(f"A média dos numeros é: {media}")
'''
from math import factorial

# While - estrutura que executa um bloco de código enquanto uma condição específica for verdadeira.
'''
# exe 

x = 0

while x <= 10:
    x = x + 1
    print(x)
'''

# soma += 1 - qunado é a mesma variavel (soma = soma + 1)
# ex 1
'''
num = int(input("Insira um numero de 5 ate 10: "))

if num >= 5 and num <= 10:
    while num > 0:
        num -= 1
        print(num)
else:
    print("Número deve estar entre 5 e 10")
'''

# ex 2
'''
maior = float(0.0)

contador = 1

while contador <= 5:
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero
    contador += 1
print(f"O maior numero é {maior}")

'''

# ex 3
'''
num = int(input("Digite um número: "))

fatorial = 1 
i = 1 

while i <= num:
    fatorial *= i
    i += 1

print(f"O resultado de {num}! é {fatorial}")
'''

# ex 4
'''
n = int(input("Digite o tamanho da lista: "))

numeros = []
contador = 0

while contador < n:
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    contador += 1
media = sum(numeros) / n
print(f"A média dos numeros é {media}")
'''

# ex 5
'''
opcao = 0

while opcao != 5:
    print("Menu:")
    print("1 - somar\n2 - subtrair\n3 - multiplicar\n4 - dividir\n5 - sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        num = float(input("digite o primeiro número: "))
        num3 = float(input("digite o segundo número: "))

        resul = num + num3
        print(f"Resultado: {resul}")
    elif opcao == 2:
        num = float(input("digite o primeiro número: "))
        num3 = float(input("digite o segundo número: "))

        resul = num - num3
        print(f"Resultado: {resul}")
    elif opcao == 3:
        num = float(input("digite o primeiro número: "))
        num3 = float(input("digite o segundo número: "))

        resul = num * num3
        print(f"Resultado: {resul}")
    elif opcao == 4:
        num = float(input("digite o primeiro número: "))
        num3 = float(input("digite o segundo número: "))

        if num3 != 0:
            resul = num / num3
            print(f"Resultado: {resul:.2f}")
        else:
            print("Erro divisão por zero")
    elif opcao == 5:
        print("Saindo...")
'''


# while true - enquanto for verdadeiro, loop infinito que so para com o break, parando o while inteiro
"""
while True:
    bloco a ser repetido
    if condição:
        break

# exemplo 1
while True:
    resposta = input("digite 'sair' para encerrar: ")
    if resposta == 'sair':
        break
        
# comando continue - para o loop , ou pula
for i in range(5):
    if i == 2:
        continue
    print(i)
"""
#  quando usar:
# sei a condição de parada? = while condição
# preciso repetir ate o usuario acertar algo? = while True + break
# quero algo que nunca pare(mas posso encerrar manualmente)? = while True + break

# avaliação
# usado sem entender while = falta de dominio da logica
# usado por preguiça de escrever a condição = desatenção ou habito ruim

# BINGO
# aula - teoria, uso + codigo e exercicio

































