from musica import *
from tkinter import *

janela = Tk()
janela.title("Tocador de musicas com Pygame")
janela.geometry("400x400")

texto_orientacao = Label(janela,text="Clique em um dos botões para tocar alguma musica.",padx= 20,pady= 20)
texto_orientacao.grid(column=0,row=0)

musica1 = Button(janela, text="Saudades da Rosa", command=dar_play_em_cond,padx=0,pady= 10)
musica1.grid(column=0,row=2)

musica2 = Button(janela, text="Oasis - Bardo", command=dar_play_em_bardo,padx= 12,pady= 10)
musica2.grid(column=1,row=2)