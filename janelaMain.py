from tkinter import *
from editor import Editor

class JanelaMain():
    def __init__(self) -> None:
        print("janela main criada")
        self.JanelaPrincipal()
        #self.MenuPrincipal()
        self.LogoMaiaNote()
        self.root.mainloop()


    def JanelaPrincipal(self):
        self.root = Tk()
        self.favicon = PhotoImage(file="icones/favicon1.png")
        self.root.iconphoto(True,self.favicon)
        self.root.title("Maia Note")
        #self.root.geometry("640x580")
        self.root.geometry("1280x720")
        self.root.after(102000,self.AbrirEditor)

    
    def MenuPrincipal(self):
        self.menubar = Menu(self.root, borderwidth=1, relief="solid", bg="#232323", fg="#e7e7e7", activebackground="#131313",activeforeground="#e7e7e7")
        self.menuArquivo = Menu(self.menubar, tearoff=0, borderwidth=1, relief="solid", bg="#232323", fg="#e7e7e7", activebackground="#131313",activeforeground="#e7e7e7")
        self.menuArquivo.add_command(label="Novo",command=lambda:self.Click("novo"))
        self.menubar.add_cascade(label="Arquivo", menu=self.menuArquivo)
        self.root.config(menu=self.menubar)


    def LogoMaiaNote(self):
        self.imagemLogo = PhotoImage(file="imagens/logoMaia.png")
        self.logoMaiaNote = Label(self.root,image=self.imagemLogo)
        self.logoMaiaNote.pack(side=TOP, fill=BOTH, expand=1,anchor=W)
        self.creditoImagem = Label(self.root,text="Fonte de: https://www.dafont.com/magnus-cederholm.d1740")
        self.creditoImagem.place(relx=0.08, rely=0.75,relwidth=1,anchor=W)

    
    def Click(self,parametro):
        if parametro == "novo":
            self.root.destroy()
            self.editor = Editor()
            
            
    def AbrirEditor(self):
        self.root.destroy()
        self.editor = Editor()
