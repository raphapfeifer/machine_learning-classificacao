from classificacao_web import carregar_acessos

def mostra_dados():

    x, y = carregar_acessos()
    print('essas são as marcações {}'.format(x))

if(__name__== "__main__"):
    mostra_dados()