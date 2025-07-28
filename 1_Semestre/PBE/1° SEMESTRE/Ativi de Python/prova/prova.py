# PROVA DE ORIENTAÇÃO A OBJETOS
# 1° EXERCICIO
class Produto:
    def __init__(self, estoque, nome_produ, qtd_disponivel, preco_unitario):
        self.estoque = estoque
        self.nome_produ = nome_produ
        self.qtd_disponivel = qtd_disponivel
        self.preco_unitario = preco_unitario

    def adicionar_qtd(self, valor):
        estoque_disponivel = []
        estoque_disponivel.append(valor)
        
    def remover_quantidade(self, valor):
        if self.estoque < 0:
            raise Exception("O valor informado é negativo.")
        else:
            estoque_disponivel = []
            estoque_disponivel.pop(valor)
    
    def calcular_valor_total(self):
        total = self.estoque * self.preco_unitario
        return total



# 2° EXERCICIO
class VeiculoTransporte:
    def __init__(self, capacidade_p, placa, custo):
        self.capacidade_p = capacidade_p
        self.placa = placa
        self.custo = custo

    def capacidade_passageiros(self, capacidade_p):
        passageiros = []
        pessoa = capacidade_p
        pessoa.append(passageiros)

    def calcular_custo(self, distancia):
        custo_total = distancia * (self.custo/1000)
        return custo_total
    

class Onibus(VeiculoTransporte):
    def __init__(self, capacidade_p, placa, custo):
        super().__init__(capacidade_p, placa, custo)

    def capacidade_passageiros(self, capacidade_p):
        super().capacidade_passageiros(capacidade_p)
    

    def calcular_custo(self, distancia, capacidade):
        if capacidade >= (80/100):
            custo_total = distancia * (self.custo/1000)
            acrescimo = custo_total + (15/100)
            return acrescimo
    

class MicroOnibus(VeiculoTransporte):
    def __init__(self, capacidade_p, placa, custo):
        super().__init__(capacidade_p, placa, custo)

    def calcular_custo(self, distancia, capacidade):
        if capacidade >= (70/100):
            custo_total = distancia * (self.custo/1000)
            acrescimo = custo_total + (10/100)
            return acrescimo
        

class Van(VeiculoTransporte):
    def __init__(self, capacidade_p, placa, custo):
        super().__init__(capacidade_p, placa, custo)
    
    def calcular_custo(self, distancia, capacidade):
        if capacidade >= (60/100):
            custo_total = distancia * (self.custo/1000)
            acrescimo = custo_total + (5/100)
            return acrescimo
