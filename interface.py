from tkinter import *
from twitter import Twitter
import time


#CRIANDO A JANELA PRINCIPAL
janela = Tk()
janela.geometry('800x600+100+50')
janela.title('Twitter Monitor')

#CREDENCIAIS PARA AUTENTICAR OAUTH
Twitter.conexao(Twitter,'S9CsaSPkR4hBHQQup2IItIXlq','cgqyhmEtIqDZwHaJTCIzvCVRu2XMJqHLEhJNzNjWwj165lCd9i','4851645801-8dO8LUVGlWPh9uonu8aBKkqGNpVKb49tfHXETg8','ozAXIowQPx2ZBJEdQUhzq8rlaS6w1ikQfqRz3W7gMWaAt')


def pesquisar():
    while True:
        assunto = texto.get()
        resultado2 = monitorar(assunto)
        v.set(resultado2)


def monitorar(ass):
    '''
    NA LINHA 21 ESTÁ O SEGREDO DA FUNÇÃO
    SEMPRE QUE ELA É CHAMADA GERA UM NOVO RESULTADO
    '''
    tuites = Twitter.search(Twitter, ass, 'pt')
    for twites in tuites:
        nome = twites['user']['screen_name']
        texto = twites['text']
        resultado = nome+': '+texto
        return resultado

v = StringVar()
lbl = Label(janela, textvariable=v, font=("Helvetica",10))
lbl.place(x=150,y=180)
v.set('vazio')

texto = Entry(janela,width=20)
texto.place(x=150,y=150)

botao = Button(janela,text='OK',width=3,command=pesquisar)
botao.place(x=277,y=150)

#LOOP PARA JANELA
mainloop()

