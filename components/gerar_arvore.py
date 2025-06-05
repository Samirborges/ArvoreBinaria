from fasthtml.common import  Ul, Li
from arquivos_arvores.ArvoreAVL import ArvoreAVL
from arquivos_arvores.Celula import Celula

def gerar_avore(avl: ArvoreAVL):
    lista_nodes = list()
    
    for no in list(avl.Tree): lista_nodes.append(Li(no))

    return Ul(
        *lista_nodes
    )
    