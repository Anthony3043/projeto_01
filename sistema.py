import customtkinter
from tkinter import ttk
import sqlite3
import tkinter as tk


# def abrir cadastro
def abrir_cadastro():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_cadastrar.grid_propagate(False)
    frame_cadastrar.grid(row=0, column=1, padx=10)


def criar_banco_cadastrar():
    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute(
        "CREATE TABLE IF NOT EXISTS produtos (nome text, preco decimal, descricao text, quantidade decimal)")
    conexao.commit()
    conexao.close()


def salvar_dados_cadastro():
    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute(
        f"INSERT INTO produtos (nome, preco, descricao) VALUES ('{busca_produto_cadastrar.get()}','{float(preço_produto_cadastrar.get())}', '{descriçao_produto_cadastrar.get('1.0', 'end')}')")
    busca_produto_cadastrar.delete(0, 'end')
    preço_produto_cadastrar.delete(0, 'end')
    descriçao_produto_cadastrar.delete(1.0, 'end')
    conexao.commit()
    conexao.close()


def ler_dados_relatorio():
    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute("SELECT * FROM produtos")
    recebe_dados = produto_sql.fetchall()
    for item in trivel_relatorio_estoque.get_children():
        trivel_relatorio_estoque.delete(item)

    for i in recebe_dados:
        nome = str(i[0])
        quantidade = 0
        preco = float(i[1])
        desc = str(i[2])
        trivel_relatorio_estoque.insert('', tk.END, values=(nome, quantidade, preco, desc))
    conexao.close()


