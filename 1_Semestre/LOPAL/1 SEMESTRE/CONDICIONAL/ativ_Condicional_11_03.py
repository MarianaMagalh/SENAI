# Condicional
#n = 12

#if n < 2:
    #print("criança")
#elif n < 18:
    #print("adolecente")
#else:
    #print("adulto")

# ex 1
#idade = int(input("Qual a sua idade? "))

#if idade < 18:
    #print("Você é menor de idade!")
#else:
    #print("Você é maior de idade!")

# ex 2
#nota = float(input("Qual a nota do aluno? "))

#if nota >= 9.0:
    #print("Excelente")
#elif nota >= 7.0:
    #print("Boa")
#elif nota >= 5.0:
    #print("Media")
#else:
    #print("Insuficiente")

# ex 3
'''
num = int(input("Insira um número: "))

if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

if num % 3 == 0:
    print(f"O número {num} é multiplo por 3")
elif num % 5 == 0:
    print(f"O número {num} é multiplo de 5")
else:
    print("o número não é multiplo por 3 e nem por 5")
'''

# ex 4
'''
num1 = int(input("Insira um número: "))
num2 = int(input("Insira um outro número: "))

if num1 < num2:
    print(f"{num1} é menor que {num2}")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print("Os números são iguais")
'''

# ex 5
'''
idade = int(input("Insirá uma idade:"))

if idade <2:
    print("Bebe")
elif idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
'''

# ex 6
'''
tipotemp = input("Escolha a temperatura que deseja realizar a conversão:\nCelsius - C ou Fahrenheit - F").upper()
# upper() - deixa a entrada do usuario em maiuscula
# lower() - deixa a entrada do usuario em minusculo 

if tipotemp == 'F':
    print("Converter para fahrenheit")
    cel = float(input("Qual a temperatura em celsius que sera convertida? "))
    fah = (cel * 1.8) + 32
    print(f"Resultado: {fah}F°")
elif tipotemp == 'C':
    print("Converter para celsius")
    fahr = float(input("Qual a temperatura em fahrenheit que sera convertida?"))
    cels = (fahr - 32) / 1.8
    print(f"Resultado: {cels}C°")
else:
    print("Valor incompativel")
'''

# ex 7
'''
print("Verificação de triangulo")
num1 = int(input("Insira o primeiro lado do triangulo: "))
num2 = int(input("Insira o segundo lado do triangulo: "))
base = int(input("Insira a base do triangulo: "))

if (num1 + num2) > base and (num2 + base) > num1 and (base + num1) > num2:
    print("É um triangulo")

    if num1 == num2 == base:
        print("O triangulo é equilátero")
    elif num1 == num2 != base:
        print("O triangulo é isósceles")
    else:
        print("O triangulo é escaleno")
else:
    print("Não é um triangulo")
'''









