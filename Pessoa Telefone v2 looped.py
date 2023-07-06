import requests

url = "https://api.pipe.run/v1/persons/15946906?with=contactPhones"

headers = {
    "accept": "application/json",
    "token": ""
}

response = requests.get(url, headers=headers)
if response.status_code ==200:
    info3 = response.json() 
   
   #onde eu vou armazenar meus numeros de telefone!
    numeros_telefone=[]
    #Incia-se o laço, ele procura os numeros de contato dentro de data!
    if "contactPhones" in info3["data"]:

        #busca  objeto de telefone na lista "contact phones"
        for phone in info3["data"]["contactPhones"]:

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