def ler_relatorio_editar():

    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute("SELECT nome FROM produtos")
    recebe_dados = produto_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in lista_produtos_editar.winfo_children():
        item.destroy()
    check_var = customtkinter.StringVar()

    for item in recebe_dados:
        nome = str(item[0])
        itens = []
        itens.append(nome)

        for item in itens:
            label_edicao_dados.configure(text=item)
            box_editar = customtkinter.CTkCheckBox(lista_produtos_editar, text=item, command=lambda: checkbox_editar(check_var) if check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box_editar.pack(pady=5, padx=10)
    conexao.close()


def ler_relatorio_saida():

    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute("SELECT nome FROM produtos")
    recebe_dados = produto_sql.fetchall()
    for item in lista_produtos_saida.winfo_children():
        item.destroy()
    check_var = customtkinter.StringVar()

    for item in recebe_dados:
        nome = str(item[0])
        itens = []
        itens.append(nome)
        for item in itens:
            label_saida_dados.configure(text=item)
            box_saida = customtkinter.CTkCheckBox(lista_produtos_saida, text=item, command=lambda: checkbox_editar(check_var), variable=check_var, onvalue=item, offvalue="")
            box_saida.pack(pady=5, padx=10)

    conexao.close()

def checkbox_editar(argumento):
    valor_box_editar = argumento.get()
    print(valor_box_editar)
    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute(f"SELECT * FROM produtos WHERE nome = '{valor_box_editar}'")
    recebe_dados = produto_sql.fetchall()

    buscar_produto_editar.delete(0, 'end')
    preço_produto_editar.delete(0, 'end')
    descrição_produto_editar.delete(0, 'end')

    qtd_saida.delete(0, 'end')

    descrição_produto_editar.delete(0, 'end')

    print(recebe_dados)

    buscar_produto_editar.insert(0, recebe_dados[0][0])
    preço_produto_editar.insert(0, recebe_dados[0][1])
    descrição_produto_editar.insert(0, recebe_dados[0][2])

    qtd_saida.insert(0, recebe_dados[0][0])

    qtd_entrada.insert(0, recebe_dados[0][0])


def ler_relatorio_entrada():
    global recebe_dados, check_var
    conexao = sqlite3.connect("dados_estoque.db")
    produto_sql = conexao.cursor()
    produto_sql.execute("SELECT nome FROM produtos")
    recebe_dados = produto_sql.fetchall()
    for item in lista_produtos_entradas.winfo_children():
        item.destroy()

    for item in recebe_dados:
        nome = str(item[0])
        itens = []
        itens.append(nome)

        for item in itens:
            label_edicao_dados.configure(text=item)
            box_entrada = customtkinter.CTkCheckBox(lista_produtos_entradas, text=item)
            box_entrada.pack(pady=5, padx=10)

        for item in itens:
            label_edicao_dados.configure(text=item)
            box_saida = customtkinter.CTkCheckBox(lista_produtos_saida, text=item)
            box_saida.pack(pady=5, padx=10)

    conexao.close()


# criaçao do banco_______________________________________________________________________________________________________
criar_banco_cadastrar()


# def abrir editar_______________________________________________________________________________________________________
def abrir_editar():
    frame_cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_editar.grid_propagate(False)
    frame_editar.grid(row=0, column=1, padx=10)
    ler_relatorio_editar()


# def abrir saida_______________________________________________________________________________________________________
def abrir_saida():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_saida.grid_propagate(False)
    frame_saida.grid(row=0, column=1, padx=10)
    ler_relatorio_saida()


# def abrir entrada_____________________________________________________________________________________________________
def abrir_entrada():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_entrada.grid_propagate(False)
    frame_entrada.grid(row=0, column=1, padx=10)
    ler_relatorio_entrada()


# def abrir relatório___________________________________________________________________________________________________
def abrir_relatorio():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_estoque.grid_propagate(False)
    frame_relatorio_estoque.grid(row=0, column=1, padx=10)
    ler_dados_relatorio()


# def abrir relatorio saida_____________________________________________________________________________________________
def abrir_relatorio_saida():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_propagate(False)
    frame_relatorio_saida.grid(row=0, column=1, padx=10)


# entrada_______________________________________________________________________________________________________________
def abrir_relatorio_entrada():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_propagate(False)
    frame_relatorio_entrada.grid(row=0, column=1, padx=10)


# criação do pop-up_____________________________________________________________________________________________________
def abrir_pop_up():
    customtkinter.set_appearance_mode("dark")
    pop_up = customtkinter.CTk()
    pop_up.geometry("470x400")
    pop_up.title("pop_up")

    # criação das funções do pop-up_________________________________________________________________________________________
    impressao = customtkinter.CTkLabel(pop_up, text="Impressora", font=("Open sans", 30, "bold"))
    impressao.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")

    escolher_relatorio = customtkinter.CTkLabel(pop_up, text="Escolher relatório", font=("Open sans", 20, "bold"))
    escolher_relatorio.grid(row=1, column=0, padx=5, pady=30, sticky="w")

    exportar_estoque = customtkinter.CTkCheckBox(pop_up, text="exportar estoque")
    exportar_estoque.grid(row=2, column=0, padx=5, pady=20, sticky="w")

    exportar_saida = customtkinter.CTkCheckBox(pop_up, text="exportar saída")
    exportar_saida.grid(row=3, column=0, padx=5, pady=20, sticky="w")

    exportar_entrada = customtkinter.CTkCheckBox(pop_up, text="exportar entrada")
    exportar_entrada.grid(row=4, column=0, padx=5, pady=20, sticky="w")

    escolher_extensao = customtkinter.CTkLabel(pop_up, text="Escolher extensão", font=("Open sans", 20, "bold"))
    escolher_extensao.grid(row=1, column=1, padx=50, pady=30, sticky="w")

    word = customtkinter.CTkCheckBox(pop_up, text="Word")
    word.grid(row=2, column=1, padx=50, pady=20, sticky="w")

    PDF = customtkinter.CTkCheckBox(pop_up, text="PDF")
    PDF.grid(row=3, column=1, padx=50, pady=20, sticky="w")

    excel = customtkinter.CTkCheckBox(pop_up, text="Excel")
    excel.grid(row=4, column=1, padx=50, pady=20, sticky="w")

    # criação dos botões do pop-up__________________________________________________________________________________________
    pop_up_salvar = customtkinter.CTkButton(pop_up, text="salvar", fg_color="green", width=90, height=30)
    pop_up_salvar.grid(row=5, column=1, padx=5, pady=20, sticky="e")

    pop_up_cancelar = customtkinter.CTkButton(pop_up, text="cancelar", fg_color="red", width=90, height=30)
    pop_up_cancelar.grid(row=5, column=1, padx=70, pady=20, sticky="w")

    pop_up.mainloop()


# criação da função de deletar__________________________________________________________________________________________
def deletar_item(index):
    items_entrada.pop(index)
    atualizar()


def atualizar():
    for botaozinho in lista_excluir_produtos_saida.winfo_children():
        botaozinho.destroy()

    for botaozinho in lista_excluir_produtos_entrada.winfo_children():
        botaozinho.destroy()

    # Enumerador para escolher o item_______________________________________________________________________________________
    for i, item in enumerate(items_entrada):
        box = customtkinter.CTkCheckBox(lista_excluir_produtos_saida, text=item)
        box.grid(row=i, column=0, pady=5, padx=10, sticky="w")
        deletar_botao = customtkinter.CTkButton(lista_excluir_produtos_saida, text="🗑", fg_color="red", width=40,
                                                command=lambda index=i: deletar_item(index))
        deletar_botao.grid(row=i, column=1, padx=10, pady=5)

        for i, item in enumerate(items_entrada):
            box = customtkinter.CTkCheckBox(lista_excluir_produtos_entrada, text=item)
            box.grid(row=i, column=0, pady=5, padx=10, sticky="w")
            deletar_botao = customtkinter.CTkButton(lista_excluir_produtos_entrada, text="🗑", fg_color="red", width=40,
                                                    command=lambda index=i: deletar_item(index))
            deletar_botao.grid(row=i, column=1, padx=10, pady=5)


# criação da janela_____________________________________________________________________________________________________

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Sistema de Cadastro")
janela.geometry("800x400")

# Criação dos frames____________________________________________________________________________________________________
frame_menu = customtkinter.CTkFrame(janela, width=190, height=400, corner_radius=30, border_width=2,
                                    border_color='#aa00ff')
frame_menu.pack_propagate(False)
frame_menu.grid(row=0, column=0)

frame_cadastrar = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                         border_color='#aa00ff')
frame_cadastrar.grid_propagate(False)
frame_cadastrar.grid(row=0, column=1, padx=10)

