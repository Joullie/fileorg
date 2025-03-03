import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import ttkbootstrap as ttk


# Dicionário de categorias
EXTENSIONS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".jfif"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv", ".midi"],
    "Áudio": [".mp3", ".wav", ".ogg", ".midi"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".epub"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executáveis": [".exe", ".msi"],
    "Arquivos 3D": [".dae", ".obj", ".fbx", ".stl", ".blend"],
}

# Função para organizar arquivos
def organizar_arquivos():
    # Obtendo o caminho das pastas
    origem = entry_origem.get()
    destino = entry_destino.get()

    if not origem or not destino:
        messagebox.showwarning("Erro", "Selecione as pastas de origem e destino!")
        return
# Caso a pasta destino não exista, ela será criada
    if not os.path.exists(destino):
        os.makedirs(destino)

    for item in os.listdir(origem):
        caminho_item = os.path.join(origem, item)

        # Se for uma subpasta, move para a pasta "Pastas"
        if os.path.isdir(caminho_item) and item != "Pastas":
            pasta_destino = os.path.join(destino, "Pastas")
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            try:
                shutil.move(caminho_item, os.path.join(pasta_destino, item))
                log_text.insert(tk.END, f"Pasta : {item} → Pastas\n")
            except Exception as e:
                log_text.insert(tk.END, f"Erro ao mover pasta {item}: {str(e)}\n")

        # Se for um arquivo, move para a pasta correspondente
        elif os.path.isfile(caminho_item):
            _, ext = os.path.splitext(item)
            for categoria, exts in EXTENSIONS.items():
                if ext.lower() in exts:
                    pasta_destino = os.path.join(destino, categoria)
                    if not os.path.exists(pasta_destino):
                        os.makedirs(pasta_destino)
                    try:
                        shutil.move(caminho_item, os.path.join(pasta_destino, item))
                        log_text.insert(tk.END, f"Movido: {item} → {categoria}\n")
                    except Exception as e:
                        log_text.insert(tk.END, f"Erro ao mover arquivo {item}: {str(e)}\n")

    messagebox.showinfo("Concluído", "Arquivos organizados com sucesso!")

# Funções para escolher pastas
def escolher_origem():
    pasta = filedialog.askdirectory()
    entry_origem.delete(0, tk.END)
    entry_origem.insert(0, pasta)

def escolher_destino():
    pasta = filedialog.askdirectory()
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, pasta)

# Interface 
root = tk.Tk()
root.title("Organizador de Arquivos")
root.geometry("500x400")

tk.Label(root, text="Pasta de Origem:").pack()
entry_origem = tk.Entry(root, width=50)
entry_origem.pack()
tk.Button(root, text="Selecionar", command=escolher_origem).pack()

tk.Label(root, text="Pasta de Destino:").pack()
entry_destino = tk.Entry(root, width=50)
entry_destino.pack()
tk.Button(root, text="Selecionar", command=escolher_destino).pack()

tk.Button(root, text="Organizar Arquivos", command=organizar_arquivos).pack(pady=10)

log_text = tk.Text(root, height=10, width=60)
log_text.pack()

root.mainloop()
