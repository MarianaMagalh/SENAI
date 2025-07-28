# exer 1
"""
historico_pedidos = [
    {'ID': 1, 'Nome': 'João', 'Endereco': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preco': 50, 'Data': '01/01/2023'},
    {'ID': 2, 'Nome': 'Mariana', 'Endereco': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preco': 120, 'Data': '02/01/2023'},
    {'ID': 3, 'Nome': 'Carlos', 'Endereco': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preco': 80, 'Data': '03/01/2023'},
    {'ID': 4, 'Nome': 'Fernanda', 'Endereco': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preco': 150, 'Data': '04/01/2023'}
]

with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/pedidos.xls", "w", encoding="utf-8") as arquivo:
    cabecalho = historico_pedidos[0].keys()
    arquivo.write(";".join(cabecalho) + "\n")
    for pedido in historico_pedidos:
        linha = ";".join(str(pedido[campo]) for campo in cabecalho)
        arquivo.write(linha + "\n")



# exer 2
with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/pedidos.xls", "r", encoding="utf-8") as entrada:
    linhas = entrada.readlines()

with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/pedidos_convertido.csv", "w", encoding="utf-8") as saida:
    for linha in linhas:
        saida.write(linha)


# exer 3
import json

with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/pedidos_convertido.csv", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip().split(";")
dados = []

for linha in linhas[1:]:
    valores = linha.strip().split(";")
    registro = {cabecalho[i]: valores[i] for i in range(len(cabecalho))}
    dados.append(registro)

with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/pedidos.json", "w", encoding="utf-8") as json_file:
    json.dump(dados, json_file, ensure_ascii=False, indent=4)



# exer 4 - desafio
def decifrar_cesar(texto, deslocamento=3):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_codigo = (ord(char) - base - deslocamento) % 26 + base
            resultado += chr(novo_codigo)
        else:
            resultado += char
    return resultado

with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/LOPAL-Aula11-ManipulacaoArquivo-Exercicios-Criptografado.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()


mensagem_decifrada = [decifrar_cesar(linha.strip()) for linha in linhas]


with open("C:/Users/maria/LOPAL-1/1 SEMESTRE\MANIPULAÇÃO ARQUIVOS/tarefa da semana/mensagem_decifrada.txt", "w", encoding="utf-8") as saida:
    for linha in mensagem_decifrada:
        saida.write(linha + "\n")

"""