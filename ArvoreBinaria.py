import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from networkx.drawing.nx_pydot import graphviz_layout
from Celula import Celula, Direction

@dataclass
class ArvoreBinaria:
    raiz_content: any
    Tree: nx.DiGraph = field(default_factory=nx.DiGraph, init=False)

    def __post_init__(self):
        self.RAIZ = Celula(None, None, self.raiz_content, Direction.RAIZ)
        self.Tree.add_node(self.RAIZ)

    # A impressão continua com problema
    def imprimir(self):
        # pos = pydot_layout(self.Tree, prog='dot')  # Layout hierárquico
        # labels = {node: node for node in self.Tree.nodes()}

        # plt.figure(figsize=(6, 4))
        # nx.draw(self.Tree, pos, with_labels=True, labels=labels, node_color='lightblue', edge_color='gray',
        #         node_size=1000, font_size=10)
        # plt.show()
        
        plt.figure(figsize=(8, 5))
        pos = nx.spring_layout(self.Tree, seed=42)
        nx.draw(self.Tree, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, edge_color='gray')
        plt.show()
       
    def adicionar(self, node_father: str, node_add: Celula) -> None:
        """Adiciona um nó a estrutura Árovore Binária

        Args:
            node_father (str): Adicionar o conteúdo que está na célula/nó pai
            node_add (Celula): Célula/Nó que vai ser adicionado à estrutura
        """
        # Buscando a celula/no pai
        try:
            node_father_content = node_father.content
            node_father = self.found_index_node(node_father_content)
        except:
            node_father = self.found_index_node(node_father)
        
        if node_father not in self.Tree:
            raise Exception(f"Erro: O nó pai '{node_father}' não existe na árvore.")
            

        if node_add in self.Tree:
            raise Exception(f"Erro: O nó '{node_add}' já existe na árvore.")
            

        if self.degree_node(node_father) >= 2:
            raise Exception(f'O nó {node_father} já possui dois filhos.')
            
        for child in node_father.nodes_children:
            if child.direction == node_add.direction:
                raise Exception(f'Erro! Já existe um nó ocupando a posição: {node_add.direction}')
           
        self.Tree.add_edge(node_father, node_add)
        
        node_father.nodes_children = node_add

    def degree_node(self, node: Celula) -> Celula:
        if node not in self.Tree:
            return -1
        return self.Tree.degree(node) - (1 if node.content != 'RAIZ' else 0)

    def found_index_node(self, node_content: str) -> int:
        """Procura a celula dentro da estrutura através do conteúdo dentro da célula em str.

        Args:
            node_content (str): Conteúdo dentro da célula

        Returns:
            Celula: Retorna o objeto Celula que está sendo buscado.
        """
        
        for node in list(self.Tree):
            if node.content == node_content:
                return node
        raise Exception(f'O nó com o conteúdo {node_content} não foi encotrado na árvore.')

    def profundidade_arvore(self) -> int:
        return max(self.depth_node(node) for node in self.Tree.nodes())

    def depth_node(self, node: Celula) -> int:
        if node not in self.Tree:
            return -1
        return nx.shortest_path_length(self.Tree, self.found_index_node('RAIZ'), node)

    def altura_no(self, node: Celula) -> int:
        if node not in self.Tree:
            return -1
        return self._altura_aux(node)

    def _altura_aux(self, node: Celula) -> int:
        filhos = [filho for filho in self.Tree.neighbors(node) if self.depth_node(filho) > self.depth_node(node)]
        if not filhos:
            return 0
        return 1 + max(self._altura_aux(filho) for filho in filhos)

    def altura_arvore(self) -> int:
        return self.altura_no(self.found_index_node('RAIZ'))

    def nivel_no(self, node: Celula) -> int:
        return self.depth_node(node)

    def verificar_no(self, node: Celula) -> dict:
        if node not in self.Tree:
            return {"erro": f"O nó '{node.content}' não existe na árvore."}

        # Pai: quem aponta para o nó
        parents = list(self.Tree.predecessors(node))
        parent = parents[0] if parents else None

        # Irmãos: outros filhos do mesmo pai
        siblings = []
        if parent:
            siblings = [n for n in self.Tree.successors(parent) if n != node]

        # Avo: pai do pai
        grandparent = None
        if parent:
            gp = list(self.Tree.predecessors(parent))
            if gp:
                grandparent = gp[0]

        # Tios: filhos do avo que não são o pai
        uncles = []
        if grandparent:
            uncles = [n for n in self.Tree.successors(grandparent) if n != parent]

        # Filhos: nós que este nó aponta
        children = list(self.Tree.successors(node))

        return {
            "nó": node.content,
            "pai": parent.content if parent else None,
            "irmãos": [n.content for n in siblings],
            "tios": [n.content for n in uncles],
            "filhos": [n.content for n in children],
            "direção": node.direction if node.direction else None
        }
      
        
    # L) Crie uma função que identifique nós folha
    def identify_node_sheet(self) -> list[str]:
        list_node_sheet = []
        for node in list(self.Tree.nodes):
            neighbors_node = list(self.Tree[node])
            index_node_father = neighbors_node[0]
            neighbors_node.remove(index_node_father)

            if len(neighbors_node) == 0:
                 list_node_sheet.append(node.content)
            continue

        return list_node_sheet
    
    # M) Crie uma função que realize a impressão da árvore em formato hierárquico;
    def imprimir_hierarquia(self) -> None:
        for node in self.Tree.nodes:
            content_node = node.content
            
            filhos = [filho.content for filho in self.Tree.neighbors(node) if self.depth_node(filho) > self.depth_node(node)]

            if content_node == 'RAIZ':
                print(f'{content_node}: {filhos}')
            else:
                print(f'{content_node}: {filhos}')
                
    def preOrdem(self, node=None):
        if node is None:
            node = self.found_index_node('RAIZ')  # Começa pela raiz
        
        visitados = set()
        
        def _preOrdem_recursivo(no):
            if no is None or no in visitados:
                return
            
            print(no.content, end=' ')  # Visita o nó atual
            visitados.add(no)
            
            filhos = sorted(
                [filho for filho in self.Tree.neighbors(no) if self.depth_node(filho) > self.depth_node(no)],
                key=lambda x: getattr(x, 'direction', None)  # Ordena pelo atributo direction, se existir
            )
            
            for filho in filhos:
                _preOrdem_recursivo(filho)
        
        _preOrdem_recursivo(node)


    def inOrdem(self, node=None):
        if node is None:
            node = self.found_index_node('RAIZ')
        
        visitados = set()
        
        def _inOrdem_recursivo(no):
            if no is None or no in visitados:
                return
            
            visitados.add(no)
            
            filhos = sorted(
                [filho for filho in self.Tree.neighbors(no) if self.depth_node(filho) > self.depth_node(no)],
                key=lambda x: getattr(x, 'direction', None)
            )
            
            if filhos:
                _inOrdem_recursivo(filhos[0])  # Esquerda
            
            print(no.content, end=' ')  # Visita o nó atual
            
            if len(filhos) > 1:
                _inOrdem_recursivo(filhos[1])  # Direita
        
        _inOrdem_recursivo(node)


    def posOrdem(self, node=None):
        if node is None:
            node = self.found_index_node('RAIZ')
        
        visitados = set()
        
        def _posOrdem_recursivo(no):
            if no is None or no in visitados:
                return
            
            visitados.add(no)
            
            filhos = sorted(
                [filho for filho in self.Tree.neighbors(no) if self.depth_node(filho) > self.depth_node(no)],
                key=lambda x: getattr(x, 'direction', None)
            )
            
            for filho in filhos:
                _posOrdem_recursivo(filho)  # Visita os filhos primeiro
            
            print(no.content, end=' ')  # Visita o nó atual
        
        _posOrdem_recursivo(node)


    # N) Percurso Pré-Ordem (Root -> Left -> Right)
    def pre_ordem(self, node: Celula = None) -> None:
        if node is None:
            node = self.found_index_node('RAIZ')
        
        # print(node.content, end=" ")
        # for filho in node.nodes_children:
        #     self.pre_ordem(filho)
        resultado = []
        self._pre_ordem_aux(node, resultado)
        return resultado
    
    def _pre_ordem_aux(self, node, resultado):
        if node:
            resultado.append(node.content)
            for child in node.nodes_children:
                self._pre_ordem_aux(child, resultado)
            
    # O) Percurso Pós-Ordem (Left -> Right -> Root)
    def pos_ordem(self, node: Celula = None) -> None:
        if node is None:
            node = self.found_index_node('RAIZ')
        # for filho in node.nodes_children:
        #     self.pos_ordem(filho)
        # print(node.content, end=" ")
        
        resultado = []
        self._pos_ordem_aux(node, resultado)
        return resultado
    
    def _pos_ordem_aux(self, node, resultado):
        if node:
            for child in node.nodes_children:
                self._pos_ordem_aux(child, resultado)
            resultado.append(node.content)
    
    # P) Percurso In-Ordem (Left -> Root -> Right)
    def in_ordem(self, node: Celula = None):
        if node is None:
            node = self.found_index_node('RAIZ')
        
        # if len(node.nodes_children) > 0:
        #     self.in_ordem(node.nodes_children[0])
        
        # print(node.content, end=' ')
        
        # if len(node.nodes_children) > 1:
        #     self.in_ordem(node.nodes_children[1])
        
        resultado = []
        self._in_ordem_aux(node, resultado)
        return resultado
    
    def _in_ordem_aux(self, node, resultado):
        if node:
            if len(node.nodes_children) > 0:
                self._in_ordem_aux(node.nodes_children[0], resultado)
        resultado.append(node.content)
        if len(node.nodes_children) > 1:
            self._in_ordem_aux(node.nodes_children[1], resultado)

