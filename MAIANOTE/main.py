import sys,os,datetime
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

root = Tk()
global selecionado
selecionado = False

# FAVICON
# program_directory=sys.path[0]
program_directory16 = "icones/16x16/"
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory16, "favicon1.png")))
# Titulo da Janela
root.title("Maia Note - Versão 1.0")
# Tamanho da Tela
root.geometry("700x550")
root.resizable(True,True)
root.minsize(width=700,height=550)

#meu_menu = Menu(root,borderwidth=3,relief="solid",bg="#232323",fg="white")
meu_menu = Menu(root,relief="flat")
root.config(menu=meu_menu)


def fPadrao():
    pass

# <FUNÇÕES> --> MENU ARQUIVO </FUNÇÕES>
def fNovo(e):
    texto.delete("1.0","end")
    texto.focus()

def fAbrir(e):
    if texto.get(1.0,END) != "":
        texto.delete("1.0","end")
    try:
        # Seleciona um arquivo
        nomeDoArquivo = filedialog.askopenfilename(initialdir="/home/eduardo/Documentos/",title="Selecione seu arquivo",filetypes=(("Texto","*.txt"),("Shell Script","*.sh"),("Python","*.py"),("Todos os arquivos","*.*")))
        # Abre, lê e fecha arquivo de forma simplificada
        with open(nomeDoArquivo,"r",encoding='utf-8') as arq:
            #for linha in arq:
                lerArq = arq.read()
                texto.insert('0.0',lerArq)
    except:
         messagebox.showinfo(title="mensagem",message="Selecione um arquivo para abrir")

def fSalvar(e):
    # Salvar um arquivo
    nomeDoArquivo = filedialog.asksaveasfile(initialdir="/home/eduardo/Documentos/",title="Salve seu arquivo",filetypes=(("Texto","*.txt"),("Shell Script","*.sh"),("Python","*.py"),("Todos os arquivos","*.*")))
    arquivo = str(texto.get(1.0,END))
    nomeDoArquivo.write(arquivo)
    nomeDoArquivo.close()

def fImprimir(e):
    print("Imprimir")

def fFechar(e):
    root.quit()

# <FUNÇÕES> --> MENU EDITAR </FUNÇÕES>
def fDesfazer():
    try:
        texto.edit_undo()
    except:
         messagebox.showinfo(title="mensagem",message="Você precisa ter escrito pelo menos uma palavra")

def fRefazer():
    try:
       texto.edit_redo()
       root.clipboard_clear()
    except:
         messagebox.showinfo(title="mensagem",message="Você precisa ter desfeito pelo menos uma palavra")

def fRecortar(e):
    global selecionado
    try:
        # Checa se atalho foi usado
        if e:
            selecionado = root.clipboard_get()
        else:
            if texto.selection_get():
                selecionado = texto.selection_get()
                texto.delete("sel.first","sel.last")
                root.clipboard_clear()
                root.clipboard_append(selecionado)
    except:
         messagebox.showinfo(title="mensagem",message="Você precisa ter selecionado pelo menos uma palavra")

def fCopiar(e):
    global selecionado
    try:
        # Checa se atalho foi usado
        if e:
            selecionado = root.clipboard_get()
        if texto.selection_get():
            selecionado = texto.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selecionado)
    except:
        messagebox.showinfo(title="mensagem",message="Você precisa ter selecionado pelo menos uma palavra")

def fColar(e):
    global selecionado
    try:
    # Checa se atalho foi usado
        if e:
            selecionado = root.clipboard_get()
        else:
            if selecionado:
                posicao = texto.index(INSERT)
                texto.insert(posicao,selecionado)
    except:
        messagebox.showinfo(title="mensagem",message="Recorte ou copie pelo menos uma palavra para colar")

def fSelecionarTudo(e):
    texto.tag_add("sel","1.0",END)

def fDataHora(e):
    # Pega a data e hora atual BR
    dataEhora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    # Pega a posição do cursor
    posicao = texto.index(INSERT)
    # Insere data e hora na posição do cursor
    texto.insert(posicao,dataEhora)


