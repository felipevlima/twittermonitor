from tkinter import *
from twitter import Twitter
import time


#CRIANDO A JANELA PRINCIPAL
janela = Tk()
janela.geometry('800x600+100+50')
janela.title('Twitter Monitor')

#CREDENCIAIS PARA AUTENTICAR OAUTH
Twitter.conexao(Twitter,'S9CsaSPkR4hBHQQup2IItIXlq','cgqyhmEtIqDZwHaJTCIzvCVRu2XMJqHLEhJNzNjWwj165lCd9i','4851645801-8dO8LUVGlWPh9uonu8aBKkqGNpVKb49tfHXETg8','ozAXIowQPx2ZBJEdQUhzq8rlaS6w1ikQfqRz3W7gMWaAt')
assunto = input('Diga a query: ') #Entrada com assunto
idioma = input('Diga o idioma: ') #IDIOMA PARA REGIÃO


def monitorar():
    '''
    NA LINHA 21 ESTÁ O SEGREDO DA FUNÇÃO
    SEMPRE QUE ELA É CHAMADA GERA UM NOVO RESULTADO
    '''
    tuites = Twitter.search(Twitter, assunto, idioma)
    for twites in tuites:
        nome = twites['user']['screen_name']
        texto = twites['text']
        resultado = nome+': '+texto
        return resultado

v = StringVar()
Label(janela, textvariable=v, font=("Helvetica",10)).pack()
var = monitorar()
v.set(var)



#LOOP PARA JANELA
janela.mainloop()
