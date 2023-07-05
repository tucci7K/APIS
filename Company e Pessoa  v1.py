#Nessa primeira parte, é necessario buscar o numero da oportunidade em que queremos evidenciar.
#Após ela ser executada, queremos a informação do COMPANY-ID
import requests
import json

#fim da URL é o endereço da OP (Como eu vou criar uma maneira dessa variavel sempre se atualizar?)
url = "https://api.pipe.run/v1/deals/25015186" 

#execucação da API
headers = {
    "accept": "application/json",
    "token": "xxxxxxxxxxxx"
}
#valida a reposta da pagina se for 200 é pq deu certo
response = requests.get(url, headers=headers)
 #busca a resposta e analisa em JSON
if response.status_code ==200:
    info1 = response.json() 
 
    #aqui pega o ID Da empresa, é necessario INFORMAR QUE A INFORMAÇÃO É UM {DICIONARIO} e para buscar seus dados, 
    #é necessario informar o seu nome de origem antes do EX: data =  {....}
    empresa_id = info1['data']['company_id']
    pessoa_id = info1['data']['person_id']

    print("ID da empresa :", empresa_id)
    print("ID da pessoa :", pessoa_id)
else: 
    print("A requisição falhou, erro:", response)