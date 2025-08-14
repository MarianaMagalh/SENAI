from django.urls import path # Importa a função 'path' para definir rotas da aplicação
from .views import * # Importa todo o conteúdo do arquivo 'views.py' // Puxa o 'AutoresView'
from .views import visualizacao_autor

urlpatterns = [
    path('autores', AutoresView.as_view()), #Cria a rota '/autores' e quando o usuário acessar, a view 'AutoresView' será chamada
    # '.as_view()' = Transforma a classe em uma função que o Django consegue usar
    path('authors', visualizacao_autor)
]
