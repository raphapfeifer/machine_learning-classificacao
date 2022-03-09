from classificacao_web import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

def mostra_dados():

    x, y = carregar_acessos()

    treino_dados = x[:90]
    treino_marcacoes = y[:90]

    teste_dados = x[-9:]
    teste_marcacoes = y[-9:]


    modelo = MultinomialNB()
    modelo.fit(treino_dados,treino_marcacoes)



    resultado  = modelo.predict(teste_dados)
    diferencas = resultado - teste_marcacoes
    acertos = [d for d in diferencas if d == 0]
    total_de_acertos = len(acertos)
    total_elementos = len(x)
    print("Total de elementos: {}".format(total_elementos))
    taxa_de_acertos = 100.0 * total_de_acertos / total_elementos

    print(taxa_de_acertos)
    print(total_de_acertos)

if(__name__== "__main__"):
    mostra_dados()