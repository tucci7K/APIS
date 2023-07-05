import requests
import pprint #essa biblioteca ajuda na organização visual do dados
import json

link = "https://servicodados.ibge.gov.br/api/v3/agregados/4112/periodos/2006/variaveis/2586?localidades=N1[all]"
#faz a requisição
requisicao = requests.get(link)
#retorna a requisicao em JSON! #lembre-se sempre de separar em variaveis para organização!
informacoes = requisicao.json()

import pprint #essa biblioteca ajuda na organização visual do dados


item_busca =informacoes[0]['variavel'] #variavel
resultados = (informacoes[0]['resultados'][0]['series'])

pprint.pprint(item_busca)
pprint.pprint(resultados)