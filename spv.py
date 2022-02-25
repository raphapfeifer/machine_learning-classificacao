import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

#janeiro 2019
estoque_janeiro_2018 = 1596
consumo_progressivo_janeiro_2018 = 1596
dados_janeiro_2019 = [estoque_janeiro_2018,consumo_progressivo_janeiro_2018]

#fevereiro 2019
estoque_fevereiro_2018 = 0
consumo_progressivo_fevereiro_2018 = 1641
dados_fevereiro_2019 = [estoque_fevereiro_2018,consumo_progressivo_fevereiro_2018]

#março 2019
estoque_marco_2018 = 0
consumo_progressivo_marco_2018 = 1519
dados_marco_2019 = [estoque_marco_2018,consumo_progressivo_marco_2018]

dados = [dados_janeiro_2019,dados_fevereiro_2019,dados_marco_2019]

previsoes_2018 = [69645,69645,69645]

#janeiro 2022
estoque_janeiro_2022 = 2045
consumo_progressivo_janeiro_2022 = 27540
dados_janeiro_2022 = [estoque_janeiro_2022,consumo_progressivo_janeiro_2022]

#fevereiro 2022
estoque_fevereiro_2022 = 12540
consumo_progressivo_fevereiro_2022 = 2282
dados_fevereiro_2022 = [estoque_fevereiro_2022,consumo_progressivo_fevereiro_2022]


modelo = MultinomialNB()
modelo.fit(dados,previsoes_2018)
teste = [dados_janeiro_2022,dados_fevereiro_2022]

resultado = modelo.predict(teste)
print("As previsões simuladas foram  janeiro {} e fevereiro {}".format(resultado[0], resultado[1]))

marcacoes_teste = [118728,148818]
print("previsões reais foram janeiro {} e fevereiro {}".format(marcacoes_teste[0], marcacoes_teste[1]))

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d==0]
print("Total de acertos: {}".format(len(acertos)))

total_de_acertos = len(acertos)
