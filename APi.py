import oauth2
import json
import urllib
import time

consumer_key  = 'S9CsaSPkR4hBHQQup2IItIXlq'
conseumer_sec = 'cgqyhmEtIqDZwHaJTCIzvCVRu2XMJqHLEhJNzNjWwj165lCd9i'

token_key     = '4851645801-8dO8LUVGlWPh9uonu8aBKkqGNpVKb49tfHXETg8'
token_sec     = 'ozAXIowQPx2ZBJEdQUhzq8rlaS6w1ikQfqRz3W7gMWaAt'

consumer = oauth2.Consumer(consumer_key,conseumer_sec)
token    = oauth2.Token(token_key,token_sec)
query    = input('Diga o que quer monitorar: ')
query_cod= urllib.parse.quote(query,safe='')
idioma   = input('Indioma da pesquisa (DEIXE EM BRANCO PARA TODOS)')

cliente = oauth2.Client(consumer,token)
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+query_cod+'&lang='+idioma)

decodificar = requisicao[1].decode()
obejto_dicionario = json.loads(decodificar)
while True:
    print('---------------------------REFRESH-----------------------------')
    for tuites in obejto_dicionario['statuses']:
        print(tuites['user']['screen_name'])
        print(tuites['text'])
        print(' ')
    time.sleep(10)