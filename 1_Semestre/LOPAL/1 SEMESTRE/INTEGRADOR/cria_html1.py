import csv
import os
from idlelib.iomenu import encoding
from operator import index

arq_csv = 'LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv'
arq_html = 'index.html'

def converterCSVtoHTML(arq_csv, arq_html):
    try:
        with open(arq_csv, 'r', newline='', encoding='utf-8') as csv_arquivo:
            reader = csv.reader(csv_arquivo) # lendo arquivo
            titulo = next(reader) # criando cabeçalho
            data = list(reader)

        tabela = '<table>\n'
        tabela += '         <tr>\n'
        for cell in titulo:
            tabela += f'            <th>{cell}</th>\n'

        for linha in data:
            tabela += '         <tr>\n'
            for elemento in linha:
                if elemento == '1':
                    elemento += '⚠️'
                elif elemento >= '2':
                    elemento += '✅'
                elif elemento == '0':
                    elemento += '❌'

                tabela +=  f'           <td>{elemento}</td>\n'
            tabela += '         </tr>\n'
        tabela += '     </table>'


        with open(arq_html, 'w', encoding='utf-8') as pagina_html:
            pagina_html.write(f"<!DOCTYPE html>\n"
                              f"<html>\n"
                              f"<head>\n"
                              f"<title>Status das Esteiras</title>\n"
                              """
                              <style>
                                body { font-family: Arial; background-color: #f4f4f4; padding: 20px; }
                                h1 { text-align: center; color: #333; }
                                table { width: 80%; margin: auto; border-collapse: collapse; }
                                th, td { padding: 12px; text-align: center; border: 1px solid #ccc; }
                              </style>
                              """
                              f"</head>\n"
                              f"<body>\n"
                              f"<h1><strong>Status das Esteiras - Monitoramento de Estoque</strong></h1>\n"
                              f"    {tabela}\n"
                              f"</body>\n"
                              f"</html>\n")

            print(f"A tabela foi criada com sucesso no arquivo {arq_html}!")

    except FileNotFoundError:
        print(f"O arquivo CSV: {arq_csv} não foi encontrado!")
    except Exception as error:
        print(f"Houve um erro: {error}")

converterCSVtoHTML(arq_csv, arq_html)
