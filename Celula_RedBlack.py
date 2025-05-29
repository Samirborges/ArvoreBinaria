from Celula import Celula, Direction, Enum
from dataclasses import dataclass, field
from enum import Enum


class Color(Enum):
    COLOR_RED = 'Vermelho'
    COLOR_BLACK = 'Preto'

@dataclass
class Celula_RedBlack(Celula):
    color: Color = field(default=Color.COLOR_RED)
    

# Área de teste ----------------------------------------------
if __name__ == '__main__':
    raiz = Celula_RedBlack(None, None, 'RAIZ', Direction.RAIZ, Color.COLOR_RED)
    celula1 = Celula_RedBlack(None, None, 'celula 1', Direction.ESQUERDA, Color.COLOR_BLACK)
    raiz.nodes_children.append(celula1)
    
    print('Conteúdo dos nós filhos')
    for children_nodes in raiz.nodes_children:
        print(f'Nó: {children_nodes}, cor: {children_nodes.color.value}')
        
    