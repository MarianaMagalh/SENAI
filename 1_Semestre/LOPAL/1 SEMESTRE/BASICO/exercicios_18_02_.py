# exercicio 1
# soma de dois números dado pelo usuário
print("Soma dos Valores!")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))

soma = num1 + num2

print(f"\nA soma dos números é {soma}.")
print("-----------------------------------------------------------------")

# exercicio 2
# verificação do resultado anterior é ímpar
print("Verificação do resultado é par ou ímpar!")
resul =  soma % 2 == 0

print(f"Se for um número ímpar é aparecerá falso, caso ao contario é verdadeiro: {resul}")
print("-----------------------------------------------------------------")

# exercicio 3
# verificar se o primeiro valor é maior que 3 e o segundo menor que 4
print("Maior que 3 e Menor que 4?")
print(f"O valor 1 é maior que 3: {num1 > 3}\nO valor 2 é menor que 4: {num2 < 4}")
print("-----------------------------------------------------------------")

# exercicio 4
# valor absoluto
print("Número Absoluto!")
# função abs() guarda o valor do usuário e retorna o valor absoluto
print(f"O número absoluto do valor 1 e valor 2 é: {abs(num1)} e {abs(num2)}")
print("-----------------------------------------------------------------")

# exercicio 5
# verificação de números pares
print("Ambos os valores são pares?")
#verifica se o resto da divisão por dois é zero
val1 = num1 % 2 == 0
val2 = num2 % 2 == 0

print(f"Os dois valores são pares: {val2 == val1}")
print("-----------------------------------------------------------------")

# exercicio 6
# verificação de um dos valores como negativo
print("Um dos valores é negartivo?")
print(f"O primeiro valor é negativo: {num1 < 0}")
print(f"O segundo valor é negativo: {num2 < 0}")
print("-----------------------------------------------------------------")

# exercico 7
# calculando a media dos 2 valores do usuario e o resultado
print("Calculo da média")
media = num1 + num2 + resul/3
print(f"A média é: {media}")
print("-----------------------------------------------------------------")

# exercicio 8
# exibir que o num1 + 15 é igual a num2 * 3
print("True or False?")
valores = num1 + 15 == num2 * 3

print(f"O valor 1 + 15 é igual a o valor 2 * 3: {valores}")
print("-----------------------------------------------------------------")

# exercicio 9
# calcular resultado e o resto da divisão do dividendo e o divisor, exibir tudo!
print("Dividendo e Divisor")
dividendo = int(input("Digite o primeiro valor a ser dividido: "))
divisor = int(input("Digite o segundo valor a ser divisor: "))

resto = dividendo % divisor
resultado = dividendo // divisor

print(f"Dividendo: {dividendo} e divisor: {divisor}")
print(f"Calculo: {dividendo} / {divisor} = {resultado}")
print(f"Resto da divisão: {resto}")
print("-----------------------------------------------------------------")

# exercicio 10
# conversão de temperaturas, celsius para fahrenheit
print("Celsius para Fahrenheit!")
cel = int(input("Insira a temperatura em graus Celsius: "))

fahr = cel * 1.8 + 32

print(f"A temperatura {cel}C° em Fahrenheit é {fahr}F°.")
print("-----------------------------------------------------------------")

# exercicio 11
# calculo do imc
print("IMC!")
peso = float(input("Insira o seu pseo(kg): "))
alt = float(input("Insira a sua altura(m): "))

imc = peso / (alt ** 2)
# o uso dos caracter ":,.Xf", foi para delimitar o número de casas decimais
print(f"O seu IMC é {imc:,.4f}.")
print("-----------------------------------------------------------------")

# exercicio 12
# calculo da media ponderada, notas com pesos diferentes
print("Média Ponderada!")
not1 = int(input("Insirá a primeira nota: "))
not2 = int(input("Insirá a segunda nota: "))
not3 = int(input("Insirá a terceira nota: "))

ps1 = int(input("Qual o peso da primeira nota? "))
ps2 = int(input("Qual o peso da segunda nota? "))
ps3 = int(input("Qual o peso da terceira nota? "))

meP = (not1 * ps1 + not2 * ps2 + not3 * ps3)/(ps1 + ps2 + ps3)

print(f"A média ponderada é {meP}.")
print("-----------------------------------------------------------------")

# exercicio 13
# calculo da potencia de um número inteiro elevado a um expoente
print("Pontência!")
num = int(input("Insirá um número: "))
expo = int(input("Insirá o expoente desse número: "))

pote = num ** expo

print(f"A potência do {num} elevado à {expo} é {pote}.")
print("-----------------------------------------------------------------")

# desafio 1
# calculo da raiz cúbica de um número
print("Raiz Cúbica!")
valor = int(input("Digite um número: "))
raz = valor ** (1/3)
print(f"A raiz cúbida de {valor} é {raz}.")
print("-----------------------------------------------------------------")

# desafio 2
# calculo após um periodo de tempo com juros
capi = int(input("Quanto é o capital: "))
juros = float(input("Insira o juros: "))
temp = int(input("Insira o tempo: "))
# calculo do montante final
rest = capi * (1 + juros)**temp
print(f"O resultado final é de {rest:,.6f}.")

print("-----------------------------------------------------------------")
print("FIM DA LISTA DE EXERCICIO :)")
print("-----------------------------------------------------------------")