frame_editar = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                      border_color='#aa00ff')
frame_editar.grid_propagate(False)

frame_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                     border_color='#aa00ff')
frame_saida.grid_propagate(False)

frame_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                       border_color='#aa00ff')
frame_entrada.grid_propagate(False)

frame_relatorio_estoque = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                                 border_color='#aa00ff')
frame_relatorio_estoque.grid_propagate(False)

frame_relatorio_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                                 border_color='#aa00ff')
frame_relatorio_entrada.grid_propagate(False)

frame_relatorio_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=30, border_width=1,
                                               border_color='#aa00ff')
frame_relatorio_saida.grid_propagate(False)

# criação do menu_______________________________________________________________________________________________________
titulo_menu = customtkinter.CTkLabel(frame_menu, text="Menu", font=('Courier', 40, 'bold'))
titulo_menu.pack(pady=10)

botao_cadastrar = customtkinter.CTkButton(frame_menu, text="Cadastrar", fg_color='#aa00ff', command=abrir_cadastro)
botao_cadastrar.pack(pady=5)

botao_editar = customtkinter.CTkButton(frame_menu, text="Editar", fg_color='#aa00ff', command=abrir_editar)
botao_editar.pack(pady=5)

botao_saida = customtkinter.CTkButton(frame_menu, text="Saída", fg_color='#aa00ff', command=abrir_saida)
botao_saida.pack(pady=5)

botao_entrada = customtkinter.CTkButton(frame_menu, text="Entrada", fg_color='#aa00ff', command=abrir_entrada)
botao_entrada.pack(pady=5)

botao_relatorio = customtkinter.CTkButton(frame_menu, text="Relatório", fg_color='#aa00ff', command=abrir_relatorio)
botao_relatorio.pack(pady=5)

# Tela de cadastro______________________________________________________________________________________________________

titulo_cadastrar = customtkinter.CTkLabel(frame_cadastrar, text="Cadastro do Produto", font=("Arial", 30),
                                          text_color="white")
