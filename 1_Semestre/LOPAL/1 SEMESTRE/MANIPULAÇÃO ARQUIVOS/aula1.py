# Manipulação de arquivos
# -> escrita e  leitura

"""
arquivos possiveis de manipular
- txt
- csv
- json
- xml
- excel

# Comandos
- .with open()
- .write()
- .read()

# CSV
- .biblioteca csv
- .writer()
- .writerow()
- .reader()

# JSON
- biblioteca json
- .with open()
- .dump()
- .load()

# XML
- .with open()
- .write()
- .read()

# parametros
- r: read
- a: adicionar
- w: escrever
- x: criar

"""
from xml.etree.ElementTree import indent

"""
# criação de arquivo - TXT
with open("C:/meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Olá mundo!\n")
    arquivo.write("Aprendendo Python\n")

with open("meu_arquivo.txt", "r") as arquivo2:
    print(arquivo2.read())

************************************************************************************************************************

# CSV

import csv
with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/produtos.csv", "w") as arquivoCSV:
    arquivoCSV.write("Nome, Preço\n")
    arquivoCSV.write("Livro, R$20\n")

with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/produtos.csv", "r") as arquivoCSV:
    print(arquivoCSV.read())

outro jeito
with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/produtos.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Preço"])
    writer.writerow(["Livro", 20])

with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/produtos.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader: # printa linha por linha
        print(row)
        
************************************************************************************************************************
            
# JSON
import json

with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/dados.json", "w") as arqJSON:
    json.dump({"nome":"Mariana", "idade": 18}, arqJSON)

with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/dados.json", "r") as arqJSON:
    data = json.load(arqJSON)
    print(data)

************************************************************************************************************************

"""

# XML
xml_str ="""<?xml version="1.0" encoding="UTF-8"?>
<config>
    <versao>1.0</versao>
</config>
"""

with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/config.xml", "w", encoding="UTF-8") as arqXML:
    arqXML.write(xml_str)

with open("C:/Users/56463939811\Desktop/LOPAL/1 SEMESTRE/MANIPULAÇÃO ARQUIVOS/config.xml", "r", encoding="UTF-8") as a:
    conteudo = a.read()
    print(conteudo)

