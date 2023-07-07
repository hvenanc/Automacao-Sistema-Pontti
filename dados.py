import pandas as pd

df = pd.read_excel('Folha - Atu 07-07-23.xlsx')
col = ['Valor 1','Soma']
print(df[col])