titulo_cadastrar.grid(row=0, column=1, pady=30)

produto_cadastrar = customtkinter.CTkLabel(frame_cadastrar, text="Nome do Produto:", text_color="white")
produto_cadastrar.grid(row=1, column=0, padx=10)

produto_descrição_cadastrar = customtkinter.CTkLabel(frame_cadastrar, text="Descrição:", text_color="white")
produto_descrição_cadastrar.grid(row=3, column=0, padx=10, sticky="ne")

busca_produto_cadastrar = customtkinter.CTkEntry(frame_cadastrar, placeholder_text="Digite o nome do produto:",
                                                 width=300)
busca_produto_cadastrar.grid(row=1, column=1, pady=5, padx=10)

preço_produto_cadastrar = customtkinter.CTkEntry(frame_cadastrar, placeholder_text="0.00:", width=80)
preço_produto_cadastrar.grid(row=2, column=1, pady=5, padx=10, sticky="w")

descriçao_produto_cadastrar = customtkinter.CTkTextbox(frame_cadastrar, width=300, height=80)
descriçao_produto_cadastrar.grid(row=3, column=1, pady=5, padx=10, sticky="ne")

botao_salvar_cadastrar = customtkinter.CTkButton(frame_cadastrar, text="Salvar", fg_color='#aa00ff',
                                                 command=salvar_dados_cadastro)
botao_salvar_cadastrar.grid(row=4, column=1, pady=5, padx=10, sticky="e")

# Editar________________________________________________________________________________________________________________

titulo_editar = customtkinter.CTkLabel(frame_editar, text="Editar Produto Cadastrado", font=("Arial", 30),
                                       text_color="white")
titulo_editar.grid(row=0, column=0, pady=30, sticky="we", columnspan=2)

label_edicao_dados = customtkinter.CTkLabel(frame_editar)

lista_produtos_editar = customtkinter.CTkScrollableFrame(frame_editar)
lista_produtos_editar.grid(pady=5, padx=20, sticky="we", row=2, column=0, rowspan=5)

buscar_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="Buscar Produto:", width=300)
buscar_editar.grid(row=1, column=0, pady=5, padx=10, sticky="w", columnspan=2)

buscar_produto_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="Nome do Produto:", width=300)
buscar_produto_editar.grid(row=3, column=1, pady=5, padx=10, sticky="w")

preço_produto_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="0.00:", width=80)
preço_produto_editar.grid(row=4, column=1, pady=5, padx=10, sticky="w")

descrição_produto_editar = customtkinter.CTkEntry(frame_editar, width=300, height=100)
descrição_produto_editar.grid(row=5, column=1, pady=5, padx=10, sticky="w")

botao_excluir_editar = customtkinter.CTkButton(frame_editar, text="Excluir", fg_color='#aa00ff', width=80)
botao_excluir_editar.grid(row=6, column=1, pady=5, padx=10, sticky="w")

botao_cancelar_editar = customtkinter.CTkButton(frame_editar, text="Cancelar", fg_color='#aa00ff', width=80)
botao_cancelar_editar.grid(row=6, column=1, pady=5, padx=10)

botao_salvar_editar = customtkinter.CTkButton(frame_editar, text="Salvar", fg_color='#aa00ff', width=80)
botao_salvar_editar.grid(row=6, column=1, pady=5, padx=10, sticky="e")

# Saida_________________________________________________________________________________________________________________
titulo_saida = customtkinter.CTkLabel(frame_saida, text="Saída Produto:", font=("Arial", 30), text_color="white")
titulo_saida.grid(row=0, column=0, pady=20, padx=200, sticky="w")

lista_produtos_saida = customtkinter.CTkScrollableFrame(frame_saida)
lista_produtos_saida.grid(pady=5, padx=20, sticky="w", row=2, column=0, rowspan=5)

label_saida_dados = customtkinter.CTkLabel(frame_saida)

buscar_items_saida = []

qtd_saida = customtkinter.CTkEntry(frame_saida, placeholder_text="quantidades de items no estoque", width=280)
qtd_saida.grid(pady=5, padx=290, row=1, column=0, sticky="w")

