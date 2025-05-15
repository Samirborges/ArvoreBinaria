from ArvoreBinaria import ArvoreBinaria
from Celula import Celula, Direction

class ArvoreAVL(ArvoreBinaria):
    def balanceamento(self, father_node):
        if father_node == None: return 0
        
        # Capturando o nó pai
        try:
            father_node = self.found_index_node(father_node)
        except:
            father_node = self.found_index_node(father_node.content)
        
        
        print(f'Analisando o nó: {father_node}')
        
        lista_filhos = father_node.nodes_children
        # Pegando a direção dos nós 
        filho_esquerdo = next((filho for filho in lista_filhos if filho.direction == Direction.ESQUERDA), 0)
        filho_direito = next((filho for filho in lista_filhos if filho.direction == Direction.DIREITA), 0)
        
        
        # Encontrar a altura dos nós filhos
        altura_filho_esquerdo = self.altura_no(filho_esquerdo) if isinstance(filho_esquerdo, Celula) == True else 0
        altura_filho_direito = self.altura_no(filho_direito) if isinstance(filho_direito, Celula) == True else 0
        
        peso = altura_filho_esquerdo - altura_filho_direito
        
        print(f'Altura do nó esquerdo: {altura_filho_esquerdo}')
        print(f'Altura do nó direito: {altura_filho_direito}')
        print(f'Peso: {peso}')
        
        if -1 <= peso <= 1:
            print('Árvore Balanceada')
        else:
            print('Árvore desbalanceada!')
            direcao_balanceamento = Direction.DIREITA if peso > 0 else Direction.ESQUERDA
                        
            if father_node.direction == Direction.RAIZ: # Faz o balanceamento mudando a raiz
                
                new_children = father_node
                
                if direcao_balanceamento == Direction.DIREITA:
                    # Definindo a nova raiz
                    
                    filho_a_balancear = filho_esquerdo if direcao_balanceamento == Direction.DIREITA else filho_direito
                    
                    nova_raiz = filho_a_balancear
                    nova_raiz.direction = Direction.RAIZ
                    self.RAIZ = nova_raiz
                    
                    print(new_children)
                    new_children.direction = direcao_balanceamento
                    new_children.node_father = self.RAIZ
                    
                    # Removendo o antigo nó filho
                    if filho_a_balancear in new_children.nodes_children: new_children.nodes_children.remove(filho_a_balancear)
                    
                    return
                
            # Balanceamento de nós normais
            print('Direção Balanceamento', direcao_balanceamento)
            filho_a_balancear = filho_direito if direcao_balanceamento == Direction.ESQUERDA else filho_esquerdo
            
            print('Direção do nó a balancear: ', filho_a_balancear.direction)
            
            novo_no_pai = filho_a_balancear
            
            new_children = father_node
            new_children.direction = direcao_balanceamento
            
            print(f'Nova direção do antigo nó pai: {new_children.direction.value}')

            # Adicionando o novo nó pai do novo_pai
            novo_no_pai.node_father = new_children.node_father
            
            # Adicionando o filho no avo
            no_avo = new_children.node_father
            
            no_avo.nodes_children.remove(new_children)
            
            # Adicionando o novo nó filho no avo
            no_avo.nodes_children = novo_no_pai
            print('Filhos do nó avô: ', no_avo.nodes_children)
            
            # Adicionando o novo nó filho para o novo nó pai
            novo_no_pai.nodes_children = new_children
            
            # Removendo o antigo nó pai e adicionando o novo nó pai
            new_children.node_father = novo_no_pai
            
            # Removendo o no pai da lista de nos filho do antigo pai
            if novo_no_pai in new_children.nodes_children: new_children.nodes_children.remove(novo_no_pai)
                
            # Informações do novo nó pai:
            print('-'*20)
            print(novo_no_pai)
            print('Nó pai: ', novo_no_pai.node_father)
            print('Nós filhos: ', novo_no_pai.nodes_children)
            print('Direção: ', novo_no_pai.direction)
            
            print('-'*20)
            
            # Informações do antigo nó pai
            print(new_children)
            print('Nó pai: ', new_children.node_father)
            print('Nós filhos: ', new_children.nodes_children)
            print('Direção: ', new_children.direction)
            
            print('FIM DA ANALISE...')
            print('-'*30)
                
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
    # avl = ArvoreAVL('15')
    # # for valor in [27, 29]:
    # #     avl.adicionar(avl.RAIZ, Celula(None, None, f'{valor}', Direction.ESQUERDA))
    # avl.adicionar('15', Celula(None, None, '27', Direction.ESQUERDA))
    # avl.adicionar('27', Celula(None, None, '29', Direction.ESQUERDA))
    
    # no1 = avl.found_index_node('15')
    # print(f'Nó pai do 15: {no1.node_father}')
    # print(f'Nó Direção: {no1.direction}')
    
    # print('AVL 2:')
    
    # avl1 = ArvoreAVL('15')
    # avl1.adicionar('15', Celula(None, None, '27', Direction.DIREITA))
    # avl1.adicionar('27', Celula(None, None, '29', Direction.DIREITA))

    # no1 = avl1.found_index_node('15')
    # print(f'Nó pai do 15: {no1.node_father}')
    # print(f'Nó Direção: {no1.direction}')
    
    # Adicionando os nós
    avl3 = ArvoreAVL('27')
    avl3.adicionar(avl3.RAIZ, Celula(None, None, '15', Direction.ESQUERDA))
    avl3.adicionar(avl3.RAIZ, Celula(None, None, '29', Direction.DIREITA))
    avl3.adicionar('15', Celula(None, None, '16', Direction.ESQUERDA))
    avl3.adicionar('16', Celula(None, None, '17', Direction.ESQUERDA))
    avl3.adicionar('29', Celula(None, None, '13', Direction.DIREITA))
    avl3.adicionar('13', Celula(None, None, '12', Direction.DIREITA))
    
    print('-'*30)
    # Imprindo
    for node in list(avl3.Tree):
        print(avl3.verificar_no(node))
    
