import tkinter as tk
from tkinter import simpledialog, messagebox
from arquivos_arvores.ArvoreAVL import ArvoreAVL
from arquivos_arvores.Celula import Celula, Direction

class ArvoreAVLGUInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Árvore AVL - Interface Gráfica")

        # Solicita conteúdo da raiz
        raiz_content = simpledialog.askstring("Raiz", "Digite o conteúdo da raiz:")
        if not raiz_content:
            messagebox.showerror("Erro", "Raiz não definida. Encerrando aplicação.")
            root.destroy()
            return

        self.arvore = ArvoreAVL(raiz_content)

        # Botões
        botoes = [
            ("Adicionar Nó", self.adicionar_no),
            ("Mostrar Árvore", self.mostrar_arvore),
            ("Mostrar Árvore Hierárquica", self.mostrar_arvore_hierarquica),
            ("Altura do Nó", self.mostrar_altura_no),
            ("Altura da Árvore", self.mostrar_altura_arvore),
            ("Nível do Nó", self.mostrar_nivel_no),
            ("Nível da Árvore", self.mostrar_nivel_arvore),
            ("Informações do Nó", self.verificar_no),
            ("Pré-Ordem", self.pre_ordem),
            ("In-Ordem", self.in_ordem),
            ("Pós-Ordem", self.pos_ordem),
        ]

        for texto, comando in botoes:
            btn = tk.Button(root, text=texto, command=comando, width=30)
            btn.pack(pady=2)

    def adicionar_no(self):
        pai = simpledialog.askstring("Adicionar Nó", "Digite o conteúdo do nó pai:")
        if not pai: return

        novo = simpledialog.askstring("Adicionar Nó", "Digite o conteúdo do novo nó:")
        if not novo: return

        direcao = simpledialog.askstring("Direção", "Digite a direção (E ou D):")
        if direcao not in ["E", "D", "e", "d"]:
            messagebox.showerror("Erro", "Direção inválida (use E ou D).")
            return

        direcao = Direction.ESQUERDA if direcao.upper() == "E" else Direction.DIREITA

        try:
            self.arvore.adicionar(pai, Celula(None, None, novo, direcao))
            messagebox.showinfo("Sucesso", f"Nó '{novo}' adicionado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_arvore(self):
        try:
            def gerar_estrutura_hierarquica(node, filho_esquerdo_fn, filho_direito_fn, nivel=0, pos="C"):
                if node is None:
                    return ""
                esquerda = filho_esquerdo_fn(node)
                direita = filho_direito_fn(node)
                linha = " " * (6 * nivel)
                if pos == "E":
                    linha += "/-- "
                elif pos == "D":
                    linha += "\\-- "
                else:
                    linha += "    "
                linha += str(node.content) + "\n"
                estrutura = linha
                if esquerda:
                    estrutura += gerar_estrutura_hierarquica(esquerda, filho_esquerdo_fn, filho_direito_fn, nivel + 1, "E")
                if direita:
                    estrutura += gerar_estrutura_hierarquica(direita, filho_esquerdo_fn, filho_direito_fn, nivel + 1, "D")
                return estrutura

            estrutura = gerar_estrutura_hierarquica(
                self.arvore.RAIZ,
                self.arvore.filho_esquerdo,
                self.arvore.filho_direito
            )
            messagebox.showinfo("Árvore AVL", estrutura)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_arvore_hierarquica(self):
        try:
            saida = []
            for node in self.arvore.Tree.nodes:
                filhos = [f.content for f in node.nodes_children]
                saida.append(f"{node.content}: {', '.join(filhos) if filhos else 'Sem filhos'}")
            messagebox.showinfo("Árvore Hierárquica", "\n".join(saida))
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_altura_no(self):
        nome = simpledialog.askstring("Altura", "Conteúdo do nó:")
        try:
            no = self.arvore.found_index_node(nome)
            altura = self.arvore.altura_no(no)
            messagebox.showinfo("Altura", f"Altura do nó '{nome}': {altura}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_altura_arvore(self):
        try:
            h = self.arvore.altura_arvore()
            messagebox.showinfo("Altura da Árvore", f"A altura da árvore é {h}.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_nivel_no(self):
        nome = simpledialog.askstring("Nível", "Conteúdo do nó:")
        try:
            no = self.arvore.found_index_node(nome)
            nivel = self.arvore.nivel_no(no)
            messagebox.showinfo("Nível", f"O nível do nó '{nome}' é {nivel}.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_nivel_arvore(self):
        try:
            nivel = self.arvore.profundidade_arvore()
            messagebox.showinfo("Nível Máximo", f"Nível máximo da árvore: {nivel}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def verificar_no(self):
        nome = simpledialog.askstring("Verificar Nó", "Conteúdo do nó:")
        try:
            no = self.arvore.found_index_node(nome)
            info = self.arvore.verificar_no(no)
            formatado = "\n".join(f"{chave}: {valor}" for chave, valor in info.items())
            messagebox.showinfo("Informações do Nó", formatado)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def pre_ordem(self):
        percurso = self.arvore.pre_ordem()
        messagebox.showinfo("Pré-Ordem", " → ".join(percurso))

    def in_ordem(self):
        percurso = self.arvore.in_ordem()
        messagebox.showinfo("In-Ordem", " → ".join(percurso))

    def pos_ordem(self):
        percurso = self.arvore.pos_ordem()
        messagebox.showinfo("Pós-Ordem", " → ".join(percurso))


if __name__ == "__main__":
    root = tk.Tk()
    app = ArvoreAVLGUInterface(root)
    root.mainloop()
