from fasthtml.common import Div, Ul, Li
from arquivos_arvores.ArvoreAVL import ArvoreAVL

def avl_hierarquia(avl: ArvoreAVL):
    saida = list()
    for node in avl.Tree.nodes:
        filhos = [f.content for f in node.nodes_children]
        saida.append(f"{node.content}: {', '.join(filhos) if filhos else 'Sem filhos'}")
    
    impressao = list()
    for info in saida:
        impressao.append(Li(info))
    
    return Div(
        Ul(*impressao)
    )