# PythonStudy
## Por Maria Eduarda Venturini Wollmann

### Projeto SINCABAP
Objetivo: estruturar API para receber tabela do usuário, formatar os dados e enviar para a tabela correspondente no SAP. 

Report: YESTMW_APISINCABAP 

### Possíveis caminhos 
#### Ideia 1: 
Caminho de execução: 
- Programa ABAP chama a API 
- API no python pede os dados para o cliente ou puxa de outro lugar (por exemplo, de X pasta pré definida no sistema)
  - se a data de modificação da última planilha for > que a data da última vez que rodou a API, os dados são processados. Se for igual ou menor, retorna que os dados já foram processados.
- Os dados da planilha/tabela são tratados
  - Ideia: os dados tratados vão para outro programa Python para serem executados e servirem de aprendizado para uma IA
- Os dados tratados retornam para o SAP e, no programa ABAP, a tabela é modificada no SAP

#### Referências utilizadas:
[Conexão Python com SAP](https://community.sap.com/t5/technology-blogs-by-members/connecting-python-with-sap-step-by-step-guide/ba-p/13452893)
[Orientação a Objeto no Python](https://www.hashtagtreinamentos.com/programacao-orientada-a-objetos-python?gad_source=1&gclid=CjwKCAjwps-zBhAiEiwALwsVYcX4tg8IXy0z85kxl43HZMtxR__ijv1YA8eRGNjeHx9fiCNiuBm4_xoCCcEQAvD_BwE)
[Métodos Python](https://www.w3schools.com/python/python_file_handling.asp)
[Biblioteca TKINTER](https://docs.python.org/3/library/dialog.html)