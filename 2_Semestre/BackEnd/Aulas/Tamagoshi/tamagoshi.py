class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0 
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.historico = []
        self.energia = 100  
        self.felicidade = 100  

    def alimentar(self, quantidade):
        try:
            quantidade = int(quantidade)
            if 0 <= quantidade <= 100:
                self.fome = max(0, self.fome - quantidade)
                self.historico.append(f"{self.nome} foi alimentado.")
                print(f"{self.nome} comeu e agora está com {self.fome} de fome.")
            else:
                print("Quantidade inválida para alimentar.")
        except ValueError:
            print("Por favor, digite um número válido.")

    def brincar(self):
        if self.energia > 10:
            self.felicidade = min(100, self.felicidade + 20)
            self.energia -= 10
            self.tedio = max(0, self.tedio - 15)  
            self.historico.append(f"{self.nome} brincou e está feliz.")
            print(f"{self.nome} brincou!\nFelicidade: {self.felicidade}, Energia: {self.energia}")
        else:
            print(f"{self.nome} está cansado demais para brincar!")
            
    def get_humor(self):
        humor = (self.felicidade + self.energia) - (self.fome + self.tedio) / 2
        return max(min(humor, 100), 0)

    def vida(self):
        if self.saude > 0:
            if 50 < self.fome <= 60 or 50 < self.tedio <= 60: 
                self.saude -= 10
            elif 60 < self.fome <= 80 or 60 < self.tedio <= 80:
                self.saude -= 30
            elif 80 < self.fome <= 90 or 80 < self.tedio <= 90:
                self.saude -= 50
            elif self.fome > 90 or self.tedio > 90:
                print(f"{self.nome}: Estou morrendo, cuide de mim por favor!!")
            if self.fome >= 100 or self.tedio >= 100:
                self.saude = 0
                print(f"O seu bichinho {self.nome} morreu.")

    def passar_tempo(self):
        self.vida()
        self.idade += 1
        self.tedio += 2
        self.fome += 5
        self.felicidade = max(0, self.felicidade - 2)

        if self.tedio > 100: self.tedio = 100  
        if self.fome > 100: self.fome = 100 

    def dormir(self):
        self.energia = 100
        self.historico.append(f"{self.nome} foi dormir.")
        print(f"{self.nome} dormiu e recuperou a energia!")

    def mostrar_status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"Fome: {self.fome} | Idade: {self.idade} |Felicidade: {self.felicidade} | Energia: {self.energia} | Saúde: {self.saude} | Humor: {self.get_humor()} | Tedio: {self.tedio}")

    def mostrar_historico(self):
        print("\nHistórico de atividades:")
        for evento in self.historico:
            print("-", evento)


class Dragao(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.fogo = 100

    def cuspir_fogo(self):
        if self.energia > 20 and self.fogo > 0:
            self.fogo -= 10
            self.energia -= 20
            self.historico.append(f"{self.nome} cuspiu fogo!")
            print(f"{self.nome} soltou fogo!\nFogo restante: {self.fogo}")
        else:
            print(f"{self.nome} está cansado demais ou sem fogo para soltar chamas!")
            
    def rugir(self):
        if self.energia > 10:
            self.energia -= 10
            self.felicidade = min(100, self.felicidade + 10)
            self.historico.append(f"{self.nome} rugiu ferozmente!")
            print(f"{self.nome} rugiu!\nEnergia: {self.energia}, Felicidade: {self.felicidade}")
        else:
            print(f"{self.nome} está muito cansado para rugir!")

    def voar_alto(self):
        if self.energia > 25:
            self.energia -= 25
            self.fogo -= 5
            self.felicidade = min(100, self.felicidade + 20)
            self.historico.append(f"{self.nome} voou alto nos céus!")
            print(f"{self.nome} voou alto!\nEnergia: {self.energia}, Fogo: {self.fogo}")
        else:
            print(f"{self.nome} não tem energia suficiente para voar!")
            
            

class Hipogrifo(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.respeito = 50  
        
        if self.respeito <= 20:
            self.felicidade -= 50
            self.saude -= 20

    def voar(self):
        if self.energia > 30:
            self.energia -= 30
            self.felicidade = min(100, self.felicidade + 25)
            self.respeito += 10
            self.historico.append(f"{self.nome} voou majestosamente!")
            print(f"{self.nome} voou pelos céus! Respeito: {self.respeito}, Energia: {self.energia}")
        else:
            print(f"{self.nome} não tem energia suficiente para voar.")

    def planar(self):
        if self.energia > 15:
            self.energia -= 15
            self.felicidade = min(100, self.felicidade + 10)
            self.historico.append(f"{self.nome} planou suavemente pelo ar.")
            print(f"{self.nome} planou!\nEnergia: {self.energia}, Felicidade: {self.felicidade}")
        else:
            print(f"{self.nome} está sem energia para planar.")

    def gritar(self):
        if self.energia > 10:
            self.energia -= 10
            self.respeito += 5
            self.historico.append(f"{self.nome} soltou um grito poderoso!")
            print(f"{self.nome} gritou!\nRespeito: {self.respeito}, Energia: {self.energia}")
        else:
            print(f"{self.nome} está muito cansado para gritar!")



class Camaleao(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.camuflagem = 100  

    def camuflar(self):
        if self.camuflagem > 0:
            self.camuflagem -= 20
            self.felicidade = min(100, self.felicidade + 15)
            self.historico.append(f"{self.nome} se camuflou e ficou protegido.")
            print(f"{self.nome} se camuflou!\nCamuflagem restante: {self.camuflagem}")
        else:
            print(f"{self.nome} está sem energia para se camuflar!")
            
    def se_esconder(self):
        if self.energia > 10 and self.camuflagem > 20:
            self.energia -= 10
            self.camuflagem -= 20
            self.historico.append(f"{self.nome} se escondeu habilmente.")
            print(f"{self.nome} se escondeu!\nEnergia: {self.energia}, Camuflagem: {self.camuflagem}")
        else:
            print(f"{self.nome} não pode se esconder agora!")

    def relaxar(self):
        self.energia = min(100, self.energia + 25)
        self.camuflagem = min(100, self.camuflagem + 15)
        self.historico.append(f"{self.nome} relaxou e recuperou energia e camuflagem.")
        print(f"{self.nome} relaxou!\nEnergia: {self.energia}, Camuflagem: {self.camuflagem}")

