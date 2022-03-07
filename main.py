from classificacao_web import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

def mostra_dados():

    x, y = carregar_acessos()
    #print('essas são as marcações {}'.format(x))

    modelo = MultinomialNB()
    modelo.fit(x,y)

    #print(modelo.predict([[1,0,1],[0,1,0],[1,0,0],[1,1,0],[1,1,1]]))

    resultado  = modelo.predict(x)
    diferencas = resultado - y
    acertos = [d for d in diferencas if d == 0]
    total_acertos = len(acertos)
    total_elementos = len(x)
    taxa_de_acertos = 100.0 * total_acertos / total_elementos

    print(taxa_de_acertos)
    print(total_acertos)

if(__name__== "__main__"):
    mostra_dados()