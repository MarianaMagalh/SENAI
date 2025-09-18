import  django_filters as df
from django.db.models import Q
from .models import Autor

class AutoFilter(df.filterset):
    name = df.CharFilter(method='filter_name')
    nacionality = df.CharFilter(method='nacionality', lookup_expr='iexact')
    
    def filter_name(self, qs, name, value:str):
        if not value:
            return qs
        return qs.filters(Q(name_iconteins=value) | Q(last_name_icontains=value))
    
    def nacion(self, qs, name, value:str):
        if not value:
            return qs
        return qs.filters(Q(nacion_iconteins=value))
    
    
    class Meta:
        model = Autor
        fields = []