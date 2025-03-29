from dataclasses import dataclass, field
from typing import List, Optional, Any
from enum import Enum

class Direction(Enum):
    ESQUERDA = 'Esquerda'
    DIREITA = 'Direita'
    RAIZ = 'RAIZ'

@dataclass
class Celula:
    _node_father: Optional['Celula']
    _nodes_children: List['Celula'] = field(default_factory=list)
    content: Any = None
    _direction: Direction = None
    
    def __post_init__(self):
        if self._nodes_children is None:
            self._nodes_children = []
    
    def __str__(self):
        return self.content
    
    def __hash__(self): return hash(self.content) # O network x aceita apenas elementos hashaveis. A instância dessa classe não é hashavel, a menos com esse thunder method.
        
    # Nós pais
    @property
    def node_father(self): return self._node_father
    
    @node_father.setter
    def node_father(self, node_father: Optional['Celula']): self._node_father = node_father

    # Nós filhos
    @property
    def nodes_children(self): return self._nodes_children
    
    @nodes_children.setter
    def nodes_children(self, node_children: Optional['Celula']): self._nodes_children.append(node_children)
    
    # Direção
    @property
    def direction(self): return self._direction.value
    
    
# Teste    
# Testes isolados
def initial_teste():
    # Teste de mudança de pai com a raiz
    celula_teste = Celula('celula 1', None, 'celula teste', Direction.DIREITA) # Adicionar uma classe com 
    print(celula_teste.node_father )
    
    celula_raiz = Celula(None, None, 'RAIZ', Direction.RAIZ) # Adicionando raiz
    celula_teste.node_father = celula_raiz # Mudando nó pai
    print(celula_teste.node_father )
    
    print('Verficiando a direção do nó')
    print(celula_teste.direction)
    
def teste_filhos_celulas():
    raiz = Celula(None, None, 'RAIZ', Direction.RAIZ)
    celula1 = Celula(raiz, None, 'celula 1', Direction.ESQUERDA) 
    raiz.nodes_children = celula1
    
    print('Conteúdo dos nós filhos')
    for children_nodes in raiz.nodes_children:
        print(children_nodes.content)
    
# Execução teste
if __name__ == '__main__':
    teste_filhos_celulas()

    