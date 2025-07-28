# exer 1
'''
num = int(input("Insira um número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} não é par.")
'''

# exer 2
'''
num =  int(input("Insira um número: "))

if num > 10:
    print(f"O número {num} é maior que 10.")
else:
    print(f"O número {num} não é maior que 10.")
'''

# exer 3
'''
idade = int(input("Insira a sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Parece que você não é maior de idade.")
'''

# exer 4
'''
idade = int(input("Qual a sua idade: "))

if idade < 16:
    print("Voto não obrigatorio. Você ainda não tem idade para votar!")
elif idade >= 60:
    print("Voto Opcional. Não há a necessidade de voto.")
else:
    print("Voto obrigatório.")
'''

# exer 5
'''
num = int(input("Insira o número: "))

if num == 0:
    print(f"O número é {num}")
elif num >= 0:
    print("O numero é positivo!")
else:
    print("O número é negativo")
'''

# exer 6
'''
nota = int(input("Insira a nota do aluno: "))

if nota >= 9:
    print("A")
elif nota == 7:
    print("B")
elif nota >= 5:
    print("C")
elif nota >= 3:
    print("D")
else:
    print("E")
'''

# exer 7
'''
idade =  int(input("Informe a sua idade, para saber de tem direito a desconto:"))

if idade >= 18 and idade <= 60:
    print("Você não tem direito a desconto.")
else:
    print("Você tem direito a desconto")
'''

# exer 8
'''
lad1 = int(input("Insira o tamanho de um dos lados do possivel triangulo: "))
lad2 = int(input("Insira o tamanho de um dos lados do possivel triangulo: "))
base = int(input("Insira o tamanho da base do possivel triangulo: "))


if (lad1 + lad2) >= base:
    print("É um triangulo")
    if lad1 == lad2 and lad2 == base and base == lad1:
        print("Triangulo equilátero")
    elif lad1 == lad2 and lad1 != base:
        print("Triangulo isósceles")
    else:
        print("Triangulo escaleno")
elif (lad2 + base) >= lad1:
    print("É um triangulo")
    if lad1 == lad2 and lad2 == base and base == lad1:
        print("Triangulo equilátero")
    elif lad1 != lad2 and lad1 != base and lad2 != base:
        print("Triangulo escaleno")
    else:
        print("Triangulo isosceles")
elif (lad1 + base) >= lad2:
    print("É um triangulo")
    if lad1 == lad2 and lad2 == base and base == lad1:
        print("Triangulo equilátero")
    elif lad1 == lad2 and lad1 != base:
        print("Triangulo isósceles")
    else:
        print("Triangulo escaleno")
else:
    print("Não é um triangulo")
'''

# exer 9
'''
valor = int(input("Qual o valor da compra? "))

if valor < 100:
    desconto = valor * (5/100)
    print(f"Você recebeu o desconto de 5%. O valor da sua compra é de R${desconto}")
elif valor >= 100 and valor <= 500:
    desconto = valor * (10/100)
    print(f"Você recebeu o desconto de 10%. O valor total da compra é R${desconto}")
else:
    desconto = valor * (15/100)
    print(f"Você recebeu o desconto de 15%. O valor total da compra é R${desconto}")
'''

# exer 10
'''
ano = int(input("Insira um ano: "))

if ano % 4 == 0 or ano % 400 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

'''

# exer 11
'''
altura = float(input("Insira a sua altura: "))
peso =  float(input("Insira o seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal.")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")

'''

# exer 12
'''
num1 = int(input("Insira um número: "))
num2 = int(input("Insira um outro número: "))
num3 = int(input("Insira mais um número: "))

if num1 == num2 and num2 == num3 and num3 == num1:
    print("São iguais.")
elif num1 < num2 and num1 < num3 and num2 < num3:
    print("Crescente.")
elif num1 > num2 and num2 > num3 and num1 > num3:
    print("Decrescente.")
else:
    print("numeros invalidos")
'''

# exer 13
'''
temC = float(input("Insira a temperantura atual: "))

if temC < 10:
    print("Frio")
elif temC >= 10 and temC < 25:
    print("Aconchegante")
elif temC >= 25 and temC < 40:
    print("Quente")
else:
    print("Muito Quente")
'''

# exer 14
'''
from datetime import datetime

data = input("Insira uma data: ")

data2 = datetime.strptime(data, "%d/%m/%Y")
print(data2)
'''


# exer 15
'''
import re

senha = input("Insira uma senha: ")

if len(senha) < 8:
    print("Senha inválida")
    print("A senha deve ter no minimo 8 caracteres.")
elif senha.islower():
    print("Senha inválida")
    print("A senha precisa ter pelo menos um caractere maiusculo.")
elif senha.isalpha():
    print("Senha inválida")
    print("A senha precisa ter um número.")
elif senha.isalnum():
    print("Senha inválida")
    print("A senha precisa de um caracter especial.")
else:
    print("Senha válida")
'''

# exer 16
'''
numero = float(input("Digite um número: "))

if numero < 0:
    print("Digito invalido, insira um numero positivo.")
elif numero > 100:
    print("Digito invalido, insira um numero menor que 100")
else:
    calculo = numero ** (1/2)
    print(f"A raiz quadrada é {calculo:,.2f}")
'''

# exer 17
'''
import re

data = input("Insira uma data: ")

regra = r"^\d{2}/\d{2}/\d{4}$"
valid = re.match(regra, data)

if valid:
    dia, mes, ano = data.split('/')
    datam = f'{ano}-{mes}-{dia}'
    if int(mes) == 2:
        if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 400 == 0):
            if int(dia) >= 1 and int(dia) <= 29:
                print("Dia valido.")
                print(f"A data formatada é {datam}")
            else:
                print("Dia invalido, insira um dia valido, entre 1 e 29 dias")
        else:
            if int(dia) >= 1 and int(dia) <= 28:
                print(f"Dia valido")
                print(f"A data formatada é {datam}")
            else:
                print("Dia invalido, insira um dia valido, entre 1 e 28 dias")
    elif int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(mes) == 12:
        if int(dia) >= 1 and int(dia) <= 31:
            print("Dia valido")
            print(f"A data formatada é {datam}")
        else:
            print("Dia invalido, insira um dia valido, entre 1 e 31 dias")
    elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
        if int(dia) >= 1 and int(dia) <= 30:
            print("Dia valido")
            print(f"A dara formatda é {datam}")
        else:
            print("Dia invalido, insira um dia valido, entre 1 e 30 dias")
    else:
        print("Mes invalido")
else:
    print("Invalido, insira uma data valida.")
'''

# exer 19 - desafio
import re

cpf = input("Digite o CPF: ")
cpf = re.sub(r'\D', '', cpf)  

if not cpf.isdigit() or len(cpf) != 11:
    print("CPF Inválido")
else:
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cpf[i]) * pesos[i] for i in range(9))
    resto = soma % 11
    primeiro_digito = '0' if resto < 2 else str(11 - resto)

    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cpf[i]) * pesos[i] for i in range(10))
    resto = soma % 11
    segundo_digito = '0' if resto < 2 else str(11 - resto)

    print("CPF Válido" if cpf[-2:] == primeiro_digito + segundo_digito else "CPF Inválido")






