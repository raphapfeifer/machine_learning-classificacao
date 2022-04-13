
import pandas as pd
df = pd.read_csv('buscas.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

Xdummies_df = pd.get_dummies(x_df)
Ydummies_df = y_df

x = Xdummies_df.values
y = Ydummies_df.values

porcentagem_de_treino = 0.9
tamanho_de_treino = int(porcentagem_de_treino * len(y))
tamanho_de_teste = len(y) - tamanho_de_treino

treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]

teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acertos)
print(total_de_elementos)





