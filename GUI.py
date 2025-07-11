import tkinter as tk
from tkinter import messagebox, simpledialog
import os

ARQUIVO = "dados.txt"

def ler_dados():
    competidores = []
    if not os.path.exists(ARQUIVO):
        return competidores
    with open(ARQUIVO, "r") as f:
        for linha in f:
            campos = linha.strip().split(",")
            if len(campos) >= 7:
                competidores.append(campos)
    return competidores

def salvar_dados(competidores):
    with open(ARQUIVO, "w") as f:
        for campos in competidores:
            f.write(",".join(map(str, campos)) + "\n")

def listar():
    competidores = ler_dados()
    texto.delete(1.0, tk.END)
    if not competidores:
        texto.insert(tk.END, "Nenhum competidor cadastrado.\n")
        return
    cabecalho = "Modalidade | Gênero | RG | CPF | Nome | Idade | Peso\n"
    texto.insert(tk.END, cabecalho)
    texto.insert(tk.END, "-"*70 + "\n")
    for c in competidores:
        texto.insert(tk.END, " | ".join(c) + "\n")

def adicionar():
    campos = []
    for label in ["Modalidade", "Gênero", "RG", "CPF", "Nome", "Idade", "Peso"]:
        valor = simpledialog.askstring("Adicionar", f"Digite {label}:")
        if valor is None or valor.strip() == "":
            messagebox.showwarning("Atenção", f"{label} não informado.")
            return
        campos.append(valor.strip())
    competidores = ler_dados()
    # Verifica duplicidade de RG
    if any(c[2] == campos[2] for c in competidores):
        messagebox.showerror("Erro", "RG já cadastrado.")
        return
    competidores.append(campos)
    salvar_dados(competidores)
    messagebox.showinfo("Sucesso", "Competidor adicionado!")
    listar()

def remover():
    rg = simpledialog.askstring("Remover", "Digite o RG do competidor a ser removido:")
    if not rg:
        return
    competidores = ler_dados()
    novos = [c for c in competidores if c[2] != rg]
    if len(novos) == len(competidores):
        messagebox.showerror("Erro", "RG não encontrado.")
        return
    salvar_dados(novos)
    messagebox.showinfo("Sucesso", "Competidor removido!")
    listar()

def pesquisar():
    termo = simpledialog.askstring("Pesquisar", "Digite parte do nome:")
    if not termo:
        return
    termo = termo.lower()
    competidores = ler_dados()
    encontrados = [c for c in competidores if termo in c[4].lower()]
    texto.delete(1.0, tk.END)
    if not encontrados:
        texto.insert(tk.END, "Nenhum competidor encontrado.\n")
        return
    cabecalho = "Modalidade | Gênero | RG | CPF | Nome | Idade | Peso\n"
    texto.insert(tk.END, cabecalho)
    texto.insert(tk.END, "-"*70 + "\n")
    for c in encontrados:
        texto.insert(tk.END, " | ".join(c) + "\n")

def atualizar():
    rg = simpledialog.askstring("Atualizar", "Digite o RG do competidor a ser atualizado:")
    if not rg:
        return
    competidores = ler_dados()
    for i, c in enumerate(competidores):
        if c[2] == rg:
            # Atualiza cada campo
            for idx, label in enumerate(["Modalidade", "Gênero", "RG", "CPF", "Nome", "Idade", "Peso"]):
                novo = simpledialog.askstring("Atualizar", f"{label} atual: {c[idx]}\nNovo {label} (deixe em branco para manter):")
                if novo and novo.strip() != "":
                    competidores[i][idx] = novo.strip()
            salvar_dados(competidores)
            messagebox.showinfo("Sucesso", "Competidor atualizado!")
            listar()
            return
    messagebox.showerror("Erro", "RG não encontrado.")

# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Competidores")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_listar = tk.Button(frame, text="Listar", width=15, command=listar)
btn_listar.grid(row=0, column=0, padx=5, pady=5)

btn_adicionar = tk.Button(frame, text="Adicionar", width=15, command=adicionar)
btn_adicionar.grid(row=0, column=1, padx=5, pady=5)

btn_remover = tk.Button(frame, text="Remover", width=15, command=remover)
btn_remover.grid(row=0, column=2, padx=5, pady=5)

btn_pesquisar = tk.Button(frame, text="Pesquisar", width=15, command=pesquisar)
btn_pesquisar.grid(row=0, column=3, padx=5, pady=5)

btn_atualizar = tk.Button(frame, text="Atualizar", width=15, command=atualizar)
btn_atualizar.grid(row=0, column=4, padx=5, pady=5)

texto = tk.Text(root, width=90, height=20)
texto.pack(padx=10, pady=10)

listar()  # Mostra a lista ao iniciar

root.mainloop()