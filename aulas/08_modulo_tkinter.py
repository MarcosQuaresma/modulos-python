# o Modulo Tkinter é essencial para construir aplicações desktop
import tkinter as tk

# 1 Diando a janela
janela = tk.Tk()
janela.geometry("300x150")
janela.title("Gerencia Frases")

# 2 Adicionar um Frame -> Rótulo, Campo de Texto e um Botão
# Frame - Quadro
quadro = tk.Frame(janela)
quadro.pack(padx=10, pady=10, fill="x", expand=True)

# 3 Adicionando um Label
# Label - Rótulo
rotulo = tk.Label(quadro, text="Olá Quaresma!")
rotulo.pack(fill="x", expand=True)

# 4 Adicionando o input text
fraseRotulo = tk.Label(janela, text="Frase")
fraseRotulo.pack(fill="x", expand=True)

fraseInput = tk.Entry(janela)
fraseInput.pack(fill="x", expand=True)

# 5 Função para alterar o texto do Label - Rótulo
def click():
    rotulo.config(text=fraseInput.get())

# 6 Adicionando o Botão
botao = tk.Button(janela, text="Enviar", command=click)
botao.pack(fill="x", expand=True)

janela.mainloop()