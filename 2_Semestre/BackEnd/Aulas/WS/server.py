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
    # Adiciona ID incremental se ausente (para compatibilidade).
    def carregar_filmes(self):
        arquivo_json = 'filmes.json'
        if os.path.exists(arquivo_json):
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                filmes = json.load(f)
                # Adiciona ID se ausente (para JSONs antigos)
                for i, filme in enumerate(filmes):
                    if 'id' not in filme:
                        filme['id'] = i + 1
                return filmes
        return []
    # Função auxiliar: Salva a lista de filmes no arquivo JSON. (Sem mudanças, mas mantida aqui para contexto)
    def salvar_filmes(self, filmes):
        with open('filmes.json', 'w', encoding='utf-8') as f:
            json.dump(filmes, f, ensure_ascii=False, indent=4)
    
    # Método sobrescrito: Lida com requisições HTTP GET (ex: carregar páginas ou recursos).
    # Analisa o path da URL e responde de acordo com a rota.
    def do_GET(self):
        # Extrair o path limpo (sem query params)
        # Usa urlparse para obter apenas o caminho da URL (ex: '/rota' sem '?id=1').
        parsed_path = urlparse(self.path).path
        
        # Rota para página de login: Serve o arquivo 'login.html' estaticamente.
        # caminho para Login
        if parsed_path == '/2_Semestre/BackEnd/Aulas/WS/login':
            try:
                # Constrói o caminho absoluto para o arquivo (assumindo estrutura de pastas fixa). Use sempre '/' para cross-platform.
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
                
        # Rota para listar filmes: CRIA/ATUALIZA ARQUIVO HTML com dados do JSON, então serve o arquivo.
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/listar_filmes':
            # Carrega a lista de filmes existentes do JSON.
            filmes = self.carregar_filmes()

            # Inicia a construção do HTML com DOCTYPE, head e estilos CSS inline (para tabela simples).
            # Baseado no seu template original, mas com tabela dinâmica e correções.
            html = """<!DOCTYPE html>
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
                            <li><a href="/2_Semestre/BackEnd/Aulas/WS/index.html">HOME</a></li>
                            <li><a href="/2_Semestre/BackEnd/Aulas/WS/listar_filmes">FILMES</a></li>
                            <li><a href="/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes">CADASTRO DE FILMES</a></li>
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
                html += "<p>Nenhum filme cadastrado ainda. <a href='/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes'>Cadastrar o primeiro!</a></p>"
            else:
                # Inicia a tabela com cabeçalhos (adiciona coluna "Ações").
                
                html += "<table>\n<thead><tr><th>Nome</th><th>Atores</th><th>Diretor</th><th>Ano</th><th>Gênero</th><th>Produtora</th><th>Sinopse</th><th>Ações</th></tr></thead>\n<tbody>"
                
                # Itera sobre cada filme e adiciona uma linha <tr>.
                for filme in filmes:
                    # Usa .get() para valores padrão se campo ausente, e escapa HTML básico.
                    nome = filme.get('nome_filme', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    atores = filme.get('atores', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    diretor = filme.get('diretor', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    ano = filme.get('ano', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    genero = filme.get('genero', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    produtora = filme.get('produtora', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    sinopse = filme.get('sinopse', 'N/A').replace('<', '&lt;').replace('>', '&gt;')
                    filme_id = filme.get('id', 'N/A')  # ID para os links
                    html += f"""
                    <tr>
                        <td>{nome}</td>
                        <td>{atores}</td>
                        <td>{diretor}</td>
                        <td>{ano}</td>
                        <td>{genero}</td>
                        <td>{produtora}</td>
                        <td>{sinopse}</td>
                        <td>
                            <a class="modLink" href="/2_Semestre/BackEnd/Aulas/WS/editar_filme?id={filme_id}">Editar</a> |
                            <a class="modLink" href="/2_Semestre/BackEnd/Aulas/WS/excluir_filme?id={filme_id}" onclick="return confirm('Tem certeza que deseja excluir este filme?')">Excluir</a>
                        </td>
                    </tr>
                    """
                # Fecha a tabela.
                html += "</tbody></table>"

            # Adiciona link de navegação e fecha o HTML.
            html += """
                    <div class="alinhamento">
                        <a class="btnLinks" href="/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes">Adicionar Novo Filme</a>
                    </div>
                </body>
                </html>"""

            # **CRIA/ATUALIZA O ARQUIVO HTML** (corrigido: escreve o conteúdo no arquivo).
            caminho_html_saida = os.path.join(os.getcwd(), '2_Semestre', 'BackEnd', 'Aulas', 'WS', 'listar_filmes.html')
            with open(caminho_html_saida, 'w', encoding='utf-8') as h:
                h.write(html)  # CORREÇÃO: Escreve o HTML no arquivo (era 'h == html').
            
            print(f"Arquivo HTML criado/atualizado: {caminho_html_saida} (com {len(filmes)} filmes)")

            # Agora, serve o arquivo gerado como resposta HTTP 200 (lê de volta para envio).
            try:
                with open(caminho_html_saida, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))  # COMPLETO: Fecha o write.
            except FileNotFoundError:
                self.send_error(404, "Erro ao ler o arquivo gerado!")
         
        # Rota para editar filme: Gera formulário pré-preenchido baseado no ID.
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/editar_filme':
            # Extrai ID da query string
            query_params = parse_qs(urlparse(self.path).query)
            filme_id = int(query_params.get('id', [0])[0]) if query_params.get('id') else 0

            if filme_id == 0:
                self.send_error(400, "ID do filme não fornecido!")
                return

            # Carrega filmes e busca o específico
            filmes = self.carregar_filmes()
            filme = next((f for f in filmes if f.get('id') == filme_id), None)

            if not filme:
                self.send_error(404, "Filme não encontrado!")
                return

            # Extrai dados para preencher o form (escapa HTML)
            nome = filme.get('nome_filme', '').replace('<', '&lt;').replace('>', '&gt;')
            atores = filme.get('atores', '').replace('<', '&lt;').replace('>', '&gt;')
            diretor = filme.get('diretor', '').replace('<', '&lt;').replace('>', '&gt;')
            ano = filme.get('ano', '')
            genero = filme.get('genero', '').replace('<', '&lt;').replace('>', '&gt;')
            produtora = filme.get('produtora', '').replace('<', '&lt;').replace('>', '&gt;')
            sinopse = filme.get('sinopse', '').replace('<', '&lt;').replace('>', '&gt;')

            # Gera HTML do formulário (similar ao cadastro, mas com values preenchidos e action para POST editar)
            html = f"""<!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Editar Filme</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <header>
                    <nav>
                        <ul>
                            <li><a href="/2_Semestre/BackEnd/Aulas/WS/index.html">HOME</a></li>
                            <li><a href="/2_Semestre/BackEnd/Aulas/WS/listar_filmes">FILMES</a></li>
                            <li><a href="/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes">NOVO CADASTRO</a></li>
                        </ul>
                    </nav>
                </header>
                <h1>Editar Filme: {nome}</h1>
                <form method="POST" action="/2_Semestre/BackEnd/Aulas/WS/editar_filme">
                    <div class="maeOrganizacao">
                        <div id="alinhamento">
                            <input type="hidden" name="id" value="{filme_id}">
                            <label for="nome_filme">Nome do Filme:</label>
                            <input type="text" id="nome_filme" name="nome_filme" value="{nome}" required><br><br>

                            <label for="atores">Atores:</label>
                            <input type="text" id="atores" name="atores" value="{atores}"><br><br>

                            <label for="diretor">Diretor:</label>
                            <input type="text" id="diretor" name="diretor" value="{diretor}"><br><br>

                            <label for="ano">Ano:</label>
                            <input type="number" id="ano" name="ano" value="{ano}"><br><br>

                        </div>
                        <div id="alinhamento">
                            <label for="genero">Gênero:</label>
                            <input type="text" id="genero" name="genero" value="{genero}"><br><br>

                            <label for="produtora">Produtora:</label>
                            <input type="text" id="produtora" name="produtora" value="{produtora}"><br><br>

                            <label for="sinopse">Sinopse:</label>
                            <textarea id="sinopse" name="sinopse" rows="4" cols="50">{sinopse}</textarea><br><br>
                        </div>
                    </div>
                    
                    <input class="btn" type="submit" value="Salvar Alterações">
                    <a class="btn2" href="/2_Semestre/BackEnd/Aulas/WS/listar_filmes">Cancelar e Voltar à Lista</a>
                </form>
            </body>
            </html>"""

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        
        # Rota para excluir filme: Remove baseado no ID e redireciona.
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/excluir_filme':
            # Extrai ID da query string
            query_params = parse_qs(urlparse(self.path).query)
            filme_id = int(query_params.get('id', [0])[0]) if query_params.get('id') else 0

            if filme_id == 0:
                self.send_error(400, "ID do filme não fornecido!")
                return

            # Carrega e remove o filme
            filmes = self.carregar_filmes()
            filmes = [f for f in filmes if f.get('id') != filme_id]
            self.salvar_filmes(filmes)

            # Redireciona para lista (sem body)
            self.send_response(302)
            self.send_header('Location', '/2_Semestre/BackEnd/Aulas/WS/listar_filmes')
            self.end_headers()


                
        # Para qualquer outra rota GET não tratada (ex: arquivos estáticos como CSS ou imagens), usa o handler padrão.
        else:
            print(f"DEBUG GET: Servindo arquivo estático para '{parsed_path}'")  # DEBUG
            super().do_GET()
            
        # Método sobrescrito: Lida com requisições HTTP POST (ex: envio de formulários).
    # Processa dados do form e responde de acordo com a rota.
    def do_POST(self):
        # Extrai o path da URL para identificar a rota.
        parsed_path = urlparse(self.path).path
        print(f"DEBUG POST: Path recebido = '{parsed_path}'")  # DEBUG: Mostra o path no console
        
        # Rota para envio de login: Processa form simples (urlencoded, sem arquivos).
        if parsed_path == '/2_Semestre/BackEnd/Aulas/WS/send_login':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            
            login = form_data.get('email', [""])[0]
            password = form_data.get('password', [""])[0]
            
            logou = self.accont_user(login, password)
            
            print("Data from login:")
            print("Email:", login)
            print("Password:", password)
            print(f"Resultado do login: {logou}")  # DEBUG: Para rastrear no console
            
            if logou == "Usuario Logado":
                # Sucesso: Redireciona para a página inicial (ajuste o URL se necessário)
                self.send_response(302)  # Código HTTP para redirecionamento
                self.send_header('Location', '/2_Semestre/BackEnd/Aulas/WS/index.html')  # Página inicial
                self.end_headers()
                # Não escreve body (não precisa, o browser redireciona automaticamente)
            else:
                # Erro: Envia HTML com mensagem e link para voltar ao login
                erro_html = f"""
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Erro no Login</title>
                    <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <h1>{logou}</h1>
                    <p>Verifique suas credenciais e tente novamente.</p>
                    <a href="/2_Semestre/BackEnd/Aulas/WS/login">Voltar ao Login</a>
                </body>
                </html>
                """
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(erro_html.encode('utf-8'))
        
            
        # Rota para envio de cadastro de filmes
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/send_cadastro':
            print("DEBUG: Entrou no bloco de cadastro de filmes!")  # DEBUG
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            print(f"DEBUG: Dados do form = {form_data}")  # DEBUG: Mostra se names estão corretos

            # Extrair dados (com strip para espaços)
            nome_filme = form_data.get('nome_filme', [""])[0].strip()
            atores = form_data.get('atores', [""])[0].strip()
            diretor = form_data.get('diretor', [""])[0].strip()
            ano = form_data.get('ano', [""])[0].strip()
            genero = form_data.get('genero', [""])[0].strip()
            produtora = form_data.get('produtora', [""])[0].strip()
            sinopse = form_data.get('sinopse', [""])[0].strip()

            # Validação básica
            if not nome_filme:
                print("DEBUG: Erro - Nome do filme vazio!")  # DEBUG
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write("<h1>Erro: Nome do filme é obrigatório!</h1><a href='/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes'>Voltar</a>")
                return

            # Carregar filmes existentes para calcular o próximo ID (movido para cá)
            filmes = self.carregar_filmes()

            # Criar dict do filme
            novo_filme = {
                'nome_filme': nome_filme,
                'atores': atores,
                'diretor': diretor,
                'ano': ano,
                'genero': genero,
                'produtora': produtora,
                'sinopse': sinopse
            }

            # Adicionar ID incremental
            proximo_id = len(filmes) + 1 if filmes else 1
            novo_filme['id'] = proximo_id

            # Salvar no JSON
            filmes.append(novo_filme)
            self.salvar_filmes(filmes)

            print("Novo filme cadastrado:")
            print(novo_filme)

            # HTML de sucesso com redirecionamento
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
                <h1>Filme '{nome_filme}' cadastrado com sucesso!</h1>
                <p>Redirecionando para a lista de filmes...</p>
                <a href="/2_Semestre/BackEnd/Aulas/WS/listar_filmes">Ir para Lista</a>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(sucesso_html.encode('utf-8'))
        
        # Rota para atualizar filme editado
        elif parsed_path == '/2_Semestre/BackEnd/Aulas/WS/editar_filme':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            # Extrai ID e dados (com strip)
            filme_id = int(form_data.get('id', [0])[0]) if form_data.get('id') else 0
            nome_filme = form_data.get('nome_filme', [""])[0].strip()
            atores = form_data.get('atores', [""])[0].strip()
            diretor = form_data.get('diretor', [""])[0].strip()
            ano = form_data.get('ano', [""])[0].strip()
            genero = form_data.get('genero', [""])[0].strip()
            produtora = form_data.get('produtora', [""])[0].strip()
            sinopse = form_data.get('sinopse', [""])[0].strip()

            if filme_id == 0 or not nome_filme:
                self.send_error(400, "ID ou nome do filme inválido!")
                return

            # Carrega e atualiza o filme
            filmes = self.carregar_filmes()
            for filme in filmes:
                if filme.get('id') == filme_id:
                    filme['nome_filme'] = nome_filme
                    filme['atores'] = atores
                    filme['diretor'] = diretor
                    filme['ano'] = ano
                    filme['genero'] = genero
                    filme['produtora'] = produtora
                    filme['sinopse'] = sinopse
                    break
            else:
                self.send_error(404, "Filme não encontrado para edição!")
                return

            self.salvar_filmes(filmes)

            # HTML de sucesso com redirecionamento
            sucesso_html = f"""<!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="refresh" content="2;url=/2_Semestre/BackEnd/Aulas/WS/listar_filmes">
                <title>Sucesso na Edição!</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <h1>Filme '{nome_filme}' atualizado com sucesso!</h1>
                <p>Redirecionando para a lista de filmes...</p>
                <a href="/2_Semestre/BackEnd/Aulas/WS/listar_filmes">Ir para Lista</a>
            </body>
            </html>"""

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(sucesso_html.encode('utf-8'))



# Função principal: Configura e inicia o servidor HTTP.
# Função principal: Configura e inicia o servidor HTTP.
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    
    print("Server Running in http://localhost:8000/2_Semestre/BackEnd/Aulas/WS/")
    print("Teste cadastro: http://localhost:8000/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes")
    print("Teste lista: http://localhost:8000/2_Semestre/BackEnd/Aulas/WS/listar_filmes")
    
    httpd.serve_forever()

if __name__ == "__main__":
    main()