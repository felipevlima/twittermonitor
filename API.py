import time
from twitter import Twitter

Twitter.conexao(Twitter,'S9CsaSPkR4hBHQQup2IItIXlq','cgqyhmEtIqDZwHaJTCIzvCVRu2XMJqHLEhJNzNjWwj165lCd9i','4851645801-8dO8LUVGlWPh9uonu8aBKkqGNpVKb49tfHXETg8','ozAXIowQPx2ZBJEdQUhzq8rlaS6w1ikQfqRz3W7gMWaAt')
assunto = input('Diga a query: ')
idioma = input('Diga o idioma: ')
tuites = Twitter.search(Twitter,assunto,idioma)
while True:
    print('---------------------------REFRESH-----------------------------')
    for twits in tuites:
        print(twits['user']['screen_name'])
        print(twits['text'])
        print(' ')

    time.sleep(10)