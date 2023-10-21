import pandas as pd

#Extract
df = pd.read_csv('clientes.csv',sep=';')
#print(df)

#Transform
saldos_negativos = df[df['Saldo'] < '0']
dados_saldos_negativos = saldos_negativos[['Nome', 'Saldo']]

print(dados_saldos_negativos)

#Load
dados_saldos_negativos.to_csv('saldos_negativos.csv', index=False)