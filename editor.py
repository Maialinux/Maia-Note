from tkinter import *
from tkinter import ttk, filedialog, messagebox
import datetime,math



class Editor():
    def __init__(self) -> None:
        print("janela editor criada")
        self.JanelaPrincipal()
        self.MenuPrincipal()
        self.SetEditorTexto()       
        self.root.mainloop()


    def JanelaPrincipal(self):
        self.root = Tk()
        self.favicon = PhotoImage(file="icones/favicon1.png")
        self.root.iconphoto(True,self.favicon)
        self.root.title("Editor de Texto")
        self.root.geometry("1280x720")
        self.AtalhoDoTeclado()
        
        

    
    def MenuPrincipal(self):
        self.SetIcons()
        # Menu Arquivo
        self.menubar = Menu(self.root, borderwidth=1, relief="solid", bg="#232323", fg="#e7e7e7", activebackground="#131313",activeforeground="#e7e7e7")
        self.menuArquivo = Menu(self.menubar, tearoff=0, borderwidth=1, relief="solid", bg="#232323", fg="#e7e7e7", activebackground="#131313",activeforeground="#e7e7e7")
        self.menuArquivo.add_command(label="Novo",command=lambda:self.Click("novo"),image=self.iconeNovo, compound=LEFT, accelerator="Ctrl+N")
        self.menuArquivo.add_command(label="Abrir",command=lambda:self.Click("abrir"),image=self.iconeAbrir, compound=LEFT, accelerator="Ctrl+O")
        self.menuArquivo.add_command(label="Salvar",command=lambda:self.Click("salvar"),image=self.iconeSalvar, compound=LEFT, accelerator="Ctrl+S")
        self.menuArquivo.add_command(label="Imprimir",command=lambda:self.Click("imprimir"),image=self.iconeImprimir, compound=LEFT, accelerator="Ctrl+P")
        self.menuArquivo.add_command(label="Sair",command=lambda:self.Click("sair"),image=self.iconeSair, compound=LEFT, accelerator="Ctrl+Q")
        self.menubar.add_cascade(label="Arquivo", menu=self.menuArquivo)
        # Menu Editar
        self.menuEditar = Menu(self.menubar, tearoff=0, borderwidth=1, relief="solid", bg="#232323", fg="#e7e7e7", activebackground="#131313",activeforeground="#e7e7e7")
        self.menuEditar.add_command(label="Desfazer",command=lambda:self.Click("desfazer"),image=self.iconeDesfazer, compound=LEFT, accelerator="Ctrl+Z")
        self.menuEditar.add_command(label="Refazer",command=lambda:self.Click("refazer"),image=self.iconeRefazer, compound=LEFT, accelerator="Ctrl+Y")
        self.menuEditar.add_command(label="Recortar",command=lambda:self.Click("recortar"),image=self.iconeRecortar, compound=LEFT, accelerator="Ctrl+X")
        self.menuEditar.add_command(label="Copiar",command=lambda:self.Click("copiar"),image=self.iconeCopiar, compound=LEFT, accelerator="Ctrl+C")
        self.menuEditar.add_command(label="Colar",command=lambda:self.Click("colar"),image=self.iconeColar, compound=LEFT, accelerator="Ctrl+V")
        self.menuEditar.add_command(label="Selecionar Tudo",command=lambda:self.Click("selecionarTudo"),image=self.iconeSelecionarTudo, compound=LEFT, accelerator="Ctrl+A")
        self.menuEditar.add_command(label="Inserir Data e Hora",command=lambda:self.Click("dataEHora"),image=self.iconeDataEHora, compound=LEFT, accelerator="Ctrl+T")
        self.menubar.add_cascade(label="Editar", menu=self.menuEditar)
        self.root.config(menu=self.menubar, background="#131313")


    def SetIcons(self):
        # ICONES DO MENU ARQUIVO
        self.iconeNovo = PhotoImage(file="icones/novo.png")
        self.iconeAbrir = PhotoImage(file="icones/abrir.png")
        self.iconeSalvar = PhotoImage(file="icones/salvar.png")
        self.iconeImprimir = PhotoImage(file="icones/imprimir.png")
        self.iconeSair = PhotoImage(file="icones/fechar.png")
        # ICONES DO MENU EDITAR
        self.iconeDesfazer = PhotoImage(file="icones/desfazer.png")
        self.iconeRefazer = PhotoImage(file="icones/refazer.png")
        self.iconeRecortar = PhotoImage(file="icones/recortar.png")
        self.iconeCopiar = PhotoImage(file="icones/copiar.png")
        self.iconeColar = PhotoImage(file="icones/colar.png")
        self.iconeSelecionarTudo = PhotoImage(file="icones/select_all.png")
        self.iconeDataEHora = PhotoImage(file="icones/data_hora.png")


    def SetEditorTexto(self):
        self.style = ttk.Style(self.root)
        # temas legais: plastik, elegance, black, aquativo, keramik, smog
        self.style.theme_use("black")
        self.painelLat = Frame(self.root,highlightbackground="#000000", highlightcolor="#000000",width=25)
        self.painelLat.pack(side=LEFT,fill=Y)
        self.linenumbers = Text(self.painelLat, width=2, font=("Terminus bold",13))
        self.linenumbers.pack(fill=Y,expand=True)
        self.painel = Frame(self.root,highlightbackground="#000000", highlightcolor="#000000")
        self.painel.pack(side=RIGHT,fill=BOTH,expand=1)
        self.scrollBar_V = ttk.Scrollbar(self.painel,orient="vertical")
        self.scrollBar_V.pack(side=RIGHT, fill=Y)
        # Text Area opcional cor de fundo #2a2a4a
        self.textArea = Text(self.painel,yscrollcommand=self.scrollBar_V.set, 
                             foreground="#E7E7E7", background="#131313", font=("Terminus bold",13),
                             highlightbackground="#131313",highlightcolor="#131313", 
                             insertbackground="white",undo=True)
        self.textArea.pack(side=TOP, fill=BOTH, expand=1)
        self.textArea.focus()
        self.scrollBar_V.config(command=self.textArea.yview)
        self.textArea.bind('<Key>', self.Update_Line_Numbers)
        self.textArea.bind("<Delete>", self.Update_Line_Numbers)
      

    def Update_Line_Numbers(self,parametro):
        lines = self.textArea.get("1.0", "end-1c").count("\n") + 1
        self.linenumbers.delete("1.0", "end")
        for i in range(1, lines+1):
            self.linenumbers.insert("end", str(i) + "\n")

  

    def Click(self,parametro):
       # Parâmetros do menu arquivo
        if parametro == "novo":
           self.Novo(False)
               
        elif parametro == "abrir":
            self.Abrir(False)

        elif parametro == "salvar":
            self.Salvar(False)

        elif parametro == "imprimir":
            print("imprimir")
        
        elif parametro == "sair":
           self.Sair(False)
        
        # Parâmetros do menu editar
        elif parametro == "desfazer":
            self.Desfazer()
            print("desfazer")
            
        elif parametro == "refazer":
            self.Refazer()
            print("refazer")
            
        elif parametro == "recortar":
            self.Recortar(False)
            print("recortar")    
            pass
        elif parametro == "copiar":
            self.Copiar(False)
            print("copiar")
            pass
        elif parametro == "colar":
            self.Colar(False)
            print("colar")
            pass
        elif parametro == "selecionarTudo":
            self.SelecionarTudo(False)
            print("selecionarTudo")
            pass
        elif parametro == "dataEHora":
            self.DataHora(False)
            print("dataEHora")
            pass



    # FUNÇÕES PARA COLOCAR NA FUNÇÃO CLICK MENU ARQUIVO        
    def Novo(self,e):
        if self.textArea.get("1.0","end").__sizeof__() != 50:
            print("Quer Salvar")
            resposta = messagebox.askyesno(title="Salvar arquivo",message="Você quer salvar arquivo ?")
            if resposta == True:
                self.Salvar()
            else:
                self.textArea.delete("1.0","end")
                self.textArea.focus()

            #subprocess.call("./arquivos/base.sh", shell=True) -> comando executa shell bash linux
        else:
            print("Não tem nada escrito")


    def Abrir(self,e):  
        try: 
            filename = filedialog.askopenfilename(initialdir = "./arquivos",title = "SELECIONE UM ARQUIVO",filetypes = (
                ("FORMATO DO ARQUIVO","*.mn"),
                ("ALL FILES","*.*"))) 
            
            if filename.endswith(".mn"):
                self.caminhoDoArquivo = filename
                print(self.caminhoDoArquivo)
                if self.caminhoDoArquivo != "":
                    with open(self.caminhoDoArquivo, "r") as arquivo:
                        self.arquivo = arquivo.read()
                        print("ARQUIVO CARREGADO: "+self.arquivo)
                        self.textArea.delete("1.0","end")
                        self.textArea.insert("end",self.arquivo)
                        arquivo.close()
                        messagebox.showinfo(title="Aviso", message="ARQUIVO CARREGADO")
            else:
                print(self.caminhoDoArquivo)
            
        except:
            messagebox.showinfo(title="Aviso", message="NENHUM ARQUIVO .mn ABERTO")
    

    def Salvar(self,e):
        try:
            filename = filedialog.asksaveasfilename(initialdir = "./arquivos", defaultextension=".mn", title = "GRAVAR MENSAGEM", filetypes = (
                ("FORMATO DO ARQUIVO",".mn"),
                ("ALL FILES","*.*")))
            
            if filename.endswith(".mn"):
                self.caminhoDoArquivo = filename
                print(self.caminhoDoArquivo)
                if self.caminhoDoArquivo != "":
                    with open(self.caminhoDoArquivo, "w") as arquivo:           
                        arquivo.write(self.textArea.get("1.0","end"))
                        arquivo.close()                  
                        #self.textArea.delete("1.0","end")
                        messagebox.showinfo(title="ARQUIVO SALVO", message="ARQUIVO SALVO COM SUCESSO")
                        resposta = messagebox.askyesno(title="Deseja continuar",message="Você deseja continuar editando ?")
                        if resposta == True:
                            self.textArea.focus()
                        else:
                            self.textArea.delete("1.0","end")
                            self.textArea.focus()
            else:
                print(self.caminhoDoArquivo)
        except:
            messagebox.showinfo(title="Aviso", message="DIGITE A EXTENSÃO CERTA")

    def Sair(self,e):
        self.root.destroy()
            

    # FUNÇÕES PARA COLOCAR NA FUNÇÃO CLICK MENU EDITAR
    def Desfazer(self):
        try:
            self.textArea.edit_undo()
        except:
            messagebox.showinfo(title="Aviso",message="PRECISA TER ESCRITO AO MENOS UMA PALAVRA")

    def Refazer(self):
        try:
            self.textArea.edit_redo()
            self.root.clipboard_clear()
        except:
            messagebox.showinfo(title="mensagem",message="PRECISA TER DESFEITO AO MENOS UMA PALAVRA")

    def Recortar(self,e):
        global selecionado
        try:
            # Checa se atalho foi usado
            if e:
                selecionado = self.root.clipboard_get()
            else:
                if self.textArea.selection_get():
                    selecionado = self.textArea.selection_get()
                    self.textArea.delete("sel.first","sel.last")
                    self.root.clipboard_clear()
                    self.root.clipboard_append(selecionado)
        except:
            messagebox.showinfo(title="Aviso",message="PRECISA TER SELECIONADO AO MENOS UMA PALAVRA")
    
    def Copiar(self,e):
        global selecionado
        try:
            # Checa se atalho foi usado
            if e:
                selecionado = self.root.clipboard_get()
            if self.textArea.selection_get():
                selecionado = self.textArea.selection_get()
                self.root.clipboard_clear()
                self.root.clipboard_append(selecionado)
        except:
            messagebox.showinfo(title="Aviso",message="PRECISA TER SELECIONADO AO MENOS UMA PALAVRA")

    def Colar(self,e):
        global selecionado
        try:
        # Checa se atalho foi usado
            if e:
                selecionado = self.root.clipboard_get()
            else:
                if selecionado:
                    posicao = self.textArea.index(INSERT)
                    self.textArea.insert(posicao,selecionado)
                    # print(posicao) -> me retorna o número da linha
                    self.root.clipboard_clear()
        except:
            messagebox.showinfo(title="Aviso",message="RECORTE OU COPIE AO MENOS UMA PALAVRA")


    def SelecionarTudo(self,e):
        self.textArea.tag_add("sel","1.0",END)

    def DataHora(self,e):
        # Pega a data e hora atual BR
        dataEhora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        # Pega a posição do cursor
        posicao = self.textArea.index(INSERT)
        #print(math.floor(float(posicao))) -> Funciona para visualizar as linhas 
        # Insere data e hora na posição do cursor
        self.textArea.insert(posicao,dataEhora)

    def AtalhoDoTeclado(self):
        # Atalhos e Evento de Tecla do Menu Arquivos
        self.root.bind("<Control-n>",self.Novo)
        self.root.bind("<Control-N>",self.Novo)
        self.root.bind("<Control-o>",self.Abrir)
        self.root.bind("<Control-O>",self.Abrir)
        self.root.bind("<Control-s>",self.Salvar)
        self.root.bind("<Control-S>",self.Salvar)
        #self.root.bind("<Control-p>",self.Imprimir)
        #self.root.bind("<Control-P>",self.Imprimir)
        self.root.bind("<Control-q>",self.Sair)
        self.root.bind("<Control-Q>",self.Sair)
        # Atalhos e Evento de Tecla do Menu Editar
        self.root.bind("<Control-z>",self.Desfazer)
        self.root.bind("<Control-Z>",self.Desfazer)
        self.root.bind("<Control-y>",self.Refazer)
        self.root.bind("<Control-Y>",self.Refazer)
        self.root.bind("<Control-x>",self.Recortar)
        self.root.bind("<Control-X>",self.Recortar)
        self.root.bind("<Control-c>",self.Copiar)
        self.root.bind("<Control-C>",self.Copiar)
        self.root.bind("<Control-v>",self.Colar)
        self.root.bind("<Control-V>",self.Colar)
        self.root.bind("<Control-a>",self.SelecionarTudo)
        self.root.bind("<Control-A>",self.SelecionarTudo)
        self.root.bind("<Control-t>",self.DataHora)
        self.root.bind("<Control-T>",self.DataHora)
        pass