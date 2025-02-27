import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """Retorna o caminho correto do recurso (imagem) quando empacotado com PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main():
    # Data de início do relacionamento
    data_inicio = datetime(2023, 11, 5)

    def atualizar_contador():
        try:
            agora = datetime.now()
            delta = agora - data_inicio
            dias = delta.days
            horas, resto = divmod(delta.seconds, 3600)
            minutos, segundos = divmod(resto, 60)
            contador_label.config(text=f"{dias} dias, {horas:02} horas, {minutos:02} minutos juntos")
            root.after(1000, atualizar_contador)
        except Exception as e:
            print("Erro no atualizar_contador:", e)
            with open("erro_log.txt", "a") as f:
                f.write("Erro no atualizar_contador: " + str(e) + "\n")

    # Configuração da janela
    root = tk.Tk()
    root.title("Nosso Tempo Juntos")
    root.geometry("500x600")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=500, height=600)
    canvas.pack(fill="both", expand=True)

    # Carregar a imagem de fundo utilizando resource_path
    image_path = resource_path("imagem_fundo.jpg")
    try:
        if os.path.exists(image_path):
            imagem_fundo = Image.open(image_path)
            imagem_fundo = imagem_fundo.resize((500, 600), Image.LANCZOS)
            fundo = ImageTk.PhotoImage(imagem_fundo)
            canvas.create_image(0, 0, anchor="nw", image=fundo)
            # Mantém referência para não ser descartada
            canvas.image = fundo
        else:
            raise FileNotFoundError(f"{image_path} não encontrado.")
    except Exception as e:
        print("Erro ao carregar imagem:", e)
        with open("erro_log.txt", "a") as f:
            f.write("Erro ao carregar imagem: " + str(e) + "\n")
        canvas.create_rectangle(0, 0, 500, 600, fill="gray")

    # Rótulo do contador
    contador_label = tk.Label(root, text="", font=("Arial", 20, "bold"), fg="white", bg="black")
    contador_label.place(relx=0.5, rely=0.2, anchor="center")

    # Rótulo com a mensagem personalizada
    mensagem = ("Esse é um relógio que vai te lembrar pra sempre tudo que passamos e quando nos amamos.\n\n"
                "Do seu menino e sua menina, Te amamos.")
    mensagem_label = tk.Label(root, text=mensagem, font=("Arial", 12), fg="white", bg="black", wraplength=400, justify="center")
    mensagem_label.place(relx=0.5, rely=0.85, anchor="center")

    atualizar_contador()

    try:
        root.mainloop()
    except Exception as e:
        print("Erro no mainloop:", e)
        with open("erro_log.txt", "a") as f:
            f.write("Erro no mainloop: " + str(e) + "\n")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Erro na execução do programa:", e)
        with open("erro_log.txt", "w") as f:
            f.write("Erro na execução do programa: " + str(e) + "\n")