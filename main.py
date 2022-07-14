from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import requests

# Cores
white = "#fff"
grey = "#d3d3d3"
transparent = "#0000ffff"

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('340x240')
janela.resizable(False, False)
janela.configure(bg=white)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

def cep_catch():
    cep_value = cep_input.get()

    if len(cep_value) != 8:
        messagebox.showerror("ERRO!", "CEP incorreto!")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_value))
    data_cep = request.json()
    if "erro" not in data_cep:
        label_cep_f.config(text=cep_value, font=('Arial 10'))
        label_logradouro_f.config(text="{}".format(data_cep['logradouro']))
        label_bairro_f.config(text="{}".format(data_cep['bairro']))
        label_cidade_f.config(text="{}".format(data_cep['localidade']))
    else:
        messagebox.showerror("ERRO!", "CEP inválido!")
        label_cep_f.config(text="", font=('Arial 10'))
        label_logradouro_f.config(text="", font=('Arial 10'))
        label_bairro_f.config(text="", font=('Arial 10'))
        label_cidade_f.config(text="", font=('Arial 10'))


def clean():
    label_cep_f.config(text="", font=('Arial 10'))
    label_logradouro_f.config(text="", font=('Arial 10'))
    label_bairro_f.config(text="", font=('Arial 10'))
    label_cidade_f.config(text="", font=('Arial 10'))


# Título
label_title = Label(janela, text="Consulta de CEP", relief='flat', anchor=CENTER, font=('Arial 20'), bg=white)
label_title.place(x=12, y=15)

# Campos e labels
label_cep_input = Label(janela, text="Digite o CEP:", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_cep_input.place(x=12, y=80)

cep_input = Entry(janela, relief='flat', border=1, bg=grey, width=15)
cep_input.place(x=12, y=100)

# Botão
btn_pesquisar = Button(janela, text="Pesquisar", relief='flat', border=1, borderwidth=1, font=('Arial 10'), bg=grey, command=cep_catch)
btn_pesquisar.place(x=120, y=97)

btn_limpar = Button(janela, text="Limpar", relief='flat', border=1, borderwidth=1, font=('Arial 10'), bg=grey, command=clean)
btn_limpar.place(x=200, y=97)

# CEP label
label_cep = Label(janela, text="CEP:", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_cep.place(x=12, y=140)

label_cep_f = Label(janela, text="", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_cep_f.place(x=50, y=140)

# Logradouro label
label_logradouro = Label(janela, text="Logradouro:", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_logradouro.place(x=12, y=160)

label_logradouro_f = Label(janela, text="", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_logradouro_f.place(x=90, y=160)

# Bairro label
label_bairro = Label(janela, text="Bairro:", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_bairro.place(x=12, y=180)

label_bairro_f = Label(janela, text="", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_bairro_f.place(x=60, y=180)

# Cidade label
label_cidade = Label(janela, text="Cidade:", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_cidade.place(x=12, y=200)

label_cidade_f = Label(janela, text="", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_cidade_f.place(x=70, y=200)

label_incorreto = Label(janela, text="", relief='flat', anchor=CENTER, font=('Arial 10'), bg=white)
label_incorreto.place(x=120, y=220)


janela.mainloop()
