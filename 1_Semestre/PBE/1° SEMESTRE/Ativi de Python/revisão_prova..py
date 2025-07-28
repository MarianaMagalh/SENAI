"""
class Livro:
    def __init__(self, autor, titulo, n_pag, genero):
        self.titulo = titulo
        self.autor = autor
        self.n_pag = n_pag
        self.genero = genero

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

meu_livro = Livro("Ali Hazelwood", "Hipotese do Amor", 360, "Romance")

print(meu_livro.get_titulo())

meu_livro.set_titulo("Amor, Teoricamente")
print(meu_livro.get_titulo())
"""

class Tv:
    def __init__(self, volume, canal, vol_min, vol_max, canal_min, canal_max, ligada):
        self.volume = volume
        self.canal = canal
        


