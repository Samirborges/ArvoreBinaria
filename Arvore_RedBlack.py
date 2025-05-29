from ArvoreAVL import ArvoreAVL
from Celula import Direction, Celula

class Arvore_RedBlack(ArvoreAVL):    
    def adicionar(self, node_father, node_add):
        super().adicionar(node_father, node_add)
        
    
# Área de testes ----------------------------------------------------------------------------------------------------------------------------
def executa_avl1():
    avl1 = Arvore_RedBlack('27')
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
    avl2 = Arvore_RedBlack('15')
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
    avl3 = Arvore_RedBlack('15')
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

