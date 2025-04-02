import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass
# from networkx.drawing.nx_pydot import pydot_layout
from Celula import Celula, Direction

@dataclass
class ArvoreBinaria:
    Tree: nx.Graph = nx.Graph()

    def __post_init__(self):
        raiz = Celula(None, None, 'RAIZ', Direction.RAIZ)
        self.Tree.add_node(raiz)

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
        node_father = self.found_index_node(node_father)
        
        if node_father not in self.Tree:
            print(f"Erro: O nó pai '{node_father}' não existe na árvore.")
            return

        if node_add in self.Tree:
            print(f"Erro: O nó '{node_add}' já existe na árvore.")
            return

        if self.degree_node(node_father) >= 2:
            print(f'O nó {node_father} já possui dois filhos.')
            return
        
        if len(node_father.nodes_children) > 0:
            node_child = node_father.nodes_children[0]
            if node_child.direction == node_add.direction:
                print('Um nó já ocupa essa posição. Escolha outra.')
                return
           
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
        raise(f'O nó com o conteúdo {node_content} foi encotrado na árvore.')

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

    def verificar_no(self, node: Celula) -> None:
        if node not in self.Tree:
            print(f"O nó '{node}' não existe na árvore.")
            return

        parent = next((pai for pai in self.Tree.neighbors(node) if self.depth_node(pai) < self.depth_node(node)), None)
        
        if not parent:
            print(f"Nó: {node.content} (RAIZ)")
            return

        irmaos = [n.content for n in self.Tree.neighbors(parent) if n != node and self.depth_node(n) > self.depth_node(parent)]
        avo = next((p for p in self.Tree.neighbors(parent) if self.depth_node(p) < self.depth_node(parent)), None)
        tios = []
        if avo:
            tios = [n for n in self.Tree.neighbors(avo) if n != parent and self.depth_node(n) > self.depth_node(avo)]

        # filhos_pai = [n for n in self.Tree.neighbors(parent) if self.depth_node(n) > self.depth_node(parent)]
        lado = node.direction

       
        print(f"Nó: {node}")
        print(f"Pai: {parent}")
        print(f"Irmãos: {irmaos}")
        print(f"Tios: {tios}")
        print(f"Lado do nó {node}: {lado}.")
        
        return lado
        
    # L) Crie uma função que identifique nós folha
    def identify_node_sheet(self) -> list[str]:
        list_node_sheet = []
        for node in list(self.Tree.nodes):
            neighbors_node = list(self.Tree[node])
            index_node_father = neighbors_node[0]
            neighbors_node.remove(index_node_father)

            if len(neighbors_node) <= 0:
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


# Teste
if __name__ == "__main__":
    # Teste com célula:

    arvore = ArvoreBinaria()
    # arvore.adicionar('RAIZ', Celula(arvore.found_index_node('RAIZ'), None, 'Celula 1', Direction.ESQUERDA))
    # arvore.adicionar('RAIZ', Celula(arvore.found_index_node('RAIZ'), None, 'Celula 2', Direction.DIREITA))

    # arvore.adicionar('RAIZ', Celula(arvore.found_index_node('RAIZ'), None, 'Celula 3', Direction.DIREITA))
    
    # print(f'Grau do nó RAIZ {arvore.degree_node(arvore.found_index_node('RAIZ'))}')
    # arvore.adicionar('Celula 1', Celula(arvore.found_index_node('Celula 1'), None, 'Celula 3', Direction.ESQUERDA))

    # Criando uma árvore
    arvore.adicionar('RAIZ', Celula(arvore.found_index_node('RAIZ'), None, 'A', Direction.ESQUERDA))
    arvore.adicionar('RAIZ', Celula(arvore.found_index_node('RAIZ'), None, 'B', Direction.DIREITA))
    arvore.adicionar('A', Celula(arvore.found_index_node('A'), None, 'C', Direction.ESQUERDA))
    arvore.adicionar('A', Celula(arvore.found_index_node('A'), None, 'D', Direction.DIREITA))
    arvore.adicionar('B', Celula(arvore.found_index_node('B'), None, 'E', Direction.ESQUERDA))
    arvore.adicionar('B', Celula(arvore.found_index_node('B'), None, 'F', Direction.DIREITA))
    
    # Verificando métodos
    print(f'Profundidade da árvore {arvore.profundidade_arvore()}')
    
    # Verificar se o método da altura do nó está correto!
    print(f'Altura do nó: {arvore.altura_no(arvore.found_index_node('A'))}')

    print(f'Altura da árvore: {arvore.altura_arvore()}')

    print(f'Nível do nó {arvore.nivel_no(arvore.found_index_node('C'))}')

    print('''
Verifação do nó''')
    
    arvore.verificar_no(arvore.found_index_node('A'))

    print(f'Nós folhas: {arvore.identify_node_sheet()}')
    print("")
    
    print("Pré Ordem: ")
    arvore.preOrdem()
    print("")
    
    print("Pós Ordem: ")
    arvore.posOrdem()
    print("")
    
    print("In Ordem: ")
    arvore.inOrdem()
    print("")
    print("")
    
    arvore.imprimir_hierarquia()
    
    arvore.imprimir()
    
    
    
    # Testes antigos:
    # arvore = ArvoreBinaria()
    # arvore.adicionar('RAIZ', 'A')
    # arvore.adicionar('RAIZ', 'B')
    # arvore.adicionar('A', 'C')
    # arvore.adicionar('A', 'D')
    # arvore.adicionar('B', 'E')
    # arvore.adicionar('B', 'F')
    
    # print(arvore.identify_node_sheet())
    # arvore.imprimir_hierarquia()
    
    # arvore.imprimir()

    # print("\nProfundidade da árvore:", arvore.profundidade_arvore())
    # print("Altura do nó 'A':", arvore.altura_no('A'))
    # print("Altura da árvore:", arvore.altura_arvore())
    # print("Nível do nó 'D':", arvore.nivel_no('D'))
    # arvore.verificar_no('C')