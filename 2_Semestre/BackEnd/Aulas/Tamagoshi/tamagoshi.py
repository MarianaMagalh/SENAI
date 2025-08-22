class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.energia = 100
        self.saude = 100
        self.tedio = 0
        self.historico = []
        self.idade = 1
        
    def alimentar(self, quantidade):
        try:
            quantidade = int(quantidade)
            
            if 0 <= quantidade <= 100:
                self.fome = max(0, self.fome - quantidade)
                self.historico.append(f"{self.nome} foi alimentado.")
                print(f"{self.nome} comeu!\nSua fome é {self.fome}")
            else:
                print("Quantidade inválida para alimentar.")
        except ValueError:
            print("Por favor, digite um número entre 1 á 100.")

    def brincar(self):
        self.energia -= 5
        self.tedio -= 2
        
        self.historico.append(f"{self.nome} bricou!\nSeu tedio é {self.tedio}\nSua energia ficou {self.energia}")
        print(f"{self.nome} brincou muitoo!!")
        
    def vida(self):
        if self.energia >= 5:
            if self.fome > 50 or self.tedio > 50 or self.energia < 50:
                self.saude -= 10
            elif self.fome > 60 or self.tedio > 60 or self.energia < 40:
                self.saude -=20
            elif self.fome > 70 or self.tedio > 70 or self.energia < 30:
                self.saude -= 10
                print(f"Fique atento a saude de {self.nome}!")
            elif self.fome > 80 or self.tedio > 80 or self.energia < 20:
                self.saude -= 20
                print(f"A saude de {self.nome} esta muito baixa cuide delu rapidamente!!")
            elif self.fome > 90 or self.tedio > 90 or self.energia < 10:
                self.saude -= 30
                print("MANO SEU BIXINHO ESTÁ MORRENDO\nCUIDA DELE POR FAVOR\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        else:
            self.energia = 0
            print(f"{self.nome} morreu!")
            print("""
                    ░▒▓███████████████▓▒░  ░▒▓█████████▓▒░ ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                    ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒ ░▒▓█▓▒░ ░▒▓█▓▒░ ▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                    ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒ ░▒▓█▓▒░ ░▒▓█▓▒░ ▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                    ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒ ░▒▓█▓▒░ ░▒▓█▓▒░ ▒▓████████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
                    ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒ ░▒▓█▓▒░ ░▒▓█▓▒░ ▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                    ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒ ░▒▓█▓▒░ ░▒▓█▓▒░ ▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                    ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒  ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░                                                                 
                  """)
            
    def dormir(self):
        self.energia = 100
        self.historico.append(f"{self.nome} foi dormir")
        print(f"{self.nome} dormiu e recuperou a energia!")
            
    def passarTempo(self):
        self.vida()
        self.idade += 1
        self.tedio += 2
        self.fome += 3
        
        if self.tedio > 100: self.tedio = 100  
        if self.fome > 100: self.fome = 100
        
    def mostraStatus(self):
        print(f"\nStatus de {self.nome}:")
        print(f"Fome: {self.fome} | Idade: {self.idade} | Energia: {self.energia} | Saúde: {self.saude} | Tedio: {self.tedio}")

    def mostraHistorico(self):
        print("\nHistórico de atividades:")
        for evento in self.historico:
            print("-", evento)