botao_adicionar_saida = customtkinter.CTkButton(frame_saida, text='adicionar item', width=120, fg_color="green", )
botao_adicionar_saida.grid(pady=1, padx=450, row=2, column=0, sticky="w", columnspan=2)

busca_produto_saida = customtkinter.CTkEntry(frame_saida, placeholder_text="Campo de Busca:", width=225)
busca_produto_saida.grid(row=1, column=0, pady=2, padx=20, sticky="w", columnspan=2)

busca_estoque_saida = customtkinter.CTkEntry(frame_saida, placeholder_text="", width=140)
busca_estoque_saida.grid(pady=1, padx=290, row=2, column=0, sticky="w", columnspan=2)

lista_excluir_produtos_saida = customtkinter.CTkScrollableFrame(frame_saida, width=260)
lista_excluir_produtos_saida.grid(row=3, column=0, pady=1, padx=290, sticky="w")

items_saida = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7", "Produto 8"]
for item in items_saida:

    box_excluir_saida = customtkinter.CTkCheckBox(lista_excluir_produtos_saida, text=item)
    box_excluir_saida.pack(pady=5, padx=10)

botao_cancelar_saida = customtkinter.CTkButton(frame_saida, text="Cancelar", width=80, fg_color="red")
botao_cancelar_saida.grid(row=4, column=0, pady=5, padx=290, sticky="w")

botao_salvar_saida = customtkinter.CTkButton(frame_saida, text="Salvar", width=80, fg_color="green")
botao_salvar_saida.grid(row=4, column=0, pady=5, padx=490, sticky="e")

# Entrada_______________________________________________________________________________________________________________
titulo_entrada = customtkinter.CTkLabel(frame_entrada, text="Entrada Produto:", font=("Arial", 30), text_color="white")
titulo_entrada.grid(row=0, column=0, pady=20, padx=200, sticky="w")

lista_produtos_entradas = customtkinter.CTkScrollableFrame(frame_entrada)
lista_produtos_entradas.grid(pady=5, padx=20, sticky="w", row=2, column=0, rowspan=5)

label_entrada_dados = customtkinter.CTkLabel(frame_entrada)

buscar_items_entradas = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7",
                         "Produto 8"]
for item in buscar_items_saida:
    box_entrada = customtkinter.CTkCheckBox(lista_produtos_entradas, text=item)
    box_entrada.pack(pady=5, padx=10)

qtd_entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="quantidades de items no estoque", width=280)
qtd_entrada.grid(pady=5, padx=290, row=1, column=0, sticky="w")

botao_adicionar_entrada = customtkinter.CTkButton(frame_entrada, text='adicionar item', width=120, fg_color="green", )
botao_adicionar_entrada.grid(pady=1, padx=450, row=2, column=0, sticky="w", columnspan=2)

busca_produto_entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="Campo de Busca:", width=225)
busca_produto_entrada.grid(row=1, column=0, pady=2, padx=20, sticky="w", columnspan=2)

busca_estoque_entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="", width=140)
busca_estoque_entrada.grid(pady=1, padx=290, row=2, column=0, sticky="w", columnspan=2)

lista_excluir_produtos_entrada = customtkinter.CTkScrollableFrame(frame_entrada, width=260)
lista_excluir_produtos_entrada.grid(row=3, column=0, pady=1, padx=290, sticky="w")

items_entrada = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7", "Produto 8"]
for item in items_saida:
    box_excluir_entrada = customtkinter.CTkCheckBox(lista_excluir_produtos_entrada, text=item)
    box_excluir_entrada.pack(pady=5, padx=10)

botao_cancelar_entrada = customtkinter.CTkButton(frame_entrada, text="Cancelar", width=80, fg_color="red")
botao_cancelar_entrada.grid(row=4, column=0, pady=5, padx=290, sticky="w")

botao_salvar_entrada = customtkinter.CTkButton(frame_entrada, text="Salvar", width=80, fg_color="green")
botao_salvar_entrada.grid(row=4, column=0, pady=5, padx=490, sticky="e")

