import requests
import json 

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(cotacoes)
print(cotacoes.json())


dicionario = cotacoes.json()
print(dicionario['USDBRL']['bid'])