"""
class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.escolaridade = 'Superior Incompleto'

    def apresentar(self): #Apresentação da pessoa
        print(f"Olá. Meu nome é {self.nome} e tenho {self.idade} anos.")

    def __str__(self): #Converter em string de maneira certa
        return f'{self.nome} - {self.idade}'

    def __eq__(self, other): #Verificar se os dois são iguais.
        if isinstance(other, Pessoa): #pessoa1 == Pessoa
            if self.nome == other.nome and self.idade == other.idade and self.cpf == other.cpf and self.rg == other.rg:
                return True
            return False
"""
#def __lt__(self, other): #Se há algo de um menor que o outro    
# def __le__(self, other): #Se há algo de um menor ou igual que o outro    
# def __gt__(self, other): #Se há algo de um maior que o outro    
# def __ge__(self, other): #Se há algo de um maior ou igual que o outro    
# def __len__(self): # Definir o tamanho da classe        
# return self.idade#isinstance = Verificar se o objeto (variável) é algo.pessoa1 = Pessoa(nome="Yasmin", idade=19, cpf="123456789", rg="25487432")pessoa1.apresentar()print(pessoa1)class Funcionario(Pessoa): 
# 
# #Herança    
# def __init__(self, nome, idade, cpf, rg, cargo):        
#   super().__init__(nome, idade, cpf, rg) #Puxar as informações da classe mãe        
#   self.cargo = cargo    
# def trabalhar(self):        
#   print("Trabalhando...")    
# def apresentar(self):        
#   print(f"Olá. Meu nome é {self.nome} e trabalho como {self.cargo}.")funcionario = Funcionario(nome="Solange", idade=50, cpf="987654321", rg="153687667", cargo="Estilista")funcionario.apresentar()
#   print(isinstance(funcionario, Pessoa)) #Verificando se o funcionáro é pessoa.#Polimorfismo = Mesma função, porém de maneiras e para coisas diferentes

# Abistração e encapsulamento

# 1 - criar a classe Produto com os atributos:
# - nome
# - preco -> privado

# 2 - implemente um metodo para exibir_dados(), que imprime o nome e o preco

# 3 - crie os getter e setter do preço

# 4 - criar a classe Carrinho com:
# - atributo itens (lista, inicialmente vazia)

# 5 - Método da classe Carrinho:
# - adicionar(produto) - recebe um Produto e o adiciona a lista itens
# - remover(produto) - remove o produto da lista itens
# - total() - RETORNA a soma dos preco dos produtos no carrinho
# - listar_itens() - imprime todos os produtos com seu preço