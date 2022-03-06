from pandas_datareader import data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

acao = input('Qual ação você deseja ver o gráfico?').upper()

dia_ini = int(input('Qual é o dia de inicio?'))
mes_ini = int(input('Qual é o mês de inicio?'))
ano_ini = int(input('Ano de inicio:'))
dia_fim = int(input('Dia do fim da análise:'))
mes_fim = int(input('Mês fim da análise:'))
ano_fim = int(input('Ano de fim:'))

banco_cot = web.DataReader(f'{acao}.SA',data_source='yahoo',start=f'{mes_ini}-{dia_ini}-{ano_ini}',end=f'{mes_fim}-{dia_fim}-{ano_fim}')

media = np.mean(banco_cot['Adj Close'])
maxi = np.max(banco_cot['Adj Close'])
mini = np.min(banco_cot['Adj Close'])


plt.figure(figsize=(15,10))
plt.xlabel('Data')
plt.ylabel('Valor')
plt.title(f'Gráfico da ação {acao} do periodo de {dia_ini}/{mes_ini}/{ano_ini} a de {dia_fim}/{mes_fim}/{ano_fim}, a média foi {media:.2f}, máximo de {maxi:.2f} e minimo de {mini:.2f}')
sns.lineplot(x='Date',y='Adj Close',data=banco_cot)
plt.show()