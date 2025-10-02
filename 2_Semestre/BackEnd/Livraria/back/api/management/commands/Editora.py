import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Editora

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/editora.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]
        
        if o["truncate"]:Editora.objects.all().delete() # apaga tudo
        
        df['editora'] = df['editora'].astype(str).str.strip()
        df['cnpj'] = df['cnpj'].astype(str).str.strip()
        df['endereco'] = df['endereco'].astype(str).str.strip()
        df['telefone'] = df['telefone'].astype(str).str.strip()
        df['email'] = df['email'].astype(str).str.strip()
        df['site'] = df['site'].astype(str).str.strip()
        
        # apagar todos que não tem nome e sobrenome
        df = df.query('editora != "" and cnpj != "" ') # query - consulta
        
        # se não tiver data de nascimento, não entra
        df = df.dropna(subset=['site']) 
        
        if o["update"]:
            criados = atualizados = 0
            
            for r in df.itertuples(index=False): # itertuples - cada linha é uma tuplas
                _, created = Editora.objects.update_or_create(
                    editora = r.editora, cnpj = r.cnpj, endereco = r.endereco, # r = for no df
                    telefone = r.telefone, email = r.email, site = r.site
                )
                
                criados += int(created)
                atualizados += (not created)
            self.stdout.write(self.style.SUCCESS(f'Criados:{criados}  | Atualizados: {atualizados}')) # igual ao print
        else:
            objs = [Editora(
                editora = r.editora, cnpj = r.cnpj, endereco = r.endereco, telefone = r.telefone, email = r.email, site = r.site
            ) for r in df.itertuples(index=False)]
            
            Editora.objects.bulk_create(objs, ignore_conflicts=True)
            
            self.stdout.write(self.style.SUCCESS(f'Criados:{len(objs)}'))