#Declarando e atribuindo valores a variáveis`

idade = 18
nome = 'Mariana'
altura = 1.64
#exibindo os valores das variaveis

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

# exercicio 1
Idade = 18
Nome = "Mariana "
print("Olá, meu nome é ",Nome," e tenho ",Idade," anos")


nome1 = 'aula'
nome2 = 'python'

#Variavel temporária para armazenar o valor de 'a'
temp = nome1

#Atribui o valor de 'b' à variavel 'a'
nome1 = nome2

#Atribui o valor anterior de 'a' variavel 'b'(armazenado em 'temp')
nome2 = temp

print("O valor de a após a troca é:", nome1)
print("O valor de b após a troca é", nome2)

# exercicio 2
nome1 = 'Mariana Macena'
nome2 = "de Magalhães"
nome_completo = nome1 + " " + nome2

print("Nome_Completo:" ,Nome_Completo)

# exercicio 3
alimento1 = 'Banana'
alimento2 = 'Tomate'
alimento3 = 'Cebola'

#print("Hoje, eu vou preparar uma saladinha com ",Alimento1,", ",Alimento2,", e ",Alimento3)
receita =f"Hoje vou preparar uma saladinha de {alimento1}, {alimento2}, {alimento3}."
print(receita)

dia = 11
mes = '02'
ano = 2025
data = f"{dia}/{mes}/{ano}"

print(data)