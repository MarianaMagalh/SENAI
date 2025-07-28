# exer 1
"""
a = 5.00
b = 8.00
c = 12.00

def dobro(numero):
    return numero * 2

print(f"O dobro do produto de R${a}, é {dobro(a)}\n"
      f"O dobro do produto de R${b}, é {dobro(b)}\n"
      f"O dobro do produto de R${c}, é {dobro(c)}")


# exer 2
lista = ["João", "Maria", "Carlos"]

def bemVinde(nome):
    return print(f"Bem Vinde {nome}!")

for nomes in lista:
    print(bemVinde(nomes))


# exer 3
import random

lista = range(1, 10 + 1)

numeros = random.choice(lista)

def acao(numero):
    if numero % 2 == 0:
        return print("Jogador Avança")
    else:
        return print("Jogador Recua")


print(f"Posição do Dado: {numeros}")
print(acao(numeros))


# exer 4
numeros = [2, 3, 4]

def tabuada(num):
    contador = 0

    for _ in range(10):
        tabuada = num * (contador + 1)
        contador += 1

        print(f"{num} X {contador} = {tabuada}")

for numero in numeros:
    print(tabuada(numero))


# exer 5

idade_cli = [8, 15, 20]

def verificacao(idade):
    if idade >= 18:
        return print("Você tem idade para ver o filme.\nBom filme!")
    else:
        return print("Você não tem idade para ver o filme.\nEscolha outro filme!")

for idade in idade_cli:
    print(verificacao(idade))


# exer 6
produtos = [50, 120, 200]

def desconto(preco):
    des = preco * (10/100)
    return des

def preco_final(preco):
    preco_final = preco - desconto(preco)
    return preco_final

for produto in produtos:
    print(f"O valor final com desconto é: {preco_final(produto)}")


# exer 7
# len()
poema = ("casa", "paralelepípedo", "python")

def quantidade(palavras):
    return len(palavras)

for palavra in poema:
    print(f"A palavra {palavra} tem {quantidade(palavra)} letras")


# exer 8
tem_celsius = [30, 100, 0]

def converte(temperatura):
    fah = (temperatura * 1.8) + 32
    return fah

for tems in tem_celsius:
    print(f"A temperatura {tems}, convertida é: {converte(tems)}")


# exer 9
desafios = [3, 9, 12]

def dificuldade(desafio):
    if desafio == 3:
        print("O desafio é de pouca dificuldade!")
    elif desafio == 9:
        print("O desafio é de média dificuldade!")
    elif desafio ==  12:
        print("O desafio é de grande dificuldade!")

for desafio in desafios:
    print(desafio)
    print(dificuldade(desafio))


# exer 10
palavras = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]

def palindromos(palavras):
    # na minha cabeça dá para ser um titulo
    if palavras == 'Subi no Onibus' or palavras == 'Ana Ana':
        print(palavras)
        print("É um palíndromos!")
    else:
        print(palavras)
        print("Não é um palíndromos")

for palavra in palavras:
    print(palindromos(palavra))


# exer 12
num_mate = [3, 7, 9, 25, 26]

def conta_fatorial(numero):
    fatorial = 1
    i = 1
    while i <= numero:
        fatorial *= i
        i += 1
    return fatorial

for numero in num_mate:
    print(f"{numero}: {conta_fatorial(numero)}")
"""



