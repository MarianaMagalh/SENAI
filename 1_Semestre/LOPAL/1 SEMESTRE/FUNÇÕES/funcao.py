# Função - bloco de codigo autonomi e reutilizavel que é designado para realizar uma tarefa especifica.
"""
def nome_da_funcao(parametro1, parametro2):
    corpo da funcao - instruções

# Exemplo 1
def saudacao():
    print("Ola mundo!")

saudacao()


# Exemplo 2
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado =  calcular_media(nota1, nota2)

print(resultado)


# Quando uma variavel é criada dentro da função, ela é uma variavel local, que só existe dentro da função.
def gjsgi():
    x = 10
    print(x)

gjsgi()
print(x) # ERROR


# Quando uma variavel é criada fora da função, é uma variavel global.
y = 20

def kikiki():
    print(y)

kikiki()
print(y)


# seu valor não pode ser alterado dentro da função, APENAS com um comando especial.
z = 20

def mudar_valor():
    global z
    z = 100

mudar_valor()
print(z)


# exer1
num = int(input("Insira um número: "))

def dobro(num):
    dobro = num * 2
    return dobro - return num * 2

resultado = dobro(num)
print(resultado) - print(dobro())


# exer2
num1 = float(input("Insira um número: "))
num2 = float(input("Insira mais um número: "))

def maior(num1, num2):
    if num1 > num2:
        print(f"O {num1} é maior que {num2}")
        return num1
    elif num1 == num2 and num2 == num1:
        print("Os números são iguais")
        return num2
    else:
        print(f"O {num2} é maior que {num1}")
        return num1


print(maior(num1, num2))


# exer4
lista = [10, 20, 30]

def media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)

print(f"A media é {media(lista)}")
"""


# exer5


def fatorial(num):
    contador = 1

    for i in range(1, num + 1):
        contador *= i

        return contador

num = int(input("Insira um número: "))
print(fatorial(num))