# <FUNÇÕES> --> MENU FORMATAR fEscolherFonte </FUNÇÕES>

def fEscolherCor(valor):
    global selecionado
    try:

        if valor == 1:
            if texto.selection_get():
                selecionado = texto.selection_get()
                cor = colorchooser.askcolor()
                corHexadecimal = cor[1].upper()
                if selecionado:
                    texto.tag_configure(str(selecionado), foreground=str(corHexadecimal))
                    #colore a ultima palavra
                    texto.tag_add(str(selecionado), "sel.first","sel.last")
                    #texto.tag_add(str(selecionado), 'insert-2c wordstart', 'end-2c')

        if valor == 2:
            if texto.selection_get():
                selecionado = texto.selection_get()
                cor = colorchooser.askcolor()
                corHexadecimal = cor[1].upper()
                if selecionado:
                    texto.tag_configure(str(selecionado), background=str(corHexadecimal))
                    #colore a ultima palavra
                    texto.tag_add(str(selecionado), "sel.first","sel.last")
                    #texto.tag_add(str(selecionado), 'insert-2c wordstart', 'end-2c')

    except:
           messagebox.showinfo(title="mensagem",message="Selecione o texto primeiro")

    if valor == 3:
        cor = colorchooser.askcolor()
        corHexadecimal = cor[1].upper()
        texto['bg'] = corHexadecimal

    if valor == 4:
        cor = colorchooser.askcolor()
        corHexadecimal = cor[1].upper()
        texto['fg'] = corHexadecimal



# <FUNÇÕES> --> MENU AJUDA </FUNÇÕES>
def fAjuda():
    messagebox.showinfo(title="Ajuda",message="Este programa é simples como o bloco de notas do Windows ou com o Leaftpad do linux")

def fSobre():
    messagebox.showinfo(title="Sobre",message="Simples editor de texto feito em Python3 e Tkinter")

# IMAGENS CARREGADAS NO MENU ARQUIVO
imgNovo = PhotoImage(file="icones/16x16/novo.png")
imgAbrir = PhotoImage(file="icones/16x16/abrir.png")
imgSalvar = PhotoImage(file="icones/16x16/salvar.png")
imgImprimir = PhotoImage(file="icones/16x16/imprimir.png")
imgFechar = PhotoImage(file="icones/16x16/fechar.png")

# Menu Arquivo
file_menu = Menu(meu_menu,tearoff=0)
meu_menu.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Novo", command=lambda:fNovo(False), image=imgNovo, compound=LEFT, accelerator="Ctrl+N")
file_menu.add_command(label="Abrir", command=lambda:fAbrir(False), image=imgAbrir, compound=LEFT, accelerator="Ctrl+O")
file_menu.add_command(label="Salvar", command=lambda:fSalvar(False), image=imgSalvar, compound=LEFT, accelerator="Ctrl+S")
file_menu.add_command(label="Imprimir", command=lambda:fImprimir(False), image=imgImprimir, compound=LEFT, accelerator="Ctrl+P")
file_menu.add_command(label="Fechar", command=lambda:fFechar(False), image=imgFechar, compound=LEFT, accelerator="Esc")


# IMAGENS CARREGADAS NO MENU EDITAR
imgDesfazer = PhotoImage(file="icones/16x16/desfazer.png")
imgRefazer = PhotoImage(file="icones/16x16/refazer.png")
imgRecortar = PhotoImage(file="icones/16x16/recortar.png")
imgCopiar = PhotoImage(file="icones/16x16/copiar.png")
imgColar = PhotoImage(file="icones/16x16/colar.png")
imgSelectALL = PhotoImage(file="icones/16x16/select_all.png")
imgDataHora = PhotoImage(file="icones/16x16/data_hora.png")

