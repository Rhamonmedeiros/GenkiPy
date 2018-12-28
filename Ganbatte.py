#Ganbatte
#Ensino de Python - lembrar de colocar botão para abrir o Idle.
import sys
import os
import tkinter
from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
#___________________________Labels______________________________________________________________________________
        self.style = ttk.Style()#Aqui eu defino um padrão para os Labels.
        self.style.configure("BW.TLabel", foreground="blue", font = ("times new roman", 15))#Importante copiar o Bw.

#__________________________Button________________________________________________________________________________
        self.styleButton = ttk.Style()
        self.styleButton.map("C.TButton",
            foreground=[('pressed', 'yellow'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')],
                           
            
        )

        #colored_btn = ttk.Button(text="Test", style="C.TButton").pack() exemplo para o botão funcionar

        #self.l1 = ttk.Label(self.primeiroContainer, text="Teste", style="BW.TLabel")
        #self.l1.pack()
        
  
        self.titulo = ttk.Label(self.primeiroContainer, text="Ganbatte v1.0", style="BW.TLabel", font = ("Lucida Console",22))#padding - distancia entre label, width - tamanho.
        self.titulo.pack()
        
        self.indice = ttk.Button(self.terceiroContainer, text = "Indice", command = self.indice_2, style = "C.TButton")
        self.indice.pack()
        #self.nomeLabel = ttk.Label(self.segundoContainer,text="Aprenda Python usando Python!\n\n\nNenhum ser humano é limitado\nEliud Kipchogue", style = "BW.TLabel")
        #self.nomeLabel.pack(side=LEFT)
  
        self.autenticar = ttk.Button(self.segundoContainer, text = "Iniciar", command = self.Introducao, style = "C.TButton")
        self.autenticar.pack()#dessa forma é possivel destroy().#Bottom fica em cima do outro
        
  
  
    #Método verificar senha
    def Introducao(self):
        try:
            self.indice.destroy()
            self.autenticar.destroy()
            #self.nomeLabel.destroy()
            self.autentica = ttk.Button(self.terceiroContainer, text = "Seguir", command = self.ambiente, style = "C.TButton")
            self.autentica.pack()
            self.introducao = ttk.Label(self.primeiroContainer, text ="Introdução",style="BW.TLabel")
            self.introducao.pack()
            self.textIntro = ttk.Label(self.segundoContainer, text = "Este software tem como objetivo disseminar o conhecimento sobre a linguagem Python.",style="BW.TLabel")
            self.textIntro.pack()
           
        except:
            self.introducao = ttk.Label(self.segundoContainer, text ="Bug",style="BW.TLabel").pack()
    def ambiente(self):
        try:
            self.autentica.destroy()
            self.introducao.destroy()
            self.textIntro.destroy()
            
            self.ambiente1 = ttk.Label(self.segundoContainer, text = "Clique no botão abaixo para conhecer a historia do python.", style="BW.TLabel")
            self.ambiente1.pack()
            self.cmd = ttk.Button(self.terceiroContainer, text = "Historia Py", command = self.historyPy, style = "C.TButton")
            self.cmd.pack(side = LEFT)
            self.seguir = ttk.Button(self.terceiroContainer, text = "Seguir", command = self.indice)
            self.seguir.pack(side = RIGHT)
        except:
            self.introducao = ttk.Label(self.segundoContainer, text ="Bug",style="BW.TLabel").pack()
    def indice(self):
        try:
            self.ambiente1.destroy()
            self.cmd.destroy()
            self.introducao.destroy()
            self.textIntro.destroy()
            self.seguir.destroy()
            self.indice = ttk.Label(self.terceiroContainer, text = "Indice", style="BW.TLabel")
            self.indice.pack()
            self.aulaUm = ttk.Button(self.terceiroContainer, text = "Aula 1", command = self.indice, style = "C.TButton")
            self.aulaUm.pack()
            self.idle = ttk.Button(self.segundoContainer, text = "Idle", style = "C.TButton", command = self.idle)#Deixar Fixo para abrir o Idle.
            self.idle.pack(side = RIGHT)
        except:
            None
    def historyPy(self):
        import sys
        import os
        os.startfile("https://wiki.python.org.br/HistoriaDoPython")
        
    def idle(self):#Esse codigo faz o python executar algum programa.
        import sys
        import os
        
        os.startfile('python.exe')#por motivos de não sei, o pythonw (Idle não executa), por isso uso o cmd (python.exe)

    #---------------------------------------------------Inicio das aulas--------------------------------------------------------------#
    def indice(self):
        try:
            self.indice.destroy()
            self.aulaUm.destroy()
            self.aula1 = ttk.Label(self.primeiroContainer, text = "Aula 1", fg = "blue")
            self.aula1.pack()
            self.idle = ttk.Button(self.primeiroContainer, text = "Idle", style="BW.TLabel", command = self.idle)#Deixar Fixo para abrir o Idle.
            self.idle.pack()
        except:
            None

    def indice_2(self):
        try:
            self.indice.destroy()
            self.autenticar.destroy()
            self.aulaUm = ttk.Button(self.terceiroContainer, text = "Aula - 1", style="C.TButton")
            self.aulaUm.pack()
            self.idle = ttk.Button(self.segundoContainer, text = "Idle", style="C.TButton", command = self.idle)#Deixar Fixo para abrir o Idle.
            self.idle.pack()
        except:
             self.introducao = ttk.Label(self.segundoContainer, text ="Bug",style="BW.TLabel")
             self.introducao.pack()              
root = tkinter.Tk()
Application(root)
root.mainloop()
