class Node:
    def __init__(self, key, color="RED", left=None, right=None, parent=None):
        self.key = key
        self.color = color  # "RED" or "BLACK"
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"{self.key}({self.color[0]})"

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color="BLACK")  # Sentinel NIL node
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        new_node = Node(key, color="RED", left=self.NIL, right=self.NIL)
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    # Tio vermelho
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    # Tio preto
                    if node == node.parent.right:
                        # Rotação dupla à esquerda
                        node = node.parent
                        self.left_rotate(node)
                    # Rotação simples à direita
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, key):
        node = self.root
        while node != self.NIL:
            if node.key == key:
                break
            node = node.left if key < node.key else node.right
        if node == self.NIL:
            return  # Node not found

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == "BLACK":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def validate_properties(self):
        def is_red_black_tree(node):
            if node == self.NIL:
                return 1
            if node.color == "RED":
                if node.left.color == "RED" or node.right.color == "RED":
                    raise Exception("Dois vermelhos consecutivos")
            left_black_height = is_red_black_tree(node.left)
            right_black_height = is_red_black_tree(node.right)
            if left_black_height != right_black_height:
                raise Exception("Alturas pretas diferentes")
            return left_black_height + (1 if node.color == "BLACK" else 0)

        if self.root.color != "BLACK":
            raise Exception("A raiz não é preta")
        try:
            is_red_black_tree(self.root)
            return True
        except Exception as e:
            print(f"Erro de validação: {e}")
            return False

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        if node != self.NIL:
            print(indent, "`- " if last else "|- ", node, sep="")
            indent += "   " if last else "|  "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

if __name__ == '__main__':
    tree = RedBlackTree()
    for value in [10, 20, 30, 15, 25, 5, 1]:
        tree.insert(value)
    tree.print_tree()
    assert tree.validate_properties()  # Valida se tudo está correto

    tree.delete(20)
    tree.print_tree()
    assert tree.validate_properties()