# Relatório de estoque__________________________________________________________________________________________________
titulo_estoque = customtkinter.CTkLabel(frame_relatorio_estoque, text="Relatório de estoque", font=("Arial", 30))
titulo_estoque.grid(row=0, column=0, padx=5, columnspan=4, pady=10, sticky="nsew")

botao_exportar = customtkinter.CTkButton(frame_relatorio_estoque, text="exportar", command=abrir_pop_up, height=35,
                                         width=110, fg_color="purple")
botao_exportar.grid(padx=0, pady=5, row=1, column=3, sticky="e")

campo_busca = customtkinter.CTkEntry(frame_relatorio_estoque, placeholder_text="barra de pesquisa", width=200,
                                     height=35)
campo_busca.grid(padx=5, pady=5, row=1, column=0, sticky="w")

estilo = ttk.Style()
estilo.configure("Custom.Treeview", background="black", foreground="white", fieldbackground="black")

estilo.configure("Custom.Treeview.Heading", background="black", foreground="black", font=("Arial", 12, "bold"))

estilo.map("Custom.Treeview", background=[('selected', '#2a2625')], foreground=[('selected', 'white')])

colunas_estoque = ["Produtos", "Quantidade", "Preço", "Descrição"]
trivel_relatorio_estoque = ttk.Treeview(frame_relatorio_estoque, columns=colunas_estoque, show="headings",
                                        style="Custom.Treeview")
trivel_relatorio_estoque.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

trivel_relatorio_estoque.heading("Produtos", text="Produtos")
trivel_relatorio_estoque.heading("Quantidade", text="Quantidade")
trivel_relatorio_estoque.heading("Preço", text="Preço")
trivel_relatorio_estoque.heading("Descrição", text="Descrição")

trivel_relatorio_estoque.column("Produtos", width=140, anchor="center")
trivel_relatorio_estoque.column("Quantidade", width=140, anchor="center")
trivel_relatorio_estoque.column("Preço", width=140, anchor="center")
trivel_relatorio_estoque.column("Descrição", width=140, anchor="center")

trivel_relatorio_estoque.insert("", "end", values=("recebe_dados"))

botao_estoque = customtkinter.CTkButton(frame_relatorio_estoque, text='Estoque', width=100, command=abrir_relatorio,
                                        fg_color="green")
botao_estoque.grid(padx=10, row=3, column=0, sticky="e")

botao_saida = customtkinter.CTkButton(frame_relatorio_estoque, text='Saída', width=100, fg_color='#aa00ff',
                                      command=abrir_relatorio_saida)
botao_saida.grid(padx=10, row=3, column=1, sticky="w")

botao_entrada = customtkinter.CTkButton(frame_relatorio_estoque, text='Entrada', width=100, fg_color='#aa00ff',
                                        command=abrir_relatorio_entrada)
botao_entrada.grid(padx=10, row=3, column=2, sticky="w")

# Relatório de entrada__________________________________________________________________________________________________
titulo_estoque = customtkinter.CTkLabel(frame_relatorio_entrada, text="Relatório de entrada", font=("Arial", 30))
titulo_estoque.grid(row=0, column=0, padx=5, columnspan=4, pady=10, sticky="nsew")

botao_exportar = customtkinter.CTkButton(frame_relatorio_entrada, text="exportar", command=abrir_pop_up, height=35,
                                         width=110, fg_color="purple")
botao_exportar.grid(padx=0, pady=5, row=1, column=3, sticky="e")

campo_busca = customtkinter.CTkEntry(frame_relatorio_entrada, placeholder_text="barra de pesquisa", width=200,
                                     height=35)
campo_busca.grid(padx=5, pady=5, row=1, column=0, sticky="w")

estilo = ttk.Style()
estilo.configure("Custom.Treeview", background="black", foreground="white", fieldbackground="black")
estilo.configure("Custom.Treeview.Heading", background="black", foreground="black", font=("Arial", 12, "bold"))
estilo.map("Custom.Treeview", background=[('selected', '#2a2625')], foreground=[('selected', 'white')])

