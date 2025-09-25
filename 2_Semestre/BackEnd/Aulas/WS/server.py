# Importações necessárias:
# - os: Para manipular caminhos de arquivos e diretórios (ex: os.path.join para construir caminhos absolutos).
# - json: Para carregar (json.load) e salvar (json.dump) os dados dos filmes em formato JSON (persistência simples).
# - http.server: Fornece as classes base para criar um servidor HTTP simples (HTTPServer e SimpleHTTPRequestHandler).
# - urllib.parse: Para parsear URLs (urlparse para extrair paths) e dados de formulários (parse_qs para forms urlencoded).
import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

# Classe personalizada que herda de SimpleHTTPRequestHandler.
# Ela estende o handler padrão para adicionar lógica personalizada em métodos como do_GET e do_POST.
# Isso permite definir rotas específicas e respostas dinâmicas, em vez de só servir arquivos estáticos.
class MyHandle(SimpleHTTPRequestHandler):
    
    # Método sobrescrito: Personaliza a listagem de diretórios (chamado quando o browser acessa uma pasta).
    # Tenta servir um 'index.html' estático se existir; caso contrário, usa o comportamento padrão.
    def list_directory(self, path):  # class base
        try:
            # Constrói o caminho para 'index.html' no diretório fornecido e abre o arquivo.
            # abrindo e lendo o arquivo e mandando a resposta estatica
            f = open(os.path.join(path, 'index.html'), encoding='utf-8') 
            
            # Envia resposta HTTP 200 (sucesso) para o browser.
            self.send_response(200)  # resposta para o browser, 'SUCCESS'
            # Define o header Content-type como HTML para o browser interpretar corretamente.
            self.send_header("Content-type", "text/html")  # enviado as infos do header
            # Finaliza os headers da resposta HTTP.
            self.end_headers()  # fechando o header
            # Escreve o conteúdo do arquivo no stream de saída (wfile) para o browser, codificado em UTF-8.
            self.wfile.write(f.read().encode('utf-8'))  # fluxo de saida do browser
            # Fecha o arquivo para liberar recursos.
            f.close()
            
            # Retorna None para interromper o list_directory padrão (não lista arquivos da pasta).
            return None 
        except FileNotFoundError:  # se não achar o arquivo
            # Ignora o erro e continua com o comportamento padrão se o arquivo não existir.
            pass
        
        # Chama o método padrão da classe pai para listar o diretório se necessário (ex: mostra arquivos).
        return super().list_directory(path)
    
    # Função auxiliar para validar login (exemplo simples e hardcoded, não seguro para produção).
    # Parâmetros: login (email) e password (senha como string).
    # Retorna uma mensagem de texto para exibir no browser (sucesso ou erro).
    def accont_user(self, login, password):  # Corrigi 'passaword' para 'password'
        # Credenciais fixas (em um app real, use banco de dados ou autenticação segura).
        loga = "mariana@gmail.com"
        senha = "1234"  # Mudei para str para evitar erros de int (não force conversão).
        
        # Verifica se as credenciais fornecidas batem com as fixas.
        if login == loga and password == senha:
            return "Usuario Logado"  # Mensagem de sucesso.
        else:
            return "Usuario não existe"  # Mensagem de erro.
    
    # Função auxiliar: Carrega a lista de filmes do arquivo JSON.
    # Retorna uma lista de dicionários (cada um é um filme).
    # Se o arquivo não existir, retorna uma lista vazia.
    def carregar_filmes(self):
        # Nome fixo do arquivo JSON (salvo no diretório atual do script).
        arquivo_json = 'filmes.json'
        if os.path.exists(arquivo_json):
            # Abre o arquivo em modo leitura com encoding UTF-8 (suporte a acentos).
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                # Converte o JSON em uma lista Python de dicionários.
                return json.load(f)
        # Fallback: Lista vazia se o arquivo não existir ou estiver corrompido.
        return []
    
    # Função auxiliar: Salva a lista de filmes no arquivo JSON.
    # Parâmetro: filmes (lista de dicionários com dados dos filmes).
    # Sobrescreve o arquivo existente (ou cria se não existir).
    def salvar_filmes(self, filmes):
        # Abre o arquivo em modo escrita com encoding UTF-8.
        with open('filmes.json', 'w', encoding='utf-8') as f:
            # Salva a lista como JSON, com indentação para legibilidade e suporte a caracteres não-ASCII (ex: acentos).
            json.dump(filmes, f, ensure_ascii=False, indent=4)
    
    # Método sobrescrito: Lida com requisições HTTP GET (ex: carregar páginas ou recursos).
    # Analisa o path da URL e responde de acordo com a rota.
    def do_GET(self):
        # Extrair o path limpo (sem query params)
        # Usa urlparse para obter apenas o caminho da URL (ex: '/rota' sem '?id=1').
        parsed_path = urlparse(self.path).path
        
        # Bloco de rotas para servir páginas HTML estáticas.
        
        # Rota para página de login: Serve o arquivo 'login.html' estaticamente.
        # caminho para Login
        if parsed_path == '/2_Semestre/BackEnd/Aulas/WS/login':
            try:
                # Constrói o caminho absoluto para o arquivo (assumindo estrutura de pastas fixa).
                caminho_arquivo = os.path.join(os.getcwd(), '2_Semestre', 'BackEnd', 'Aulas', 'WS', 'login.html')
                # Abre e lê o conteúdo do arquivo.
                with open(caminho_arquivo, encoding='utf-8') as login:
                    content = login.read()
                
                # Envia o conteúdo como resposta HTTP 200.
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                # Se o arquivo não existir, envia erro 404.
                self.send_error(404, "File Not Found!!!!")
                
        # Rota para página de cadastro genérico: Serve 'cadastro.html' (mantido do código original).
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/cadastro':
            # cadastro genérico (mantido como no seu código)
            try:
                caminho_arquivo = os.path.join(os.getcwd(), '2_Semestre', 'BackEnd', 'Aulas', 'WS', 'cadastro.html')
                with open(caminho_arquivo, encoding='utf-8') as cadastro:
                    content = cadastro.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                
        # Rota para formulário de cadastro de filmes: Serve 'cadastro_filmes.html' estaticamente.
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes':
            # cadastro de filmes
            try:
                caminho_arquivo = os.path.join(os.getcwd(), '2_Semestre', 'BackEnd', 'Aulas', 'WS', 'cadastro_filmes.html')
                with open(caminho_arquivo, encoding='utf-8') as cadastro_filmes:
                    content = cadastro_filmes.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                
        # Rota para listar filmes: GERA HTML a partir do JSON (não serve arquivo estático).
        # Carrega os filmes, constrói uma tabela e envia como resposta.
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/listar_filmes':
            with open("./2_Semestre/BackEnd/Aulas/WS/listar_filmes.html", 'w', encoding='utf-8') as h:
                # listar filmes - DINÂMICO: Gera HTML a partir do JSON
                # Carrega a lista de filmes existentes.
                filmes = self.carregar_filmes()

                # Inicia a construção do HTML com DOCTYPE, head e estilos CSS inline (para tabela simples).
                html = """
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Lista de Filmes</title>
                    <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <header>
                        <nav>
                            <ul>
                                <li><a href="./index.html">HOME</a></li>
                                <li><a href="./listar_filmes.html">FILMES</a></li>
                                <li><a href="./cadastro_filmes.html"></a>CADASTRO DE FILMES</li>
                            </ul>
                        </nav>
                    </header>
                    <div class="fitaFilme">
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                        <div class="framesFilme"></div>
                    </div>
                    <h1>Lista de Filmes Cadastrados</h1>
                """

                # Verifica se há filmes; se não, adiciona mensagem.
                if not filmes:
                    html += "<p>Nenhum filme cadastrado ainda.</p>"
                else:
                    # Inicia a tabela com cabeçalhos (sem coluna de poster nesta versão básica).
                    html += "<table>\n<thead><tr><th>Nome</th><th>Atores</th><th>Diretor</th><th>Ano</th><th>Gênero</th><th>Produtora</th><th>Sinopse</th></tr></thead>\n<tbody>"
                    # Itera sobre cada filme e adiciona uma linha <tr>.
                    for filme in filmes:
                        html += f"""
                        <tr>
                            <td>{filme.get('nome_filme', 'N/A')}</td>
                            <td>{filme.get('atores', 'N/A')}</td>
                            <td>{filme.get('diretor', 'N/A')}</td>
                            <td>{filme.get('ano', 'N/A')}</td>
                            <td>{filme.get('genero', 'N/A')}</td>
                            <td>{filme.get('produtora', 'N/A')}</td>
                            <td>{filme.get('sinopse', 'N/A')}</td>
                        </tr>
                        """
                    # Fecha a tabela.
                    html += "</tbody></table>"

                # Adiciona link de navegação e fecha o HTML.
                html += """
                    <div class="alinhamento">
                        <buttom class="btnLinks"><a href="/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes">Adicionar Novo Filme</a></buttom>
                        <buttom class="btnLinks"><a href="/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes">Voltar ao Cadastro</a></buttom>
                    </div>
                </body>
                </html>
                """
                h == html

                # Envia o HTML dinâmico gerado como resposta HTTP 200.
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))
                
        # Para qualquer outra rota GET não tratada (ex: arquivos estáticos como CSS ou imagens), usa o handler padrão.
        else:
            super().do_GET()
            
    # Método sobrescrito: Lida com requisições HTTP POST (ex: envio de formulários).
    # Processa dados do form e responde de acordo com a rota.
    def do_POST(self):
        # Extrai o path da URL para identificar a rota.
        parsed_path = urlparse(self.path).path
        
        # Rota para envio de login: Processa form simples (urlencoded, sem arquivos).
        if parsed_path == '/2_Semestre/BackEnd/Aulas/WS/send_login':
            # recebendo a requisição
            # Lê o tamanho do corpo da requisição e o conteúdo.
            content_length = int(self.headers['Content-Length'])  # Corrigi para 'Content-Length'
            body = self.rfile.read(content_length).decode('utf-8')  # rfile é o stream de entrada.
            # Parseia os dados do form como query string.
            form_data = parse_qs(body)
            
            # Extrai campos do form (usa [0] para o primeiro valor, pois parse_qs retorna listas).
            login = form_data.get('email', [""])[0]
            password = form_data.get('password', [""])[0]  # Não forcei int, usei str
            
            # Valida as credenciais e obtém mensagem.
            logou = self.accont_user(login, password)
            
            # Logs no console para depuração (visível no terminal onde o servidor roda).
            print("Data from login:")
            print("Email:", login)
            print("Password:", password)  
            
            # Envia resposta simples (texto/HTML) com o resultado do login.
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode('utf-8'))
            
        # Rota para envio de cadastro de filmes: Processa form e salva no JSON.
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/send_cadastro':
            # Cadastro de filmes - Salva no JSON
            # Lê o corpo da requisição (form urlencoded, sem suporte a arquivos nesta versão).
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            
            # Extrair dados 
            # Extrai cada campo do form, removendo espaços extras com .strip().
            nome_filme = form_data.get('nome_filme', [""])[0].strip()
            atores = form_data.get('atores', [""])[0].strip()
            diretor = form_data.get('diretor', [""])[0].strip()
            ano = form_data.get('ano', [""])[0].strip()
            genero = form_data.get('genero', [""])[0].strip()
            produtora = form_data.get('produtora', [""])[0].strip()
            sinopse = form_data.get('sinopse', [""])[0].strip()
            
            # Validação básica: Nome do filme é obrigatório.
            if not nome_filme:
                self.send_error(400, "Nome do filme é obrigatório!")
                return
            
            # Criar dict do filme
            # Cria um dicionário com os dados extraídos do form.
            novo_filme = {
                'nome_filme': nome_filme,
                'atores': atores,
                'diretor': diretor,
                'ano': ano,
                'genero': genero,
                'produtora': produtora,
                'sinopse': sinopse
            }
            
            # Carregar filmes existentes
            # Carrega a lista atual, adiciona o novo filme e salva.
            filmes = self.carregar_filmes()
            filmes.append(novo_filme)
            self.salvar_filmes(filmes)
            
            # Log do filme cadastrado (para depuração no console).
            print("Novo filme cadastrado:")
            print(novo_filme)
            
            # Resposta: Página de sucesso com redirecionamento para listar
            # Gera um HTML simples de confirmação com meta refresh (redireciona automaticamente em 2s).
            sucesso_html = f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="refresh" content="2;url=/2_Semestre/BackEnd/Aulas/WS/listar_filmes">
                <title>Sucesso!</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <div class="fitaFilme">
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                    <div class="framesFilme"></div>
                </div>
                <h1>Filme '{nome_filme}' cadastrado com sucesso!</h1>
                <p>Redirecionando para a lista de filmes...</p>
                <a class="links" href="/2_Semestre/BackEnd/Aulas/WS/listar_filmes">Ir para Lista</a>
            </body>
            </html>
            """
            
            # Envia o HTML de sucesso como resposta HTTP 200.
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(sucesso_html.encode('utf-8'))
            
        # Para qualquer outra rota POST não tratada, mostra um erro.
        else:
            super(MyHandle, self).do_POST()

# Função principal: Configura e inicia o servidor HTTP.
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    
    print("Server Runing in http://localhost:8000/2_Semestre/BackEnd/Aulas/WS/")
    
    httpd.serve_forever()
    
main()