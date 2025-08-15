# POO
# modelar entidades do mundo real como objetos e explora as interações
# entre eles para resolver problemas de forma eficiente e organizada

# entidades são as Classes e os objetos são instancia
"""
Class Nome:
    def // metodos
"""

import random

# exer 1
class Veiculo:
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo):
        self.marca = marca                 
        self.ano_fab = ano_fab
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.modelo = modelo
    
    def andar(self):
        print(f"{self.modelo} estou andando")
    
    def parar(self):
        print(f"{self.modelo} estou parando")

    def imprimir(self):
        print(
            "O Veículo tem as características: \n" \
            f"Marca: {self.marca}\n" \
            f"Ano de fabricação: {self.ano_fab}\n" \
            f"Cor: {self.cor}\n" \
            f"Quantidades de portas: {self.qtd_portas}\n" \
            f"Modelo: {self.modelo}"          
        )

    


# carro
class Carro(Veiculo):
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, qtd_rodas):
        super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
        self.qtd_rodas = qtd_rodas

    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de Rodas: {self.qtd_rodas}\n")

    def seta(self):
        talvez = random.random()

        if talvez == 0:
            print("Você deu seta!\nEvitou um acidente e xingamento :)")
        else:
            print("Você não deu a seta.\nVocê bateu o carro, parabens :)")


# moto
class Moto(Veiculo):
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, qtd_rodas, qtd_farol):
        super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
        self.qtd_rodas = qtd_rodas
        self.qtd_farol = qtd_farol

    def imprimir(self):
        super().imprimir()
        print(f"Quantidades de Rodas: {self.qtd_rodas}")
        print(f"Quantidade de Farois: {self.qtd_farol}\n")

    def grau(self):
        i = random.random()

        if i == 0:
            print("Dar Grau!")
            print("HAAAANDAAAADAAA")
        else:
            print("Não dar Grau!")
            print("Você passou pelo radar :)")


# caminhão
class Caminhao(Veiculo):
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, cargas, tipo):
        super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
        self.cargas = cargas
        self.tipo = tipo

    def imprimir(self):
        super().imprimir()
        print(f"Peso da Carga: {self.cargas}Kg")
        print(f"Tipo da Cargas: {self.tipo}\n")

    def barulho(self):
        contador = 0
        while contador <= 3:
            print("HAAAAAAAAAAA TUUUUUUU")
            contador += 1

def main():
    carro1 = Veiculo("Toyota", 2008, "Azul", 4, "Corolla")
    carro1.imprimir()
    carro2 = Carro("Toyota", 2008, "Azul", 4, "Corolla", 4)
    carro2.imprimir()

    moto1 = Moto("Yamada", 2020, "Preto", 0, "234k", 2, 2)
    moto1.imprimir()

    caminhao1 = Caminhao("Honda", 2005, "Vermelho", 4, "208m", 240, "Alimentos")
    caminhao1.imprimir()

main()
