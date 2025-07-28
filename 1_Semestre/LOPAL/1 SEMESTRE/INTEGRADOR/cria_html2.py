import pandas as pd

arquivo_html = 'index.html'

df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv')
print(df.columns)

def inserir_emoji(dado):
        if dado == '1':
            return '🔴'
        elif dado == '2':
            return '🟡'
        elif dado == '3':
            return '🟢'

pagina = """<html>
<head>
    <title>Status das Esteiras</title>
    <style>
        body { 
            background-color: #f4f4f4; 
            padding: 20px;
        }
        h1 { 
            text-align: center; 
            color: #333; 
        }
        table { 
            width: 80%; 
            margin: auto; 
            border-collapse: collapse; 
        }
        th, td { 
            padding: 12px; 
            text-align: center; 
            border: 1px solid #ccc; 
        }
    </style>
</head>
<body>
    <h1>Status das Esteiras - Monitoramento de Estoque</h1>
    <table>
        <tr>
            <td>Data</td>
            <td>Time</td>
            <td>Esteira 1</td>
            <td>Esteira 2</td>
            <td>Esteira 3</td>
        </tr>
"""

for _, linha in df.iterrows():
    esteira1 = inserir_emoji(linha['esteira1'])
    esteira2 = inserir_emoji(linha['esteira2'])
    esteira3 = inserir_emoji(linha['esteira3'])

    pagina += f'<tr><td>{linha["Date"]}</td><td>{linha["Time"]}</td><td>{esteira1}</td><td>{esteira2}</td><td>{esteira3}</td></tr>\n'

pagina += '</table>\n</body>\n</html>'

with open(arquivo_html, 'w', encoding='utf-8') as arquivo:
    arquivo.write(pagina)
