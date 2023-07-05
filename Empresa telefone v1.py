#Aqui, já foi mepado o ID da empresa, e agora queremos descriminar o telefone dessa empresa!
import requests
import json

url = "https://api.pipe.run/v1/companies/9520411?with=contactPhones"

headers = {
    "accept": "application/json",
    "token": "xxxxxxxxxxxx"
}

#retorna o codigo 200 e da sequencia
response = requests.get(url, headers=headers)

if response.status_code ==200:
    info2 = response.json()

    #a ordem de organização é sempre nessa direção >>>>>>>>
    Numero_telefone = info2["data"]["contactPhones"][0]["phone"]
    print(Numero_telefone)
else: 
    print("A requisição falhou, erro:", response)