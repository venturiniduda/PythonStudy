# bibliotecas
# para receber arquivos:
import tkinter as tk
from tkinter import filedialog

# classe principal


class main():
    def choice_data():
        filetype = [('Arquivos CSV', '*.csv'),
                    ('Arquivos Excel', '*.xlsx;*.xls')]
        ti_data = filedialog.askopenfilename(filetypes=filetype)
        if ti_data:
            global arquivo_selecionado
            arquivo_selecionado = ti_data
            label_arquivo.config(
                text=f"Arquivo selecionado: {arquivo_selecionado}")
        else:
            label_arquivo.config(text="Nenhum arquivo selecionado.")

    def receive_data():

        print("Recebeu dados.")

    def modify_data():
        print("Modificou e padronizou os dados.")

    def send_data():
        print("Enviou os dados.")


# execução
# estruturando tela
root = tk.Tk()
# root.withdraw()
root.title("Escolher arquivo: ")
arquivo_selecionado = None

label_arquivo = tk.Label(
    root, text="Nenhum arquivo selecionado.", pady=10, padx=10)
label_arquivo.pack(fill=tk.BOTH, padx=20, pady=5)

btn_escolher = tk.Button(root, text="Escolher Arquivo: ",
                         command=main.choice_data, bg = "grey", pady=3, padx=3)
btn_escolher.pack(fill=tk.BOTH, padx=10, pady=10)

root.mainloop()

print("Caminho do arquivo selecionado: ", arquivo_selecionado)

main.receive_data()
