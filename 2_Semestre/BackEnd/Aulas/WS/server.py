# from http.server import SimpleHTTPRequestHandler, HTTPServer

# # Definição da porta
# port = 8000

# # Definindo o gerenciador/manipulador de requisições
# handler = SimpleHTTPRequestHandler
# # Criando a instancia do servidor
# server = HTTPServer(('localhost', port), handler)
# # Imprimindo uma mensagem de deu certo
# print(f"Server Runing in http://localhost:{port}/2_Semestre/BackEnd/Aulas/WS/")

# server.serve_forever() # faz o server roda infinitamente, ate o terminal fechar

# Proxima Camada
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class MyHandle(SimpleHTTPRequestHandler):
    def list_directory(self, path): # class base
        try:
            # abrindo e lendo o arquivo e mandando a resposta estatica
            f = open(os.path.join(path, 'index.html'), encoding='utf-8') 
            
            self.send_response(200) # resposta para o browser, 'SUCCESS'
            self.send_header("Content-type", "text/html") # enviado as infos do header
            self.end_headers() # fechando o header
            self.wfile.write(f.read().encode('utf-8')) # fluxo de saida do browser, especificação do tipo,
            f.close()
            
            return None 
        except FileNotFoundError: # se não achar o arquivo
            pass
        
        return super().list_directory(path)
    
    def accont_user(self, login, passaword):
        loga = "mariana@gmail.com"
        senha = 1234
        
        if login == loga and senha == passaword:
            return "Usuario Logado"
        else:
            return "Usuario não existe"
    
    def do_GET(self):
        # caminho para Login
        if self.path == '/2_Semestre/BackEnd/Aulas/WS/login':
            try:
                # parecido com um array =>
                with open(os.path.join(os.getcwd(), '2_Semestre\BackEnd\Aulas\WS\login.html'), encoding='utf-8') as login:
                    content = login.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                # tratar o erro
                self.send_error(404, "File Not Found!!!!")
                
        elif self.path == '/2_Semestre/BackEnd/Aulas/WS/cadastro':
            # cadastro
            try:
                with open(os.path.join(os.getcwd(), '2_Semestre\BackEnd\Aulas\WS\cadastro.html'), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                
        elif self.path == '/2_Semestre/BackEnd/Aulas/WS/cadastro_filmes':
            # cadastro de filmes
            try:
                with open(os.path.join(os.getcwd(), '2_Semestre\BackEnd\Aulas\WS\cadastro_filmes.html'), encoding='utf-8') as cadastro_filmes:
                    content = cadastro_filmes.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        elif self.path == '/2_Semestre/BackEnd/Aulas/WS/listar_filmes':
            # listar filmes
            try:
                with open(os.path.join(os.getcwd(), '2_Semestre\BackEnd\Aulas\WS\listar_filmes.html'), encoding='utf-8') as listar_filmes:
                    content = listar_filmes.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                
        else:
            super().do_GET()
            
    def do_POST(self):
        if self.path == '/2_Semestre/BackEnd/Aulas/WS/send_login':
            # recebendo a requisição
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            
            login = form_data.get('email', [""])[0]
            password = int(form_data.get('password', [""])[0])
            
            logou = self.accont_user(login, password)
            
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write("Data Retrieving Sucess!".encode('utf-8'))
        else:
            super(MyHandle, self).do_POST()
    
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    
    print("Server Runing in http://localhost:8000/2_Semestre/BackEnd/Aulas/WS/")
    
    httpd.serve_forever()
    
main()
    