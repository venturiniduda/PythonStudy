# bibliotecas
# para receber arquivos:
import tkinter as tk
from tkinter import filedialog
import csv
import Pylance as pyl

# para se conectar ao SAP:
import flask
import flask_restful
import requests
import json
import os

# classe principal
class main():
    def modify_parameters(date_str):
         # Formatação de Parâmetros
         try:
            return pyl.datetime.datetime.strptime(date_str, '%Y-%m-%d')
         except ValueError:
            return json.dumps({'erro': 'Formato de data inválido'}), 400
         
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

    def run():
        # execução
        # estruturando tela
        root = tk.Tk()
        root.withdraw()
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

# parâmetros para a API
port = 5723
api = flask.Flask(__name__)
postApi = flask_restful.Api(api)

@api.route('/', methods=['POST'])
async def raiz():    
    os.system('cls')
    
    p_data = main.modify_parameters(requests.form['data_arquivo'])

    try:
        # Convert o post em um arquivo ini
        print("processar dados")
        main.run()
        ret_meth = arquivo_selecionado
    
        if ret_meth !=0:
            return{"Message": "Erro ao processar dados."}
        
        return{
        "Message": "Sucesso",
        "Ret_Tb": ret_meth
        }

    except:
        return{
            "Message": "Erro ao processar POST."
        }         
    
if __name__ == '__main__':
# os.system('cls')
    try:
        api.run(debug=True, host='0.0.0.0', port=5723)
    finally:
    # Caso haja qualquer erro matar a execução da lib
        print("Erro")
    
    


