import pandas as pd
df = pd.read_csv('buscas.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

Xdummies_df = pd.get_dummies(x_df)
Ydummies_df = y_df

x = Xdummies_df.values
y = Ydummies_df.values

print(sum(y))
print(len(y))