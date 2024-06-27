# bibliotecas
# para receber arquivos:
# import tkinter as tk
# from tkinter import filedialog
import csv

# para se conectar ao SAP:
import flask
import flask_restful
import json
import os
from datetime import datetime

# classe principal


class main():
    def formatar_parametros(body):
        print("Formatando parâmetros...")
        data_format = datetime.strptime(
            body[0]['datetime'], '%Y%m%d').strftime('%d/%m/%Y')
        return data_format

    def busca_arquivos(p_data):
        print("Buscando arquivos...")

        diretorio = '/Users/sraso/OneDrive/Documentos/docs_maria/python/diretorio_teste'

        # Buscando arquivos na data recebida
        for nome_arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            # Verificar se não é um diretório
            if os.path.isfile(caminho_arquivo):
                data_modificacao = datetime.fromtimestamp(
                    os.path.getmtime(caminho_arquivo))
                data_modif = datetime.strftime(data_modificacao, '%d/%m/%Y')
                if data_modif == p_data:
                    with open(caminho_arquivo, 'r') as arquivo:
                        conteudo = arquivo.read()
                        print(nome_arquivo)
                        print(conteudo)
                        result = (f"{nome_arquivo} -> conteudo: {conteudo}")
                    break

        else:
            result = (
                f"Nenhum arquivo encontrado com data {p_data} no diretorio {diretorio}.")

        return result

    def run():
        print("Iniciou.")


# parâmetros para a API
port = 5723
api = flask.Flask(__name__)
getApi = flask_restful.Api(api)


@api.route('/', methods=['GET'])
async def raiz():

    # Criando e iniciando API
    os.system('cls')
    print(flask.request.data)
    get_body = json.loads(flask.request.data)

    try:

        datetime = main.formatar_parametros(get_body)
        lv_return = main.busca_arquivos(datetime)

        return {
            "message": "Sucesso",
            "datetime_formatted": datetime,
            "return": lv_return
        }

    except:
        return {
            "message": "Erro ao processar GET."
        }

if __name__ == '__main__':
    # os.system('cls')
    try:
        api.run(debug=True, host='0.0.0.0', port=5723)
    except:
        # Caso haja qualquer erro matar a execução da lib
        print("Erro de Execução - __main__")
