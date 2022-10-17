from musica import *
from tkinter import *

janela = Tk()
janela.title("Tocador de musicas com Pygame")

texto_orientacao = Label(janela,text="Clique em um dos botões para tocar alguma musica.")
texto_orientacao.grid(column=0,row=0)
musica1 = Button(janela, text="Saudades da Rosa", command=darplay)
musica1.grid(column=2,row=4)

janela.mainloop()