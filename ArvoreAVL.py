from ArvoreBinaria import ArvoreBinaria
from Celula import Celula, Direction

DEBUGGER = False

def debugger(funcao, mensagem, comando): 
    if comando: print(f'{funcao}: {mensagem}')

class ArvoreAVL(ArvoreBinaria):
    def balanceamento(self, father_node):
        if father_node == None: return 0
        
        # Capturando o nó pai
        try:
            father_node = self.found_index_node(father_node)
        except:
            father_node = self.found_index_node(father_node.content)
        
        
        # print(f'Analisando o nó: {father_node}')
        debugger('balanceamento', f'Analisando o nó: {father_node}', DEBUGGER)
        
        lista_filhos = father_node.nodes_children
        # Pegando a direção dos nós 
        filho_esquerdo = next((filho for filho in lista_filhos if filho.direction == Direction.ESQUERDA), 0)
        filho_direito = next((filho for filho in lista_filhos if filho.direction == Direction.DIREITA), 0)
        
        
        # Encontrar a altura dos nós filhos
        altura_filho_esquerdo = self.altura_no(filho_esquerdo) if isinstance(filho_esquerdo, Celula) == True else 0
        altura_filho_direito = self.altura_no(filho_direito) if isinstance(filho_direito, Celula) == True else 0
        
        peso = altura_filho_esquerdo - altura_filho_direito
        
        # print(f'Altura do nó esquerdo: {altura_filho_esquerdo}')
        # print(f'Altura do nó direito: {altura_filho_direito}')
        # print(f'Peso: {peso}')
        
        debugger('balanceamento', f'Altura do nó esquerdo: {altura_filho_esquerdo}', DEBUGGER)
        debugger('balanceamento', f'Altura do nó direito: {altura_filho_direito}', DEBUGGER)
        debugger('balanceamento', f'Peso: {peso}', DEBUGGER)
        
        
        
        if -1 <= peso <= 1: debugger('balanceamento', f'Árvore balanceada. Peso: {peso}', DEBUGGER); print('-'*30) if DEBUGGER else 0
        else:
            debugger('balanceamento', f'Árvore desbalanceada: {peso}', DEBUGGER)
            direcao_balanceamento = Direction.DIREITA if peso > 0 else Direction.ESQUERDA
                        
            if father_node.direction == Direction.RAIZ: # Faz o balanceamento mudando a raiz
                
                new_children = father_node
                
                # Definindo a nova raiz
                filho_a_balancear = filho_esquerdo if direcao_balanceamento == Direction.DIREITA else filho_direito
                
                nova_raiz = filho_a_balancear
                nova_raiz.direction = Direction.RAIZ
                self.RAIZ = nova_raiz
                
                new_children.direction = direcao_balanceamento
                new_children.node_father = self.RAIZ
                
                # Removendo o antigo nó filho
                if filho_a_balancear in new_children.nodes_children: new_children.nodes_children.remove(filho_a_balancear)
                
                # Remoção do pai da raiz
                nova_raiz.node_father = None
                
                # Adicição do novo nó filho na lista de filhos da nova raiz
                nova_raiz.nodes_children = new_children
                
                debugger('balanceamento', f'Nova raiz: {nova_raiz}', DEBUGGER)
                debugger('balanceamento', f'{self.verificar_no(nova_raiz)}', DEBUGGER)
                
                debugger('balanceamento', '-'*30, DEBUGGER)
                debugger('balanceamento', f'Novo filho {new_children}', DEBUGGER)
                debugger('balanceamento', f'{self.verificar_no(new_children)}', DEBUGGER)
                debugger('balanceamento', '-'*30, DEBUGGER)
                
                return
               
                
            # Balanceamento de nós normais
            # print('Direção Balanceamento', direcao_balanceamento)
            debugger('balanceamento', f'Direção Balanceamento: {direcao_balanceamento}', DEBUGGER)
            
            filho_a_balancear = filho_direito if direcao_balanceamento == Direction.ESQUERDA else filho_esquerdo
            
            # print('Direção do nó a balancear: ', filho_a_balancear.direction)
            debugger('balanceamento', f'Direção do nó a balancear:  {filho_a_balancear.direction}', DEBUGGER)
            
            novo_no_pai = filho_a_balancear
            
            new_children = father_node
            new_children.direction = direcao_balanceamento
            
            # print(f'Nova direção do antigo nó pai: {new_children.direction.value}')
            debugger('balanceamento', f'Nova direção do antigo nó pai: {new_children.direction.value}', DEBUGGER)

            # Adicionando o novo nó pai do novo_pai
            novo_no_pai.node_father = new_children.node_father
            
            # Adicionando o filho no avo
            no_avo = new_children.node_father
            
            no_avo.nodes_children.remove(new_children)
            
            # Adicionando o novo nó filho no avo
            no_avo.nodes_children = novo_no_pai
            
            debugger('balanceamento', f'Filhos do nó avô: {no_avo.nodes_children}', DEBUGGER)
            
            # Adicionando o novo nó filho para o novo nó pai
            novo_no_pai.nodes_children = new_children
            
            # Removendo o antigo nó pai e adicionando o novo nó pai
            new_children.node_father = novo_no_pai
            
            # Removendo o no pai da lista de nos filho do antigo pai
            if novo_no_pai in new_children.nodes_children: new_children.nodes_children.remove(novo_no_pai)
                
            # Informações do novo nó pai e do antigo nó pai:
            for node in [novo_no_pai, new_children]:
                if DEBUGGER: print('-'*30)
                debugger('balanceamento', node, DEBUGGER)
                debugger('balanceamento', f'Nó pai: {node.node_father}', DEBUGGER)
                debugger('balanceamento', f'Nós filhos: {node.nodes_children}', DEBUGGER)
                debugger('balanceamento', f'Direção: {node.direction}', DEBUGGER)
                if DEBUGGER: print('-'*30)
            
            debugger('balanceamento', 'FIM DA ANÁLISE...', DEBUGGER)
            if DEBUGGER: print('-'*30)
                
            return
            
            
        new_father_node = father_node.node_father
        
        return self.balanceamento(new_father_node)
        

    def adicionar(self, node_father, node_add: Celula):
        # Fazer o balanceamento antes de adicionar o nó de fato na árvore.
        super().adicionar(node_father, node_add)
        
        self.balanceamento(node_father)
        
    def altura_no(self, node):
        return super().altura_no(node) + 1
    
    def realizar_balanceamento(self, peso):
        ...
        
    def verificar_no(self, node: Celula):
        return {
            'Nó': node.content,
            'Pai': node.node_father if node.node_father != None else 'Não possui',
            'Filhos': node.nodes_children,
            'Direção': node.direction.value
        }

