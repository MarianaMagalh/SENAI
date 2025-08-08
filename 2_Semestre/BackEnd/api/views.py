from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autor
from .serializers import AutorSerializers

# fazendo a view para listar e criar autores
# fazendo tudo, em html e criando o GET e POST
class AutoresView(ListCreateAPIView):
   queryset = Autor.objects.all()
   serializer_class = AutorSerializers
    