# Menu Editar
edit_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Desfazer", command=fDesfazer, image=imgDesfazer, compound=LEFT, accelerator="Ctrl+Z")
edit_menu.add_command(label="Refazer", command=fRefazer, image=imgRefazer, compound=LEFT)
edit_menu.add_command(label="Recortar", command=lambda:fRecortar(False), image=imgRecortar, compound=LEFT, accelerator="Ctrl+X")
edit_menu.add_command(label="Copiar", command=lambda:fCopiar(False), image=imgCopiar, compound=LEFT, accelerator="Ctrl+C")
edit_menu.add_command(label="Colar", command=lambda:fColar(False), image=imgColar, compound=LEFT, accelerator="Ctrl+V")
edit_menu.add_command(label="Selecionar Tudo", command=lambda:fSelecionarTudo(False), image=imgSelectALL, compound=LEFT, accelerator="Ctrl+A")
edit_menu.add_command(label="Inserir Data e Hora", command=lambda:fDataHora(False), image=imgDataHora, compound=LEFT,accelerator="F6")

# IMAGENS CARREGADAS NO MENU FORMATAR
imgFonte = PhotoImage(file="icones/16x16/fonte.png")

# Menu Formatar
formatar_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label="Formatar", menu=formatar_menu)
formatar_menu.add_command(label="Cor do Texto", command=lambda:fEscolherCor(1), image=imgFonte, compound=LEFT)
formatar_menu.add_command(label="Marca Texto", command=lambda:fEscolherCor(2), image=imgFonte, compound=LEFT)
formatar_menu.add_command(label="Cor de Fundo da Folha", command=lambda:fEscolherCor(3), image=imgFonte, compound=LEFT)
formatar_menu.add_command(label="Cor Padrão do Texto da Folha", command=lambda:fEscolherCor(4), image=imgFonte, compound=LEFT)


# IMAGENS CARREGADAS NO MENU AJUDA
imgAjuda = PhotoImage(file="icones/16x16/ajuda.png")
imgSobre = PhotoImage(file="icones/16x16/sobre.png")

# Menu Ajuda
ajuda_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label="Ajuda", menu=ajuda_menu)
ajuda_menu.add_command(label="Ajuda", command=fAjuda, image=imgAjuda, compound=LEFT)
ajuda_menu.add_command(label="Sobre", command=fSobre, image=imgSobre, compound=LEFT)

#frame = Frame(root,borderwidth=1,relief="solid")
#frame = Frame(root,width=640,highlightbackground='blue',highlightthicknes=3)

caixaTexto = Frame(root)

caixaTexto.place(relx=0.01,rely=0,relwidth=0.98,relheight=0.98)
#texto = Text(caixaTexto).place(relx=0,rely=0,relwidth=1,relheight=1)

scrollbar = Scrollbar(caixaTexto)
scrollbar.pack(side=RIGHT,fill=Y)

texto = Text(caixaTexto,yscrollcommand=scrollbar.set,undo=True)
texto.pack(side=LEFT,fill=BOTH,expand=1)
scrollbar.config(command=texto.yview)

# Atalhos e Evento de Tecla do Menu Arquivos
root.bind("<Control-n>",fNovo)
root.bind("<Control-N>",fNovo)
root.bind("<Control-o>",fAbrir)
root.bind("<Control-O>",fAbrir)
root.bind("<Control-s>",fSalvar)
root.bind("<Control-S>",fSalvar)
root.bind("<Control-p>",fImprimir)
root.bind("<Control-P>",fImprimir)
root.bind("<Escape>",fFechar)


# Atalhos e Evento de Tecla do Menu Editar
root.bind("<Control-x>",fRecortar)
root.bind("<Control-X>",fRecortar)
root.bind("<Control-c>",fCopiar)
root.bind("<Control-C>",fCopiar)
root.bind("<Control-v>",fColar)
root.bind("<Control-V>",fColar)
root.bind("<Control-a>",fSelecionarTudo)
root.bind("<Control-A>",fSelecionarTudo)
root.bind("<F6>",fDataHora)
# JANELA EM UPDATE
root.mainloop()
