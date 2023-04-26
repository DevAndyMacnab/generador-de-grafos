from tkinter import Button, scrolledtext as st
from tkinter import Label, Entry,messagebox
from tkinter import messagebox as messagebox
from tkinter import Frame
from controller.Grafo import generarGrafo,generarAlgoritmo

class Principal:
    def __init__(self,window):
        self.principal = window
        self.principal.title("Algoritmo de busqueda de anchura")
        self.principal.resizable(width=False,height=False)
        
        self.frameFunciones= Frame(self.principal)
        self.frameFunciones.grid(row=0,column=0)
        self.frameFunciones.config(width="250",height="300" )
        
        
        #Botones
        self.generarGrafo=Button(self.principal,text="Generar Grafo",command=lambda:self.pasoDatos(),
                                 width=16,height=4)
        self.generarGrafo.grid(row=0,column=2,padx=15)
        
        self.generarAlgoritmo=Button(self.principal,text="Generar BFS", command=lambda:self.generoAlgoritmo(), width=16,height=4)
        self.generarAlgoritmo.configure(state="disabled")
        self.generarAlgoritmo.grid(row=1,column=2,padx=15,pady=15)
        
        
        #Labels
        self.aristas=Label(self.principal,text="Ingrese las aristas: (AB,BC,CB)")
        self.aristas.grid(row=1,column=0)
        self.vertices=Label(self.principal,text="Ingrese los vertices: (A,B,C)")
        self.vertices.grid(row=0,column=0)
        
        
        #Entrys
        
        self.verticesEntry=Entry()
        self.verticesEntry.grid(row=0,column=1)
        
        self.aristasEntry=Entry()
        self.aristasEntry.grid(row=1,column=1)
        
    def pasoDatos(self):
        vertices=self.verticesEntry.get()
        aristas=self.aristasEntry.get()
        self.grafo=generarGrafo(vertices,aristas,self.generarAlgoritmo)
        if (self.grafo):
            
           pass            
            
        else:
            messagebox.showinfo(message="Ha ocurrido un error para generar el grafo", title="Error del Sistema")
            
        
    def generoAlgoritmo(self):
        generarAlgoritmo(self.grafo)
        
        
          
        
        