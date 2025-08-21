from django.urls import path # Importa a função 'path' para definir rotas da aplicação
from .views import * # Importa todo o conteúdo do arquivo 'views.py' // Puxa o 'AutoresView'
from .views import visualizacao_autor, AutoresView, EditorasView, LivrosView

urlpatterns = [
    # Cria a rota '/autores' e quando o usuário acessar, a view 'AutoresView' será chamada
    # '.as_view()' = Transforma a classe em uma função que o Django consegue usar
    
    # GET / POST
    path('authors', visualizacao_autor),
    path('autores', AutoresView.as_view()),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),
    
    # UPDATE / DELETE
    path('autores/<int:pk>', AutoresDetailView.as_view()),
    path('editoras/<int:pk>', EditorasDetailView.as_view()),
    path('livros/<int:pk>', LivroDetailView.as_view())
    
]
