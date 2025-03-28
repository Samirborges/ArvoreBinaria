import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class ArvoreBinaria:
    Tree: nx.Graph = nx.Graph() 
       
    def __post_init__(self): self.Tree.add_node('RAIZ')   
    
    def imprimir(self):
        # O desenho do grafo não está funcionando como devia
        # nx.draw(self.Tree)
        # plt.show()
         
        # Melhorar a impressão dos nos 
        print(self.Tree.adj)
    
    def adicionar(self, node_father, node_add):
        degree_no_father = self.degree_node(node_father)
        if degree_no_father >= 2:
            print(f'O nó {node_father} já possui grau 2')
            return
        self.Tree.add_edge(node_father, node_add)

    def degree_node(self, node): 
        if node == 'RAIZ':
            return self.Tree.degree(node)
        return self.Tree.degree(node) - 1 # Descontando a conexão que ele tem do nó pai

    def degree_tree(self):
        for node in self.Tree.adj:
            # print(f'Quantidade de filhos do nó {node}: {self.degree_node(node)}')
            if self.degree_node(node) >= 2:
                return 2
            continue
        return self.degree_node('RAIZ')

    def depth_node(self, node):
        depth = len(nx.dijkstra_path(self.Tree, 'RAIZ', node)) - 1
        return depth
    

if __name__ == '__main__':
    arvore = ArvoreBinaria()
    arvore.adicionar('RAIZ','B')
    arvore.adicionar('RAIZ','C')
    arvore.adicionar('B','D')
    arvore.adicionar('B','E')
    arvore.adicionar('C','F')
    arvore.adicionar('C','G')
    
    print(nx.dijkstra_path(arvore.Tree, 'D', 'G'))
    print(arvore.depth_node('D'))
    