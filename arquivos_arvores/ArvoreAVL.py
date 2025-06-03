import networkx as nx

# from ArvoreBinaria import ArvoreBinaria
# from Celula import Celula, Direction

from arquivos_arvores.ArvoreBinaria import ArvoreBinaria
from arquivos_arvores.Celula import Celula, Direction

DEBUGGER = False
def debugger(mensagem: str):
    if DEBUGGER: print(mensagem)

class ArvoreAVL(ArvoreBinaria):
    def adicionar(self, node_father, node_add):
        super().adicionar(node_father, node_add)
        debugger(f'adicionar: O nó {node_add} foi adicionado com sucesso!')
        self.balanceamento(node_add)
        debugger('-'*40)
        
    def balanceamento(self, node: Celula):
        atual = node
        while atual:
            debugger(f'balanceamento: Análisando o nó {atual}')
            fb = self.fator_balanceamento(atual)
            debugger(f'balanceamento: Fator de balanceamento: {fb}')
            if fb > 1:
                debugger(f'balanceamento: Desbalanceamento à esquerda. Rotação à direita')
                self.rotacao(atual, self.filho_esquerdo(atual), Direction.DIREITA)
                break
                
            elif fb < -1:
                debugger(f'balanceamento: Desbalanceamento à direita. Rotação à esquerda')
                self.rotacao(atual, self.filho_direito(atual), Direction.ESQUERDA)
                break
            atual = atual.node_father
        
    def fator_balanceamento(self, node: Celula):
        try:
            esq = self.filho_esquerdo(node)
            direita = self.filho_direito(node)
            altura_esq = self.altura_no(esq) if esq else 0
            altura_dir = self.altura_no(direita) if direita else 0
            
            return altura_esq - altura_dir
        
        except Exception as e:
            print('Erro ao calcular o fator de balanceamento...')
            return 0
        
    def filho_esquerdo(self, node: Celula):
        return next((filho for filho in node.nodes_children if filho.direction == Direction.ESQUERDA), None)
        
    def filho_direito(self, node: Celula):
        return next((filho for filho in node.nodes_children if filho.direction == Direction.DIREITA), None)
    
    def altura_no(self, node):
        return super().altura_no(node) + 1
    
    def rotacao(self, no_pai: Celula, no_filho: Celula, direcao_: Direction):
        no_pai_filho = no_pai
        no_filho_pai = no_filho
        
        atributos_no_pai_filho = self.get_attributes(no_pai_filho)
        atributos_no_filho_pai = self.get_attributes(no_filho_pai)
        
        # Mudando os atributos do no_filho_pai
        novo_pai = atributos_no_pai_filho[0]
        novos_filhos = atributos_no_pai_filho[1].copy()
        nova_direcao = atributos_no_filho_pai[2]
        
        no_filho_pai.node_father = novo_pai if novo_pai != None else None
        novos_filhos.remove(no_filho_pai)
        no_filho_pai.nodes_children = next((no_filho for no_filho in novos_filhos), None)
        no_filho_pai.nodes_children.pop() # Removendo o None
        
        no_filho_pai.nodes_children.append(no_pai_filho) 
        no_filho_pai.direction = nova_direcao if novo_pai != None else Direction.RAIZ
        
        if no_filho_pai.direction == Direction.RAIZ: self.RAIZ = no_filho_pai # Definindo a nova raiz caso o nó não possua pai
        
        debugger('-'*40)
        debugger('INFORMAÇÕES DO no_filho_pai')
        debugger(f'Nó {no_filho_pai.content}')
        debugger(f'Nó pai {no_filho_pai.node_father}')
        debugger(f'Nós filhos {no_filho_pai.nodes_children}')
        debugger(f'Nó direção: {no_filho_pai.direction}')
        debugger('-'*40)
        
        # Mudando os atributos do no_pai_filho
        novo_pai = atributos_no_filho_pai[0] 
        novos_filhos = atributos_no_filho_pai[1].copy() # Não deve ser colocado, pois está com os filhos do no_filhos_pai. Causando o nó com dois pais
        nova_direcao = atributos_no_filho_pai[2] # Não deve ser usado
        
        
        no_pai_filho.node_father = no_filho_pai
        no_pai_filho.nodes_children.remove(no_filho_pai)
        no_pai_filho.direction = direcao_
        
        debugger('-'*40)
        debugger('INFORMAÇÕES DO no_pai_filho')
        debugger(f'Nó {no_pai_filho.content}')
        debugger(f'Nó pai {no_pai_filho.node_father}')
        debugger(f'Nós filhos {no_pai_filho.nodes_children}')
        debugger(f'Nó direção: {no_pai_filho.direction}')
        debugger('-'*40)
        
        # Alterar o no_avo
        if no_filho_pai.node_father != None:
            no_avo = no_filho_pai.node_father
            no_avo.nodes_children.remove(no_pai_filho)
            no_avo.nodes_children.append(no_filho_pai)
            
        self.reconstrucao_arvore()
    
    def reconstrucao_arvore(self):
        # Adicionando os novos nós:
        NewGraph = nx.DiGraph()
        for no in list(self.Tree):
            filho_esquerdo = self.filho_esquerdo(no)
            filho_direito = self.filho_direito(no)
            
            if filho_esquerdo: NewGraph.add_edge(no, filho_esquerdo)
            if filho_direito: NewGraph.add_edge(no, filho_direito)
        
        self.Tree = NewGraph
        # self.imprimir_hierarquia()
        
    def get_attributes(self, node: Celula):
        no_pai = node.node_father
        nos_filhos = node.nodes_children.copy()
        no_direcao = node.direction
        
        return no_pai, nos_filhos, no_direcao
        
    def mostrar_arvore(self):
        for node in list(self.Tree):
            print(f'Node: {node.content}')
            print(f'Nó pai: {node.node_father}')
            print(f'Nós filhos: {node.nodes_children}')
            print(f'Nó direção: {node.direction}')
            print('-'*40)
        
    def verificar_no(self, node: Celula):
        return {
            'Nó': node.content,
            'Pai': node.node_father if node.node_father != None else 'Não possui',
            'Filhos': node.nodes_children,
            'Direção': node.direction.value
        }



