# exer 1
nome = "João"

print(nome)
#print("-------------------------------------------------------------------------------------------")

# exer 2
a = 5
b = 10

soma = a + b
sub = a - b
multi = a * b
divi = a / b

print("\nOperações")
print(f"Adição: {a} + {b} = {soma}\nSubtração: {a} - {b} = {sub}\nMultiplicação: {a} * {b} = {multi}\nDivisão: {a} / {b} = {divi}\n")
#print("-------------------------------------------------------------------------------------------")

# exer 3
preco = 50
desconto = 10

res = preco * (10/100)

print(res)
#print("-------------------------------------------------------------------------------------------")

# exer 4
resultado = (10 + 5) * 2

print(resultado)
#print("-------------------------------------------------------------------------------------------")

# exer 5
texto = "150"
convert = int(texto)

conta = convert * 2

print(conta)
#print("-------------------------------------------------------------------------------------------")

# exer 7
'''
a = int(input("\nDigite um valor a ser somado: "))
b = int(input("Digite um valor segundo a ser somado: "))

somar = a + b

print(f"A soma dos valore é {somar}\n")
'''
#print("-------------------------------------------------------------------------------------------")

# exer 8
'''
x = int(input("Insira um valor: "))
y = int(input("Insira um outro valor: "))

divi = x // y

print(f"O resultado da divisão inteira é {divi}")
'''
#print("-------------------------------------------------------------------------------------------")

# exer 9
'''
num1 = int(input("\nDigite um número: "))
num2 = int(input("Digite um outro número: "))

print(f"Caso o número {num1} for maior que {num2}, irá aparecer TRUE.Caso ao contrario aparecerá FALSE.\n{num1 > num2}")

'''
#print("-------------------------------------------------------------------------------------------")

# ex 10
'''
idade = int(input("Insira a sua idade: "))

diasvivi = idade * 365

print(f"Essa é a quantidade de dias que vc já viveu, {diasvivi}")
'''
#print("-------------------------------------------------------------------------------------------")

# ex 11
'''
base = int(input("Insira a base: "))
expo = int(input("Insira o expoente: "))

resultado = base ** expo

print(f"A potencia dos números é {resultado}")
'''
#print("-------------------------------------------------------------------------------------------")

# ex 12
'''
preco = float(input("Insira o preço: "))

stringPreco = str(preco)

print(f"O preço é R${stringPreco}")
'''
#print("-------------------------------------------------------------------------------------------")

# ex 13
'''
raio = float(input("Insira o raio: "))

area = 3.1415 (raio ** 2)

print(f"Area do circulo é {area}")
'''
#print("-------------------------------------------------------------------------------------------")

# ex 14
'''
a = int(input("Digite um número: "))
b = int(input("digite um outro número: "))

a, b = b,a

print(f"O resultado: {a} e {b}")
'''
#print("-------------------------------------------------------------------------------------------")

# ex 15
'''
nota1 = float(input("Insira a primaira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

ps1 = 2
ps2 = 3
ps3 = 5

medpo = (nota1 * ps1 + nota2 * ps2 + nota3 * ps3)/(ps1 + ps2 + ps3)

print(f"A media ponderada é {medpo}")
'''
#print("-------------------------------------------------------------------------------------------")

# desafio
'''
import math

x1 = float(input("Insira o primeiro ponto: "))
x2 = float(input("Insira o segundo ponto: "))
y1 = float(input("Insira o terceiro ponto: "))
y2 = float(input("Insira o quarto ponto: "))

dis = math.sqrt(((x1 - y1)** 2) + ((x2 - y2)** 2))
print(f"O resultado da distância entre os pontos é {dis}.")
'''
#print("-------------------------------------------------------------------------------------------")
