import pandas as pd
import numpy as np

df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv')

df.to_excel('LOPAL-ProjetoIntegrador.xlsx', sheet_name='Teste', header=True)