import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

#janeiro 2018
estoque_janeiro_2018 = 1596
consumo_progressivo_janeiro_2018 = 1596
dados_janeiro_2018 = [estoque_janeiro_2018,consumo_progressivo_janeiro_2018]

#fevereiro 2018
estoque_fevereiro_2018 = 0
consumo_progressivo_fevereiro_2018 = 1641
dados_fevereiro_2018 = [estoque_fevereiro_2018,consumo_progressivo_fevereiro_2018]

#março 2018
estoque_marco_2018 = 0
consumo_progressivo_marco_2018 = 1519
dados_marco_2018 = [estoque_marco_2018,consumo_progressivo_marco_2018]


#abril 2018
estoque_abril_2018 = 0
consumo_progressivo_abril_2018 = 1641
dados_abril_2018 = [estoque_abril_2018,consumo_progressivo_abril_2018]

#maio 2018
estoque_maio_2018 = 9800
consumo_progressivo_maio_2018 = 1650
dados_maio_2018 = [estoque_maio_2018,consumo_progressivo_maio_2018]

#junho 2018
estoque_junho_2018 = 1000
consumo_progressivo_junho_2018 = 1729
dados_junho_2018 = [estoque_junho_2018,consumo_progressivo_junho_2018]

#julho 2018
estoque_julho_2018 = 26800
consumo_progressivo_julho_2018 = 1841
dados_julho_2018 = [estoque_julho_2018,consumo_progressivo_julho_2018]

#agosto 2018
estoque_agosto_2018 = 58750
consumo_progressivo_agosto_2018 = 1892
dados_agosto_2018 = [estoque_agosto_2018,consumo_progressivo_agosto_2018]

#setembro 2018
estoque_setembro_2018 = 62540
consumo_progressivo_setembro_2018 = 1729
dados_setembro_2018 = [estoque_setembro_2018,consumo_progressivo_setembro_2018]

#outubro 2018
estoque_outubro_2018 = 26740
consumo_progressivo_outubro_2018 = 1810
dados_outubro_2018 = [estoque_outubro_2018,consumo_progressivo_outubro_2018]

#novembro 2018
estoque_novembro_2018 = 16780
consumo_progressivo_novembro_2018 = 2059
dados_novembro_2018 = [estoque_novembro_2018,consumo_progressivo_novembro_2018]

#dezembro 2018
estoque_dezembro_2018 = 38560
consumo_progressivo_dezembro_2018 = 1925
dados_dezembro_2018 = [estoque_dezembro_2018,consumo_progressivo_dezembro_2018]


dados = [dados_janeiro_2018,dados_fevereiro_2018,
         dados_marco_2018,dados_abril_2018,
         dados_maio_2018,dados_junho_2018,
         dados_julho_2018,dados_agosto_2018,
         dados_setembro_2018,dados_outubro_2018,
         dados_novembro_2018,dados_dezembro_2018]

#previsoes_2018 = [69645,69645,69645]
previsoes_2018 = [69645,69645,
                  69645,75412,
                  102578,102578,
                  136731,102578,
                  102578,102578,
                  148818,118728]

#janeiro 2019
estoque_janeiro_2019 = 27540
consumo_progressivo_janeiro_2019 = 2045
dados_janeiro_2019 = [estoque_janeiro_2019,consumo_progressivo_janeiro_2019]

#fevereiro 2019
estoque_fevereiro_2019 = 12540
consumo_progressivo_fevereiro_2019 = 2282
dados_fevereiro_2019 = [estoque_fevereiro_2019,consumo_progressivo_fevereiro_2019]

#março 2019
estoque_marco_2019 = 7640
consumo_progressivo_marco_2019 = 2433
dados_marco_2019 = [estoque_marco_2019,consumo_progressivo_marco_2019]


modelo = MultinomialNB()
modelo.fit(dados,previsoes_2018)
teste = [dados_janeiro_2019,dados_fevereiro_2019,dados_marco_2019]

resultado = modelo.predict(teste)
print("As previsões simuladas foram  janeiro: {} , fevereiro: {} março: {}".format(resultado[0], resultado[1],
                                                                       resultado[2]))

marcacoes_teste = [118728,148818,148818]
print("previsões reais foram janeiro: {} , fevereiro: {} e março: {}".format(marcacoes_teste[0], marcacoes_teste[1],
                                                                          marcacoes_teste[2]))

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d==0]
print("Total de acertos: {}".format(len(acertos)))

total_de_acertos = len(acertos)