# Área de testes ----------------------------------------------------------------------------------------------------------------------------
def executa_avl1():
    avl1 = ArvoreAVL('27')
    avl1.adicionar(avl1.found_index_node('27') , Celula(None, None, '15', Direction.ESQUERDA))
    avl1.adicionar(avl1.found_index_node('27') , Celula(None, None, '29', Direction.DIREITA))
    avl1.adicionar(avl1.found_index_node('15') , Celula(None, None, '16', Direction.ESQUERDA))
    
    # Desbalanceando a árvore
    avl1.adicionar(avl1.found_index_node('16'), Celula(None, None, '17', Direction.ESQUERDA))
    avl1.adicionar('29', Celula(None, None, '13', Direction.DIREITA))
    avl1.adicionar('13', Celula(None, None, '12', Direction.DIREITA))
    
    print('AVL 1')
    for node in list(avl1.Tree): print(avl1.verificar_no(node))
    # AVL 1:
        # {'Nó': '27', 'Pai': 'Não possui', 'Filhos': [16, 13], 'Direção': 'RAIZ'}
        # {'Nó': '15', 'Pai': 16, 'Filhos': [], 'Direção': 'Direita'}
        # {'Nó': '29', 'Pai': 13, 'Filhos': [], 'Direção': 'Esquerda'}
        # {'Nó': '16', 'Pai': 27, 'Filhos': [17, 15], 'Direção': 'Esquerda'}
        # {'Nó': '17', 'Pai': 16, 'Filhos': [], 'Direção': 'Esquerda'}
        # {'Nó': '13', 'Pai': 27, 'Filhos': [12, 29], 'Direção': 'Direita'}
        # {'Nó': '12', 'Pai': 13, 'Filhos': [], 'Direção': 'Direita'}
    
    print('Mostrar árvore')
    avl1.imprimir_hierarquia()

def executa_avl2():
    avl2 = ArvoreAVL('15')
    avl2.adicionar('15', Celula(None, None, '27', Direction.ESQUERDA))
    avl2.adicionar('27', Celula(None, None, '29', Direction.ESQUERDA))

    # Impressão
    print('AVL 2:')
    for node in list(avl2.Tree): print(avl2.verificar_no(node))
    print('-'*30)
    # AVL 2:
        # {'Nó': '15', 'Pai': 27, 'Filhos': [], 'Direção': 'Direita'}
        # {'Nó': '27', 'Pai': 'Não possui', 'Filhos': [29, 15], 'Direção': 'RAIZ'}
        # {'Nó': '29', 'Pai': 27, 'Filhos': [], 'Direção': 'Esquerda'}
    
def executa_avl3():
    avl3 = ArvoreAVL('15')
    avl3.adicionar('15', Celula(None, None, '27', Direction.DIREITA))
    avl3.adicionar('27', Celula(None, None, '29', Direction.DIREITA))
    
    # Impressão
    print('AVL 3:')
    for node in list(avl3.Tree): print(avl3.verificar_no(node))
    print('-'*30)
    # AVL 3:
        # {'Nó': '15', 'Pai': 27, 'Filhos': [], 'Direção': 'Esquerda'}
        # {'Nó': '27', 'Pai': 'Não possui', 'Filhos': [29, 15], 'Direção': 'RAIZ'}
        # {'Nó': '29', 'Pai': 27, 'Filhos': [], 'Direção': 'Direita'}
    
if __name__ == '__main__':
    executa_avl1()
    # executa_avl2()
    # executa_avl3()
