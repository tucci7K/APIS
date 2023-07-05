import requests

url = "https://api.pipe.run/v1/persons/15946906?with=contactPhones"

headers = {
    "accept": "application/json",
    "token": "xxxxxxxxxxxx"
}

response = requests.get(url, headers=headers)
if response.status_code ==200:
    info3 = response.json() 
    print(info3)
    numero_telefone2 =  info3["data"]["contactPhones"][0]["phone"]
    numero_telefone3 =  info3["data"]["contactPhones"][1]["phone"]
    print(numero_telefone2)
    print(numero_telefone3)
else:
    print("A requisição falhou, erro:", response)