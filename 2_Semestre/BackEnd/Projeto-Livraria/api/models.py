from django.db import models # caixa preta

# criando as tabelas do banco de dados, com classes
# make migrations -> cria um doc na pasta migrations com as alterações feitas no models.py
# a cada nova alteração cria um novo doc
# migrate -> aplica as alterações no banco de dados

# conceito "firts code"

class Autor(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nacionality = models.CharField(max_length=30, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(null=True, blank=True)
    site = models.CharField(null=True, blank=True)
    # blank - o campo pode ser vazio
    
    def __str__(self):
        return self.editora
    
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    subTitulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50)
    idioma = models.CharField(default='Portugues')
    descricao = models.TextField()
    paginas = models.IntegerField()
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.titulo
    
    
    
