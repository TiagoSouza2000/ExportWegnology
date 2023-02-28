import requests

deviceId = 'xxxxxxxxxxxxxx'
#Copiar o ID do device
url = 'https://console.app.wnology.io/applications/'
#URL request GET
API_token = url + deviceId+'/application-tokens/xxxxxxxxxxxxxxx'
#Colar o token da API com permissão suficiente

headers = {'AuthorizationY': 'Bearer ='+ API_token
           }

arquivo = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
#url recebida por email ao exportar uma tabela
resposta = requests.get(url, headers=headers)

if resposta.status_code == 200: # OK na request HTTP e escreve no arquivo
    response = requests.get(arquivo)
    with open('Export.csv', 'wb') as f:
        f.write(response.content)
        print("O download do arquivo foi  concluído")

else:
    print('Erro: ', resposta.status_code)