#Aqui, já foi mepado o ID da empresa, e agora queremos descriminar o telefone dessa empresa!
import requests
import json

url = "https://api.pipe.run/v1/companies/9520411?with=contactPhones"

headers = {
    "accept": "application/json",
    "token": ""
}

#retorna o codigo 200 e da sequencia
response = requests.get(url, headers=headers)
if response.status_code ==200:
    info2 = response.json()
    
  #onde eu vou armazenar meus numeros de telefone!
    numeros_telefone=[]
    #Incia-se o laço, ele procura os numeros de contato dentro de data!
    if "contactPhones" in info2["data"]:

        #busca  objeto de telefone na lista "contact phones"
        for phone in info2["data"]["contactPhones"]:

            #Extrai o número de telefone do objeto de telefone atual.
            numero_telefone = phone["phone"]

            #  Extrai e Adiciona o número de telefone à lista vazia até ser satisfeita
            numeros_telefone.append(numero_telefone)

    print("Números de telefone:")
    for numero in numeros_telefone:
            #pq o print "numeros_telefone" não é suficiente?
            # Pelo oque testei só retorna o ultimo elemento, já o numeros retorna todos os elementos dentro de "numeros_telefone"
            print(numero)
else:
    print("A requisição falhou, erro:", response)