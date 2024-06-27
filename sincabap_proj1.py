# bibliotecas
# para receber arquivos:
# import tkinter as tk
# from tkinter import filedialog
# import csv
# import datetime as dt

# para se conectar ao SAP:
import flask
import flask_restful
import json
import os

# classe principal
class main():
    def formatar_parametros(body):
        print("Formatando parâmetros...")
        return body[0]['datetime']

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
        # datetime_noformat = get_body['datetime']
        # datetime_obj = datetime_noformat.strptime(datetime_noformat, '%y%m%d')
        # formatted_date = datetime_obj.strftime('%d/%m/%y')
        datetime = main.formatar_parametros(get_body)
        response = "datetime"
        return {
            "message": "Sucesso",
            "datetime_formatted": datetime
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
