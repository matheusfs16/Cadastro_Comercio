import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from CTkTreeview import CTkTreeview



def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn =  conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
              
              telefone  TEXT,
              nome TEXT,
              email TEXT,
              endereco TEXT
              )   
              ''')
    conn.commit()
    conn.close() 
   

def inserir_usuario():
    telefone_ = telefone.get()
    nome_= nome.get()
    email_ = email.get()
    endereco_ = endereco.get()

    if telefone_ and nome_ and email_:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios VALUES (?,?,?,?)',(telefone_,nome_,email_,endereco_))

        conn.commit()
        conn.close()
        messagebox.showinfo('','DADOS INSERIDOS COM SUCESSO!')
    else:
        messagebox.showwarning('','INSIRA TODOS OS DADOS SOLICITADOS')

    con = conectar()
    c = con.cursor()
    con.commit()
    con.close()
    mostrar_usuario()

def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
        
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    user = c.fetchall()

    for us in user:
        tree.insert('','end',values= (us[1],us[2],us[0],us[3]))
    conn.close()

def atualizar():
    selecao = tree.selection()
    if selecao:
        dado_edit =tree.item(selecao)['values'][3]
        novo_telefone = telefone.get()
        novo_nome = nome.get()
        novo_email = email.get()
        novo_endereco = endereco.get()

        if novo_telefone and novo_nome and novo_email and novo_endereco:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE usuarios SET  nome =?, email =?, telefone =?, endereco =? WHERE endereco =?',(novo_nome,novo_email,novo_telefone,novo_endereco,dado_edit))

            conn.commit()
            conn.close()
            mostrar_usuario()
            messagebox.showinfo('','DADOS ATUALIZADOS COM SUCESSO!')
        else:
            messagebox.showwarning('','TODOS DADOS PRECISAM ESTAR PREENCHIDOS')

        con = conectar()
        c = con.cursor()
        con.commit()
        con.close()



def delete_usuario():
    selecao = tree.selection()
    if selecao:
        user_del = tree.item(selecao)['values'][2]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE telefone = ?',(user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo("","DADO DELETADO COM SUCESSO")
        mostrar_usuario()
    else:
        messagebox.showerror("",'ERRO AO DELETAR O DADO')


# INTERFACE

root = ctk.CTk()
root.geometry('830x1750')
root.title('CADASTRO XYZ')
caminho =('icone.ico')
root.iconbitmap(caminho)
ctk.set_appearance_mode('dark')

ctk.CTkLabel(root, text="CADASTRO XYZ", font= ('arial', 15)).grid(column=0, row=0,padx=10)

# DADOS

fr0 =  ctk.CTkFrame(root)

fr0.grid()

nome_lb = ctk.CTkLabel(fr0, text="Nome:", font= ('arial', 15))
nome_lb.grid(column=0, row=1,padx=10,pady=10)

email_lb = ctk.CTkLabel(fr0, text="E-mail:", font= ('arial', 15))
email_lb.grid(column=0, row=2,padx=10,pady=10)

telefone_lb = ctk.CTkLabel(fr0, text="Telefone:", font= ('arial', 15))
telefone_lb.grid(column=0, row=3,padx=10,pady=10)

endereco_lb = ctk.CTkLabel(fr0, text="Endereço:", font= ('arial', 15))
endereco_lb.grid(column=0, row=4,padx=10,pady=10)

nome = ctk.CTkEntry(fr0,font=('arial',15),placeholder_text='Nome')
nome.grid(column=1, row=1,padx=10,pady=10)

email = ctk.CTkEntry(fr0,font=('arial',15),placeholder_text='E-mail')
email.grid(column=1, row=2,padx=10,pady=10)

telefone = ctk.CTkEntry(fr0,font=('arial',15),placeholder_text='Telefone')
telefone.grid(column=1, row=3,padx=10,pady=10)

endereco = ctk.CTkEntry(fr0,font=('arial',15),placeholder_text='Endereço')
endereco.grid(column=1, row=4,padx=10,pady=10)

# BOTÕES E FRAME DELES

fr = ctk.CTkLabel(root,text='')
fr.grid(padx=10, columnspan=2)


btn_salvar = ctk.CTkButton(fr,text='CADASTRAR',font=('arial',15), command=inserir_usuario)
btn_salvar.grid(row=6, column=0,padx=10,pady=10)

btn_att = ctk.CTkButton(fr,text='ATUALIZAR',font=('arial',15),command=atualizar)
btn_att.grid(row=6, column=2,padx=10,pady=10)

btn_delete = ctk.CTkButton(fr,text='DELETAR',font=('arial',15),command=delete_usuario)
btn_delete.grid(row=6, column=3,padx=10,pady=10)

# TREE VIEW

fr2 =  ctk.CTkLabel(root, text='')
fr2.grid(pady=20, sticky="nsew")

colunas = ( 'NOME', 'E-MAIL','TELEFONE','ENDEREÇO')
tree =  CTkTreeview(fr2, columns=colunas, show='headings', height=18,)


tree.grid(row=0, column=0, sticky='nsew')
x =ctk.CTkScrollbar(fr2,orientation='vertical',command=tree.yview)
x.grid(row=0, column=1,sticky='ns')
# ----------------

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#1a1a1a",
    fieldbackground="#1a1a1a",
    foreground="white",
    rowheight=25,
    bordercolor="#333333",
    borderwidth=1
)
style.configure(
    "Treeview.Heading",
    background="#2b2b2b",
    foreground="white"
)


with tree.columns() as tc:
    tc.minwidth("NOME", 150)
    tc.minwidth("E-MAIL", 150)
    tc.minwidth("TELEFONE", 150)
    tc.anchor("ENDEREÇO", "e")


for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor= tk.CENTER)


criar_tabela()
mostrar_usuario()

root.mainloop()
