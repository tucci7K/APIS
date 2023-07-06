#Nessa primeira parte, é necessario buscar o numero da oportunidade em que queremos evidenciar.
#Após ela ser executada, queremos a informação do COMPANY-ID
import requests
import json

#define o inicio da minha função que vai realizar minha API
def info_oportunidade(oportunidade_id):

    #fim da URL é o endereço da OP (Como eu vou criar uma maneira dessa variavel sempre se atualizar?)
    url = "https://api.pipe.run/v1/deals/25015186" 

    #execucação da API
    headers = {
        "accept": "application/json",
        "token": ""
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

        return empresa_id, pessoa_id
    else: 
        print("A requisição falhou, erro:", response)
        return None, None
# Lista de IDs de oportunidades que quero evidenciar
oportunidades = [25015186, 12345678, 98765432]

#Onde eu vou armazenar meus dados!
dados=[]

#Aqui ele BUSCA O ID de oportunidades e busca as informações na função, ou seja, declaro as variaveis e depois mandei buscar na função
for oportunidade_id in oportunidades:
     empresa_id, pessoa_id = info_oportunidade(oportunidade_id)

#Agora tenho que armazenar os dados...
dados.append({
        'oportunidade_id': oportunidade_id,
        'empresa_id': empresa_id,
        'pessoa_id': pessoa_id
    })
#Agora imprimir os dados que capturei
for dado in dados:
    print("ID da oportunidade:", dado['oportunidade_id'])
    print("ID da empresa:", dado['empresa_id'])
    print("ID da pessoa:", dado['pessoa_id'])
  