import random


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

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade/100)       

    def getHumor(self):
        return 100 - ((self.fome * self.tedio)/2)

    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)):
            self.saude -= 10
        elif ((self.fome > 60 and self.fome <= 80)) or ((self.tedio > 60 and self.tedio <= 80)):
            self.saude -= 30
        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 90)):
            self.saude -= 50
        elif ((self.fome > 90)) or ((self.tedio > 90)):
            print("Estou morrendo, cuide de mim por favor!!")
        elif ((self.fome > 99)) or ((self.tedio > 99)):
            self.saude = 0
            print("O seu bichinho morreu.")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5


class Universo(Tamagoshi):
    def __init__(self, nome, cor, fundo, alimento, diversao):
        super().__init__(nome)
        self.cor = cor
        self.fundo = fundo 
        self.alimento = alimento 
        self.diversao = diversao

    def tipoAlimento(self):
        alimentos = ["materia Escura", "antimateria", "planetas e estrelas"]

        if alimentos == alimentos:
            super().alimentar()
        else:
            print("Eu não como esse tipo de coisa")

    def divertido(self):
        # colocar tempo para ele falar isso
        print("Gira, gira, gira\n" \
        "Vamos todos girará\n" \
        "Vamos dá meia-volta, volta-meia vamos dá\n" \
        ":)")

    def mudaCor(self):
        self.humor = ["feliz", "triste"]

        if self.humor == "feliz":
            print("Azul")
        elif self.humor == "triste":
            print("Jupter")
        else:   
            print("Branco")


class Arte(Tamagoshi):
    def __init__(self, nome, pintura, alimento, frases):
        super().__init__(nome)
        self.pintura = pintura
        self. alimento = alimento 
        self.frase = frases

    def citacao(self):
        self.frase = [
            "A arte é a mentira que nos permite conhecer a verdade. - Pablo Picasso.",
            "A arte não reproduz o que vemos. Ela nos faz ver. - Paul Klee.",
            "A arte nos permite encontrar a nós mesmos e nos perder ao mesmo tempo. - Thomas Merton.",
            "O alvo da minha pintura é o sentimento."
        ]

        mostra = random.random(self.frase)
        print(mostra)

    def comer(self):
        self.alimento = ["tinta aquarela", "pinceis", "telas"]

        if self.alimentos == self. alimentos:
            super().alimentar()
        else:
            print("Perdo-me, mas eu não como isso")


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





    