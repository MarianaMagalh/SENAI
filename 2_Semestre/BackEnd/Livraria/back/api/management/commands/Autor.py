import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Autor

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]
        
        if o["truncate"]:Autor.objects.all().delete()
        
        df['name'] = df['name'].astype(str).str.strip()
        df['last_name'] = df['last_name'].astype(str).str.strip()
        df['birth_date'] = pd.to_datetime(df['birth_date'], errors="coerce", format="%Y-%m-%d").dt.date
        df['nacionality'] = df.get('nacionality', '').astype(str).str.strip().str.capitalize().replace({"": None})
        
        # apagar todos que não tem nome e sobrenome
        df = df.query('name != "" and last_name != "" ') # query - consulta
        
        # se não tiver data de nascimento, não entra
        df = df.dropna(subset=['birth_date']) 
        
        if o["update"]:
            criados = atualizados = 0
            
            for r in df.itertuples(index=False): # itertuples - cada linha é uma tuplas
                _, created = Autor.objects.update_or_create(
                    name = r.name, last_name = r.last_name, birth_date = r.birth_date,
                    defaults={'nacionality': r.nacionality}
                )
                
                criados += int(created)
                atualizados += (not created)
            self.stdout.write(self.style.SUCCESS(f'Criados:{criados}  | Atualizados: {atualizados}'))
        else:
            objs = [Autor(
                name = r.name, last_name = r.last_name, birth_date = r.birth_date, nacionality = r.nacionality
            ) for r in df.itertuples(index=False)]
            
            Autor.objects.bulk_create(objs, ignore_conflicts=True)
            
            self.stdout.write(self.style.SUCCESS(f'Criados:{len(objs)}'))