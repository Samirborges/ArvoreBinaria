from typing import Optional
from Celula import Celula, Direction, Cor

class RedBlackTree:
    def __init__(self):
        self.raiz: Optional[Celula] = None

    def inserir(self, valor):
        novo_no = Celula(_node_father=None, content=valor)
        novo_no.cor = Cor.VERMELHO
        novo_no._direction = Direction.RAIZ

        if not self.raiz:
            self.raiz = novo_no
            self.raiz.cor = Cor.PRETO
            return

        self._inserir_recursivo(self.raiz, novo_no)
        self._ajustar_violacoes(novo_no)

    def _inserir_recursivo(self, atual: Celula, novo: Celula):
        if novo.content < atual.content:
            if len(atual._nodes_children) > 0 and atual._nodes_children[0]:
                self._inserir_recursivo(atual._nodes_children[0], novo)
            else:
                novo.node_father = atual
                novo.direction = Direction.ESQUERDA
                atual.nodes_children.insert(0, novo)
        else:
            if len(atual._nodes_children) > 1 and atual._nodes_children[1]:
                self._inserir_recursivo(atual._nodes_children[1], novo)
            else:
                novo.node_father = atual
                novo.direction = Direction.DIREITA
                if len(atual.nodes_children) == 0:
                    atual.nodes_children.append(None)  # lugar do filho esquerdo
                atual.nodes_children.append(novo)

    def _ajustar_violacoes(self, no: Celula):
        while no != self.raiz and no.node_father.cor == Cor.VERMELHO:
            pai = no.node_father
            avo = pai.node_father

            if not avo:
                break

            if pai == (avo.nodes_children[0] if len(avo.nodes_children) > 0 else None):
                tio = avo.nodes_children[1] if len(avo.nodes_children) > 1 else None

                if tio and tio.cor == Cor.VERMELHO:
                    # Caso 1: pai e tio vermelhos
                    pai.cor = Cor.PRETO
                    tio.cor = Cor.PRETO
                    avo.cor = Cor.VERMELHO
                    no = avo
                else:
                    # Caso 2 ou 3
                    if no == (pai.nodes_children[1] if len(pai.nodes_children) > 1 else None):
                        self._rotacao_esquerda(pai)
                        no = pai
                        pai = no.node_father

                    self._rotacao_direita(avo)
                    pai.cor = Cor.PRETO
                    avo.cor = Cor.VERMELHO
            else:
                tio = avo.nodes_children[0] if len(avo.nodes_children) > 0 else None

                if tio and tio.cor == Cor.VERMELHO:
                    pai.cor = Cor.PRETO
                    tio.cor = Cor.PRETO
                    avo.cor = Cor.VERMELHO
                    no = avo
                else:
                    if no == (pai.nodes_children[0] if len(pai.nodes_children) > 0 else None):
                        self._rotacao_direita(pai)
                        no = pai
                        pai = no.node_father

                    self._rotacao_esquerda(avo)
                    pai.cor = Cor.PRETO
                    avo.cor = Cor.VERMELHO

        self.raiz.cor = Cor.PRETO

    def _rotacao_esquerda(self, x: Celula):
        y = x.nodes_children[1]
        x.nodes_children[1] = y.nodes_children[0] if len(y.nodes_children) > 0 else None
        if x.nodes_children[1]:
            x.nodes_children[1].node_father = x
        y.node_father = x.node_father

        if not x.node_father:
            self.raiz = y
        elif x == (x.node_father.nodes_children[0] if len(x.node_father.nodes_children) > 0 else None):
            x.node_father.nodes_children[0] = y
        else:
            x.node_father.nodes_children[1] = y

        y.nodes_children.insert(0, x)
        x.node_father = y

    def _rotacao_direita(self, x: Celula):
        y = x.nodes_children[0]
        x.nodes_children[0] = y.nodes_children[1] if len(y.nodes_children) > 1 else None
        if x.nodes_children[0]:
            x.nodes_children[0].node_father = x
        y.node_father = x.node_father

        if not x.node_father:
            self.raiz = y
        elif x == (x.node_father.nodes_children[0] if len(x.node_father.nodes_children) > 0 else None):
            x.node_father.nodes_children[0] = y
        else:
            x.node_father.nodes_children[1] = y

        if len(y.nodes_children) == 0:
            y.nodes_children.append(x)
        else:
            y.nodes_children.insert(1, x)

        x.node_father = y

    def em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no:
            if len(no.nodes_children) > 0 and no.nodes_children[0]:
                self.em_ordem(no.nodes_children[0])
            print(f"{no.content} ({no.cor.value})", end=' ')
            if len(no.nodes_children) > 1 and no.nodes_children[1]:
                self.em_ordem(no.nodes_children[1])
                
                
if __name__ == "__main__":
    arvore = RedBlackTree()
    for valor in [10, 20, 30, 15, 25, 5]:
        arvore.inserir(valor)

    print("Em ordem:")
    arvore.em_ordem()
