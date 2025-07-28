# exer 1
'''
contador = 0

for num in range(11):
    resposta = int(input("Digite um número: "))
    if resposta % 3 == 0:
        print(f"O número {resposta} é multiplo ")
        contador += 1
    else:
        print(f"Número {resposta} não é multiplo")
print(f"a quatidade dos números multiplos de 3: {contador}")
'''




# exer 2
'''
print("Tentativas de Senhas")
while True:
    senha = input("Digite a 'senha correta' correta: ")
    if senha == 'senha correta':
        break
'''

# exer 3
'''
while True:
    print("Menu:")
    print("sorvete")
    print("bolo")
    print("torta de morango")
    print("mousse de limão")
    print("bombom de morango")
    print("sair")

    op = input("Escolha uma das opções acima: ")

    if op == 'sair':
        break
'''

# exer 4
'''
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

comeco = min(num1, num2)
final = max(num1, num2)

for i in range(comeco + 1, final):
    primo = True

    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(f"{i} é primo")
'''


# exer 5
'''
senha = '1234'

contador = 0

while contador < 4:
    senhaofc = input("Insira a sua senha: ")
    if senha == senhaofc:
        print("Seja bem vinde!")
        break
    else:
        contador += 1
        if contador == 3:
            print("Acesso bloqueado")
            break
'''


# exer 6
'''
pares = []
impares = []

for num in range(10):
    numeros = int(input("Insira um numero: "))

    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)


print(f"Lista de pares\n{pares}")
print(f"Lista de impares\n{impares}")
'''

# exer 7
'''
frase = input("Insira um frase: ")
frase = frase.lower()

conA = 0
conE = 0
conI = 0
conO = 0
conU = 0

for letra in frase:
    if letra == 'a':
        conA += 1
    elif letra == 'e':
        conE += 1
    elif letra == 'i':
        conI += 1
    elif letra == 'o':
        conO += 1
    elif letra == 'u':
        conU += 1
    
if conA == 0 and conE == 0 and conI == 0 and conO == 0 and conU == 0:
    print("Não há vogais nessa palavra/frase")
else:
    print(f"Quantidade de vogais na palavra/frase {frase}")
    print(f"A: {conA}\nE: {conE}\nI: {conI}\nO: {conO}\nU: {conU}")
'''

# exer 8
'''
import random

contCara = 0

while contCara < 3:
    moeda = random.choice(['cara', 'coroa'])
    print(moeda)
    if moeda == 'cara':
        contCara += 1
    else:
        contCara = 0
'''

# exer 9
'''
lisNum = []

while True:
    numeros = input("Insira um número: ")
    if numeros == 'sair':
        break
    else:
        numero = int(numeros)
        lisNum.append(numero)

media = sum(lisNum) / len(lisNum)

contMenos = 0

for num in lisNum:
    if num < media:
        contMenos += 1

print(f"A media: {media}\nNúmero que são menores do a media: {contMenos}")
'''


# exer 10
'''
sequencia = []

while True:
    numeros = input("Insira um número: ")
    if numeros == 'sair':
        break
    else:
        numero = int(numeros)
        sequencia.append(numero)

if len(sequencia) < 2:
    print("Impossivel realizar a procura")
else:
    sequencia = list(set(sequencia))
    sequencia.sort()
    segMaior = sequencia[1]
    print(f"O segundo maior é {segMaior}")
'''

# exer 11
'''
a = 1
b = 2
c = 0

for i in range(1, 6):
    if i % 2 == 0:
        a += i
    else:
        b *= i
    c = a + b
print(a, b, c)
'''


# exer 12
'''
x = 3
y = 2
z = 0

while x < 8:
    for j in range(2):
        z += y
        y += 1
    x += 1

print(x, y, z)
'''


# Desafio 1
'''
popuCoelho = int(input("Insira a quantidade de coelho: "))
geração = int(input("Ate quantas gerações vc deseja ir: "))

while True:
    taxaRepro = float(input("Insira a taxa de reprodução: ex: 0.2 "))
    taxaMor = float(input("Insira a taxa de mortalidade: ex: 0.1"))

    gera = 0
    while gera < geração:
        popuCoelho = popuCoelho * (1 + taxaRepro - taxaMor)
        gera += 1

        print(f"--- Geração: {gera}° --- População: {popuCoelho:.1f}")
        print(f"--- Taxa Reprodução: {taxaRepro} --- Taxa Mortalidade: {taxaMor}")

    break
'''

# Desafio 2
'''
import random

palavras = ['abacaxi', 'banana', 'morango', 'melancia', 'uva', 'laranja']
palavra = random.choice(palavras)


oculta = ["_" for _ in palavra]

letErradas = []
letCertas = []
tentativas = 6

print(" Jogo da Forca ")

while True:
    print("\nPalavra: ", " ".join(oculta))
    print("Letras erradas:", ", ".join(letErradas))
    print(f"Tentativas restantes: {tentativas}")

    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra.")
        continue

    if letra in letCertas or letra in letErradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra:
        letCertas.append(letra)
        for i in range(len(palavra)):
            if palavra[i] == letra:
                oculta[i] = letra
        print("Letra correta!")
    else:
        letErradas.append(letra)
        tentativas -= 1
        print("Letra errada!")

    if "_" not in oculta:
        print("\nParabéns! Você ganhou!")
        print("A palavra era:", palavra)
        break

    if tentativas == 0:
        print("\nVocê perdeu!")
        print("A palavra era:", palavra)
        break
'''






