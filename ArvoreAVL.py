from dataclasses import dataclass
from ArvoreBinaria import ArvoreBinaria
from Celula import Celula, Direction

@dataclass
class ArvoreAVL(ArvoreBinaria):
    
    def __init__(self, first_node_content):
        first_node = Celula(None, None, first_node_content, Direction.RAIZ)
        self.Tree.add_node(first_node)    
    
    def adicionar(self, node_father, node_add):
        return super().adicionar(node_father, node_add)
        
    
    def balanceamento_():
        ...

if __name__ == '__main__':
    arvore = ArvoreAVL('RAIZ')
    
    arvore.adicionar('RAIZ', Celula(None, None, '27', Direction.DIREITA))
    arvore.adicionar('27', Celula(None, None, '29', Direction.DIREITA))

    # Problema com o método de verificar para encontrar à RAIZ
    print(arvore.verificar_no(arvore.found_index_node('27'))) 
    
    