import sys
import pandas as pd
import newspaper as ns
from newspaper import Article
from tkinter import *



data = pd.read_csv("https://www.dropbox.com/s/onljwyx84aknd0y/base_art%C3%ADculos.csv?dl=1", encoding='utf-8')

def cargar_base():
    try:
        b=1
        data = pd.read_csv("https://www.dropbox.com/s/azptqcv2h6ae7lt/Acualizar_base.csv?dl=1", encoding='latin-1')
        L=data["URL"]
        while b>0:
            LL=[]
            for i in L:
                article = Article(i)
                article.download()
                article.parse()
                x=article.text
                LL+= [x]
            s=pd.DataFrame(LL)
            s.rename(columns={0:"Texto"}, inplace=True)
            data=pd.concat([data,s],axis=1)  
            #data=data.drop(["ID"], axis=1)
            a=data
            data = pd.read_csv("https://www.dropbox.com/s/onljwyx84aknd0y/base_art%C3%ADculos.csv?dl=1", encoding='utf-8')
            data=data.append(a, ignore_index=True)
            data['Fecha'] =pd.to_datetime(data.Fecha)
            data=data.sort_values(by='Fecha', ascending=False)
            try:
                data.to_csv('/Users/marianaaviles/Dropbox/scraper/base_artículos.csv', index=False, encoding='utf-8-sig')
            except:
                data.to_csv('C:/Users/aleja/Dropbox/scraper/base_artículos.csv', index=False, encoding='utf-8-sig')
            b=0
            mlabel2=Label(mGui,text="Base actualizada, ahora cierre y vuelva a abrir el programa",fg="green", font=20).pack()
    except:
        mlabel2=Label(mGui,text="Error, intente de nuevo",fg="red", font=20).pack()
    return








def dar_enter():
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)
    mask=(data.apply(lambda row: row.astype(str).str.contains(ment.get()).any(), axis=1))
    L=data[mask]
    L=L.loc[:,["URL"]]
 #   LL=[]
    T.insert(END, "                ")
    T.insert(END, "#######################################################################")
#    T.listbox.itemconfigure(END, bg="#00aa00", fg="#fff")
    T.insert(END, L)
    
    return




mGui = Tk ()
ment = StringVar()
mGui.geometry('1200x550+300+300')
mGui.title("Programa de búsqueda de artículos")
#mlabel= Label(mGui,text="Cargar base antes de usar").pack()
mbutton=Button(mGui,text="Actualizar Base",command=cargar_base,fg="white",bg="green").pack()
#Button(mGui, text="Cargar/Limpiar", command=restart_program).pack()
mlabel= Label(mGui,text="Insertar Palabra").pack()
mEntry =Entry(mGui,textvariable=ment).pack()
mbutton=Button(mGui,text="Buscar",command=dar_enter,fg="white",bg="green").pack()
S = Scrollbar(mGui)
T = Text(mGui, height=25, width=140)
S.pack(side=RIGHT, fill=Y)
T.pack(side=TOP, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.pack()

