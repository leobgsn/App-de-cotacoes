import requests
import json
from tkinter import *



def pegar_cotacoes():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']["bid"]
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_btc = cotacoes['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


    

janela = Tk()
janela.title("cotacao atual das moedas")
janela.geometry("400x500")


texto_orientacao = Label(janela, text="clique no botao para ver as cotacoes das moedas")
texto_orientacao.grid(column=0, row=0, padx=50, pady=50)

botao = Button(janela, text="buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)












janela.mainloop()