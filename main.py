from classificacao_web import carregar_acessos

def mostra_dados():

    dados, marcacoes = carregar_acessos()
    print('essas são as marcações {}'.format(marcacoes))

if(__name__== "__main__"):
    mostra_dados()