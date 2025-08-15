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
    
