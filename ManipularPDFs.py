import PyPDF2
import os
from tkinter import * 
from tkinter import ttk

def mesclarPdf ():
 contador = 0
 merger = PyPDF2.PdfMerger()

#  Janela onde é inserido o caminho da pasta
#  janela_pasta = Tk()
#  pasta1 = Label(janela_pasta, text="Digite o caminho da pasta.")
#  pasta1.place(relx=0.5, rely=0.55, anchor= CENTER)

 lista_arquivos = os.listdir("PDFs")
 lista_arquivos2 = os.listdir("PDFs 2")

 numero_arquivos = len(lista_arquivos)
 numero_arquivos2 = len(lista_arquivos2)

 if numero_arquivos == numero_arquivos2 :
    
    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            arquivo2 = os.path.join(f"PDFs 2/{arquivo}")
            if os.path.exists(arquivo2):
                merger.append(f"PDFs/{arquivo}")
                merger.append (arquivo2)
                merger.write(f"Saida/{arquivo}")
                merger = PyPDF2.PdfMerger()

                # Inserindo arquivos mesclados na janela
                arquivo_da_vez.config(text = f"{arquivo} Mesclado!")

                # Adicionando barra de carregamento
                barra_carregamento = ttk.Progressbar(janela, orient=HORIZONTAL, length=300, mode= 'determinate')
                barra_carregamento.place(relx=0.5, rely=0.6, anchor= CENTER)
                barra_carregamento['maximum'] = numero_arquivos

                # Adicionando carregamento da barra
                contador = contador+1
                total_feitos = numero_arquivos - contador
                barra_carregamento['value']= contador
            else:
                arquivo_erro.config(text = f"{arquivo} não encontrado")
                contador = contador+1
                total_feitos = numero_arquivos - contador
                barra_carregamento['value']= contador
 else: 
    # Criando janela de erro
     janela_erro_pasta = Tk()   
     janela_erro_pasta.title("Quantidade de arquivos.")

     # Inserindo erros na janela
     erro_pasta = Label (janela_erro_pasta, text = "A quantidade de arquivos nas pastas não são equivalentes.")
     erro_pasta.grid(column = 0, row = 2)

     # Abrindo janela centralizada 
     # Obtem resolução da janela
     largura_janela = janela_erro_pasta.winfo_reqwidth()
     altura_janela = janela_erro_pasta.winfo_reqheight() 

     # Obtem resolução da tela
     largura_tela = janela_erro_pasta.winfo_screenwidth()
     altura_tela = janela_erro_pasta.winfo_screenheight()
     
     # Calculando centro da tela
     x = (largura_tela - largura_janela) // 2
     y = (altura_tela - altura_janela) // 2

     janela_erro_pasta.geometry(f"+{x}+{y}")

     janela_erro_pasta.mainloop()  
             
 


# Criando janela principal
janela = Tk()
janela.title("VJR PDFs")

# Maximizando janela
janela.state('zoomed')

# Adicionando imagem no icone
imagem_icone = PhotoImage(file="icone_pdf.png")
janela.iconphoto(True, imagem_icone)

#Adicionando imagem de fundo na janela principal
imagem_fundo = PhotoImage(file ="tela_fundo.png")
imagem_redimensionada = imagem_fundo.subsample(2,2)
Label_imagem = Label(janela, image=imagem_redimensionada)
Label_imagem.pack()

# Criando e adicionando titulo principal do programa
titulo_principal = Label(janela, text="Qual função você deseja executar?")
titulo_principal.place(relx=0.5, rely=0.4, anchor= CENTER)
 
# Criando e adiconando botão
botao= Button(janela, text="Mesclar PDFs", command=mesclarPdf)
botao.place(relx=0.5, rely=0.45, anchor= CENTER)

# Mostrando arquivos que estão sendo mesclados
arquivo_da_vez = Label(janela, text="")
arquivo_da_vez.place(relx=0.5, rely=0.5, anchor= CENTER)

# Mostrando arquivos que deram erro
arquivo_erro = Label(janela, text="")
arquivo_erro.place(relx=0.5, rely=0.55, anchor= CENTER)


janela.mainloop()
                


