import tkinter as tk
from tkinter import simpledialog, messagebox
from arquivos_arvores.Arvore_RedBlack import RedBlackTree

class RedBlackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Árvore Red-Black")

        self.arvore = RedBlackTree()

        botoes = [
            ("Inserir Nó", self.inserir_no),
            ("Remover Nó", self.remover_no),
            ("Mostrar Árvore", self.mostrar_arvore),
            ("Validar Propriedades", self.validar_arvore)
        ]

        for texto, comando in botoes:
            tk.Button(root, text=texto, width=30, command=comando).pack(pady=4)

    def inserir_no(self):
        valor = simpledialog.askinteger("Inserir", "Digite a chave do nó:")
        if valor is not None:
            self.arvore.insert(valor)
            messagebox.showinfo("Inserido", f"Nó {valor} foi inserido.")

    def remover_no(self):
        valor = simpledialog.askinteger("Remover", "Digite a chave a remover:")
        if valor is not None:
            self.arvore.delete(valor)
            messagebox.showinfo("Removido", f"Nó {valor} foi removido.")

    def mostrar_arvore(self):
        import io, sys
        buffer = io.StringIO()
        sys.stdout = buffer
        self.arvore.print_tree()
        sys.stdout = sys.__stdout__
        messagebox.showinfo("Árvore Red-Black", buffer.getvalue())

    def validar_arvore(self):
        try:
            if self.arvore.validate_properties():
                messagebox.showinfo("Validação", "✅ A árvore é válida conforme as propriedades Red-Black.")
            else:
                messagebox.showerror("Erro", "❌ A árvore não está válida.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na validação:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RedBlackGUI(root)
    root.mainloop()
