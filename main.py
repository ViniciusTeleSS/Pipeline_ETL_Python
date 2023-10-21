import pandas as pd

#Extract
df = pd.read_csv('clientes.csv',sep=';')

#Transform
saldos_negativos = df[df['Saldo'] < '0']
dados_saldos_negativos = saldos_negativos[['Nome', 'Saldo']]

#Load
dados_saldos_negativos.to_csv('clientes inadimplentes.csv', index=False)