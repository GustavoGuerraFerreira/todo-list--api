from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date  

app = FastAPI()
class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]

lista = []

@app.post('/inserir')
def inserir(obj: Todo):
    try:
        lista.append(obj)
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}
    

@app.post('/listar')
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))
   

@app.post('/listagemUnica/{id}')
def listagemUnica(id : int):
    try :
        return lista[id]
    except:
        return{'status': 'erro'}
    
@app.post('/alteraStauts')
def listagemUnica(id : int):
    try :
         lista[id].realizada = not lista[id].realizada
         return {'status': 'sucesso'}
    except:
        return {'status' : 'erro'}

@app.post('/excluir')
def excluir(id : int):
    try :
         del lista[id]
         return {'status': 'sucesso'}
    except:
        return {'status' : 'erro'}

   
