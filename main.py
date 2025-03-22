from BinareTree import ArvoreBinaria
tree = ArvoreBinaria()
tree.adicionar('RAIZ', 'add_teste1')
tree.adicionar('RAIZ', 'add_teste2')
tree.adicionar('add_teste1', 'add_teste3')
# tree.adicionar('add_teste1', 'add_teste4')

tree.imprimir()
# print(tree.degree_node('RAIZ'))
# print(tree.degree_node('add_teste1'))
# print(tree.degree_tree())

print(tree.depth_node('add_teste2'))


# Bug de conexão entre nós que possui conteúdos semelhantes

# tree1 = ArvoreBinaria()
# tree1.adicionar('RAIZ', 'add_teste1')
# tree1.adicionar('RAIZ', 'add_teste2')
# print(tree1.degree_tree())