colunas_estoque = ["Produtos", "Quantidade", "Data/hora"]
trivel_relatorio_estoque_entrada = ttk.Treeview(frame_relatorio_entrada, columns=colunas_estoque, show="headings",
                                                style="Custom.Treeview")
trivel_relatorio_estoque_entrada.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

trivel_relatorio_estoque_entrada.heading("Produtos", text="Produtos")
trivel_relatorio_estoque_entrada.heading("Quantidade", text="Quantidade")
trivel_relatorio_estoque_entrada.heading("Data/hora", text="Data/hora")

trivel_relatorio_estoque_entrada.column("Produtos", width=185, anchor="center")
trivel_relatorio_estoque_entrada.column("Quantidade", width=185, anchor="center")
trivel_relatorio_estoque_entrada.column("Data/hora", width=185, anchor="center")

botao_estoque = customtkinter.CTkButton(frame_relatorio_entrada, text='Estoque', width=100, command=abrir_relatorio,
                                        fg_color="green")
botao_estoque.grid(padx=10, row=3, column=0, sticky="e")

botao_saida = customtkinter.CTkButton(frame_relatorio_entrada, text='Saída', width=100, fg_color='#aa00ff',
                                      command=abrir_relatorio_saida)
botao_saida.grid(padx=10, row=3, column=1, sticky="w")

botao_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text='Entrada', width=100, fg_color='#aa00ff',
                                        command=abrir_relatorio_entrada)
botao_entrada.grid(padx=10, row=3, column=2, sticky="w")

# Relatório de saída____________________________________________________________________________________________________
titulo_estoque = customtkinter.CTkLabel(frame_relatorio_saida, text="Relatório de saída", font=("Arial", 30))
titulo_estoque.grid(row=0, column=0, padx=5, columnspan=4, pady=10, sticky="nsew")

campo_busca = customtkinter.CTkEntry(frame_relatorio_saida, placeholder_text="barra de pesquisa", width=200, height=35)
campo_busca.grid(padx=5, pady=5, row=1, column=0, sticky="w")

botao_exportar = customtkinter.CTkButton(frame_relatorio_saida, text="exportar", command=abrir_pop_up, height=35,
                                         width=110, fg_color="purple")
botao_exportar.grid(padx=0, pady=5, row=1, column=3, sticky="e")

estilo = ttk.Style()
estilo.configure("Custom.Treeview", background="black", foreground="white", fieldbackground="black")
estilo.configure("Custom.Treeview.Heading", background="black", foreground="black", font=("Arial", 12, "bold"))
estilo.map("Custom.Treeview", background=[('selected', '#2a2625')], foreground=[('selected', 'white')])

colunas_estoque = ["Produtos", "Quantidade", "Data/hora"]
trivel_relatorio_estoque_saida = ttk.Treeview(frame_relatorio_saida, columns=colunas_estoque, show="headings",
                                              style="Custom.Treeview")
trivel_relatorio_estoque_saida.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

trivel_relatorio_estoque_saida.heading("Produtos", text="Produtos")
trivel_relatorio_estoque_saida.heading("Quantidade", text="Quantidade")
trivel_relatorio_estoque_saida.heading("Data/hora", text="Data/hora")

trivel_relatorio_estoque_saida.column("Produtos", width=185, anchor="center")
trivel_relatorio_estoque_saida.column("Quantidade", width=185, anchor="center")
trivel_relatorio_estoque_saida.column("Data/hora", width=185, anchor="center")

botao_estoque = customtkinter.CTkButton(frame_relatorio_saida, text='Estoque', width=100, command=abrir_relatorio)
botao_estoque.grid(padx=10, row=3, column=0, sticky="e")

botao_saida = customtkinter.CTkButton(frame_relatorio_saida, text='Saída', width=100, command=abrir_relatorio_saida,
                                      fg_color="green")
botao_saida.grid(padx=10, row=3, column=1, sticky="w")

botao_entrada = customtkinter.CTkButton(frame_relatorio_saida, text='Entrada', width=100,
                                        command=abrir_relatorio_entrada)
botao_entrada.grid(padx=10, row=3, column=2, sticky="w")

atualizar()
janela.mainloop()
