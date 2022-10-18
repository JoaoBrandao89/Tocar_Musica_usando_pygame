from musica import *
from tkinter import *

janela = Tk()
janela.title("Tocador de musicas com Pygame")
janela.geometry("300x300")

texto_orientacao = Label(janela,text="Clique em um dos botões para tocar alguma musica.",padx= 20,pady= 20)
texto_orientacao.grid(column=0,row=0)


musica1 = Button(janela, text="Saudades da Rosa", command = dar_play_em_cond,padx=0,pady= 10)
musica1.grid(column=0 , row=1)

musica2 = Button(janela, text="Oasis - Bardo", command = dar_play_em_bardo,padx= 12,pady= 10)
musica2.grid(column=0,row=2)

musica3 = Button(janela, text="Sweater weather", command = dar_play_em_sweat,padx= 5,pady= 12)
musica3.grid(column=0,row=3)



texto_fim = Label(janela,text="")
texto_fim.grid(column=0,row=8,padx=0,pady=20)

janela.mainloop()