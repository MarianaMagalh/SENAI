class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100 
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)
            if self.fome < 0:
                self.fome = 0

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade/100)  
            if self.tedio < 0

    def getHumor(self):
        humor = 100 - ((self.fome * self.tedio) / 2)
        return max(humor, 0)

    def vida(self):
        if self.saude > 0:
            if 50 < self.fome <= 60 or 50 < self.tedio <= 60: 
                self.saude -= 10
            elif 60 < self.fome <= 80 or 60 < self.tedio <= 80:
                self.saude -= 30
            elif 80 < self.fome <= 90 or 80 < self.tedio <= 90:
                self.saude -= 50
            elif self.fome > 90 or self.tedio > 90:
                print("Estou morrendo, cuide de mim por favor!!")
            if self.fome > 99 or self.tedio > 99:
                self.saude = 0
                print("O seu bichinho morreu.")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5

        if self.tedio > 100:
            self.tedio = 100  
        if self.fome > 100:
            self.fome = 100 

"""
Parte 1:
Usando a classe Tamagoshi.py criada em sala, desenvolva pelo menos 3 classes
filhas que deem características diferentes para seus bichinhos virtuais. Pense
nessas classes como raça/tipo/características deles.
• Você tem que adicionar novas variáveis/atributos em todas as raças
• E, pelo menos, 3 novos métodos.

Parte 2:
Crie um documento que será o seu programa, e nele terá sua função main( ).
• Nessa função, lembre que seu usuário irá rodar o programa como um jogo,
então ele tem que continuar sendo executado até o usuário querer sair.
• Dê instruções claras e feedbacks para o seu usuário
• Use o método pai, passagemTempo( ), para garantir que o jogo tenha uma
sensação de tempo passando e de consequências próprias.

Desafio:
Mantenha um histórico do bichinho do usuário, em que quando ele saia o
bichinho vá dormir, e quando ele volte ele acorde.

Fazer:
- os tipos de tamagoshi (3)
    -> cor
    -> fundo
    -> tipo de alimento
    -> diversão

- metodo de dormir quando o user sair, e quando voltar ele acordar
    
- menu
    -> com opções de escolher o tipo de tamagoshi e mercado

- mercado
    -> poder comprar comida

- criar a interface **
"""





    