if __name__ == "__main__":
    # Adicionando os nós
    # avl1 = ArvoreAVL('15')
    # avl1.adicionar('15', Celula(None, None, '27', Direction.ESQUERDA))
    # avl1.adicionar('27', Celula(None, None, '29', Direction.ESQUERDA))
    
    
    # avl2 = ArvoreAVL('15')
    # avl2.adicionar('15', Celula(None, None, '27', Direction.DIREITA))
    # avl2.adicionar('27', Celula(None, None, '29', Direction.DIREITA))
    
    avl3 = ArvoreAVL('27')
    avl3.adicionar(avl3.RAIZ, Celula(None, None, '15', Direction.ESQUERDA))
    avl3.adicionar(avl3.RAIZ, Celula(None, None, '29', Direction.DIREITA))
    avl3.adicionar('15', Celula(None, None, '16', Direction.ESQUERDA))
    avl3.adicionar('16', Celula(None, None, '17', Direction.ESQUERDA))
    avl3.adicionar('29', Celula(None, None, '13', Direction.DIREITA))
    avl3.adicionar('13', Celula(None, None, '12', Direction.DIREITA))
    
    # Imprindo
    # print('AVL 1:')
    # for node in list(avl1.Tree): print(avl1.verificar_no(node))
    # print('-'*30)
        # AVL 1:
        # {'Nó': '15', 'Pai': 27, 'Filhos': [], 'Direção': 'Direita'}
        # {'Nó': '27', 'Pai': 'Não possui', 'Filhos': [29, 15], 'Direção': 'RAIZ'}
        # {'Nó': '29', 'Pai': 27, 'Filhos': [], 'Direção': 'Esquerda'}
    
    # print('AVL 2:')
    # for node in list(avl2.Tree): print(avl2.verificar_no(node))
    # print('-'*30)
        # AVL 2:
        # {'Nó': '15', 'Pai': 27, 'Filhos': [], 'Direção': 'Esquerda'}
        # {'Nó': '27', 'Pai': 'Não possui', 'Filhos': [29, 15], 'Direção': 'RAIZ'}
        # {'Nó': '29', 'Pai': 27, 'Filhos': [], 'Direção': 'Direita'}
    
    print('AVL 3:')
    for node in list(avl3.Tree): print(avl3.verificar_no(node))
        # AVL 3:
        # {'Nó': '27', 'Pai': 'Não possui', 'Filhos': [16, 13], 'Direção': 'RAIZ'}
        # {'Nó': '15', 'Pai': 16, 'Filhos': [], 'Direção': 'Direita'}
        # {'Nó': '29', 'Pai': 13, 'Filhos': [], 'Direção': 'Esquerda'}
        # {'Nó': '16', 'Pai': 27, 'Filhos': [17, 15], 'Direção': 'Esquerda'}
        # {'Nó': '17', 'Pai': 16, 'Filhos': [], 'Direção': 'Esquerda'}
        # {'Nó': '13', 'Pai': 27, 'Filhos': [12, 29], 'Direção': 'Direita'}
        # {'Nó': '12', 'Pai': 13, 'Filhos': [], 'Direção': 'Direita'}
        

    