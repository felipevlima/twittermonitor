from tkinter import *
from twitter import Twitter
import time

#Criando a janela
janela = Tk()
#Funçao para procurar os tuites
def monitorar():
        Twitter.conexao(Twitter, 'S9CsaSPkR4hBHQQup2IItIXlq', 'cgqyhmEtIqDZwHaJTCIzvCVRu2XMJqHLEhJNzNjWwj165lCd9i',
                    '4851645801-8dO8LUVGlWPh9uonu8aBKkqGNpVKb49tfHXETg8',
                    'ozAXIowQPx2ZBJEdQUhzq8rlaS6w1ikQfqRz3W7gMWaAt')
        assunto = input('Diga a query: ')
        idioma = input('Diga o idioma: ')
        tuites = Twitter.search(Twitter, assunto, idioma)
        while True:
            print('---------------------------REFRESH-----------------------------')
            for twits in tuites:
                #Mudando o texto do label
                v.set(twits['user']['screen_name'])

            time.sleep(15)
#Criando uma variavel de texto
v=StringVar()
janela.geometry('800x600+200+50')
#Botao para disparar funcao
btnBotao = Button(janela,text='Monitorar',width='16',command=monitorar)
btnBotao.place(x=300,y=250)

Label(janela,textvariable=v,font=("Arial",15)).pack()
v.set('Vazio')



janela.mainloop()