# Teste
if __name__ == "__main__":
    # Teste com célula:

    arvore = ArvoreBinaria('RAIZ')
    
    arvore.adicionar(arvore.RAIZ, Celula(None, None, 'A', Direction.ESQUERDA))
    arvore.adicionar(arvore.RAIZ, Celula(None, None, 'B', Direction.DIREITA))
    arvore.adicionar('A', Celula(None, None, 'C', Direction.ESQUERDA))
    arvore.adicionar('A', Celula(None, None, 'D', Direction.DIREITA))
    arvore.adicionar('B', Celula(None, None, 'E', Direction.ESQUERDA))
    arvore.adicionar('B', Celula(None, None, 'F', Direction.DIREITA))
    arvore.adicionar('C', Celula(None, None, 'G', Direction.ESQUERDA))
    arvore.adicionar('C', Celula(None, None, 'H', Direction.DIREITA))
    
    # Teste de métodos
    print(f'Altura {arvore.altura_no(arvore.found_index_node('A'))}') # Resultado esperado: Altura 2
    print(f'Altura {arvore.altura_no(arvore.found_index_node('B'))}') # Resultado esperado: Altura 1
    print(f'Altura {arvore.altura_no(arvore.found_index_node('C'))}') # Resultado esperado: Altura 1
    print(f'Altura {arvore.altura_no(arvore.found_index_node('D'))}') # Resultado esperado: Altura 0
    print(f'Altura {arvore.altura_no(arvore.found_index_node('RAIZ'))}') # Resultado esperado: Altura 3
    
    print('-'*30)
    
    print(f'Altura da árvore: {arvore.altura_arvore()}')

    print('-'*30)
    
    print(f'Nível do nó RAIZ: {arvore.nivel_no(arvore.found_index_node('RAIZ'))}') # Resultado esperado: 0
    print(f'Nível do nó A: {arvore.nivel_no(arvore.found_index_node('A'))}') # Resultado esperado 1
    print(f'Nível do nó B: {arvore.nivel_no(arvore.found_index_node('B'))}') # Resultado esperado: 1
    print(f'Nível do nó C: {arvore.nivel_no(arvore.found_index_node('C'))}') # Resultado esperado: 2
    print(f'Nível do nó D: {arvore.nivel_no(arvore.found_index_node('D'))}') # Resultado esperado: 2
    print(f'Nível do nó E: {arvore.nivel_no(arvore.found_index_node('E'))}') # Resultado esperado: 2
    print(f'Nível do nó F: {arvore.nivel_no(arvore.found_index_node('F'))}') # Resultado esperado: 2
    print(f'Nível do nó G: {arvore.nivel_no(arvore.found_index_node('G'))}') # Resultado esperado: 3
    print(f'Nível do nó H: {arvore.nivel_no(arvore.found_index_node('H'))}') # Resultado esperado: 3
    
    print('-'*30)
    
    print(arvore.verificar_no(arvore.found_index_node('A')))
     # Nó: A
     # Pai: RAIZ
     # Irmãos: B
     # Tios: Nenhum
     # Filhos: C, D
     # Direção: Esquerda

    print('-'*30)
    
    print(arvore.verificar_no(arvore.found_index_node('C')))
     # Nó: C
     # Pai: A
     # Irmãos: D
     # Tios: B
     # Filhos: G, H
     # Direção: Esquerda
     
    print('-'*30)
    arvore.imprimir_hierarquia()
     # RAIZ: ['A', 'B']
     # A: ['C', 'D']
     # B: ['E', 'F']
     # C: ['G', 'H']
     # D: []
     # E: []
     # F: []
     # G: []
     
    print('-'*30)
    print(f'preOrdem: {arvore.pre_ordem()}') 
    print(f'inOrdem: {arvore.in_ordem()}') 
    print(f'posOrdem: {arvore.pos_ordem()}')
    #  Resultado esperado:
    #  preOrdem: ['RAIZ', 'A', 'C', 'G', 'H', 'D', 'B', 'E', 'F']
    #  inOrdem: ['G', 'C', 'H', 'A', 'D', 'RAIZ', 'E', 'B', 'F']
    #  posOrdem: ['G', 'H', 'C', 'D', 'A', 'E', 'F', 'B', 'RAIZ']
    