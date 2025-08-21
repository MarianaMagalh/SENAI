from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Editora, Livro
from .serializers import AutorSerializers, EditoraSerializer, LivrosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# fazendo a view para listar e criar autores
# fazendo tudo, em html e criando o GET e POST
@api_view(['GET', 'POST'])
def visualizacao_autor(request):
   if request.method == 'GET':
      queryset = Autor.objects.all()
      serializer = AutorSerializers(queryset, many = True)
      return Response(serializer.data)
   elif request.method == 'POST': 
      serializer = AutorSerializers(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
   else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# AUTORES
# GET E POST - ListCreateAPIView
class AutoresView(ListCreateAPIView):
   queryset = Autor.objects.all()
   serializer_class = AutorSerializers
   
# DELETE - RetrieveUpdateDestroyAPIView
class AutoresDetailView(RetrieveUpdateDestroyAPIView):
   queryset = Autor.objects.all()
   serializer_class = AutorSerializers
   
# EDITORAS
class EditorasView(ListCreateAPIView):
   queryset = Editora.objects.all()
   serializer_class = EditoraSerializer
   
class EditorasDetailView(RetrieveUpdateDestroyAPIView):
   queryset = Editora.objects.all()
   serializer_class = EditoraSerializer
   
# LIVROS
class LivrosView(ListCreateAPIView):
   queryset = Livro.objects.all()
   serializer_class = LivrosSerializer
   
class LivroDetailView(RetrieveUpdateDestroyAPIView):
   queryset = Livro.objects.all()
   serializer_class = LivrosSerializer