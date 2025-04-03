import tkinter as tk
from tkinter import simpledialog, messagebox
from ArvoreBinaria import ArvoreBinaria
from Celula import Celula, Direction

class ArvoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Árvore Binária - Interface Gráfica")
        
        self.arvore = ArvoreBinaria()

        # Criando botões
        btn_adicionar = tk.Button(root, text="Adicionar Nó", command=self.adicionar_no, width=20)
        btn_adicionar.pack(pady=5)

        btn_imprimir = tk.Button(root, text="Mostrar Árvore", command=self.mostrar_arvore, width=20)
        btn_imprimir.pack(pady=5)
        
        btn_grau = tk.Button(self.root, text="Verificar Grau do Nó", command=self.verificar_grau)
        btn_grau.pack(pady=5)
        
        btn_grau_arvore = tk.Button(self.root, text="Verificar Grau da Árvore", command=self.verifica_grau_arvore)
        btn_grau_arvore.pack(pady=5)
        
        btn_profundidade_no = tk.Button(self.root, text="Verificar Profundidade do Nó", command=self.verificar_profundidade_no)
        btn_profundidade_no.pack(pady=5)
        
        btn_profundidade_arvore = tk.Button(self.root, text="Verificar Profundidade da Árvore", command=self.verificar_profundidade_arvore)
        btn_profundidade_arvore.pack(pady=5)
        
        btn_verificar_no = tk.Button(self.root, text="Verificar Nó", command=self.verificar_no)
        btn_verificar_no.pack(pady=5)
        
        btn_altura_no = tk.Button(self.root, text="Mostrar Altura do Nó", command=self.mostrar_altura_no)
        btn_altura_no.pack(pady=5)
        
        btn_altura_arvore = tk.Button(self.root, text="Mostrar Altura da Árvore", command=self.mostrar_altura_arvore)
        btn_altura_arvore.pack(pady=5)
        
        btn_nivel_no = tk.Button(self.root, text="Mostrar Nível do Nó", command=self.mostrar_nivel_no)
        btn_nivel_no.pack(pady=5)
        
        btn_nivel_arvore = tk.Button(self.root, text="Mostrar Nível da Árvore", command=self.mostrar_nivel_arvore)
        btn_nivel_arvore.pack(pady=5)
        
        btn_nos_folha = tk.Button(self.root, text="Mostrar Nós Folha", command=self.mostrar_nos_folha)
        btn_nos_folha.pack(pady=5)

        btn_imprimir_hierarquia = tk.Button(self.root, text="Mostrar Árvore Hierárquica", command=self.mostrar_arvore_hierarquica)
        btn_imprimir_hierarquia.pack(pady=5)
        
        btn_pre_ordem = tk.Button(root, text="Percurso Pré-Ordem", command=self.pre_ordem, width=20)
        btn_pre_ordem.pack(pady=5)

        btn_pos_ordem = tk.Button(root, text="Percurso Pós-Ordem", command=self.pos_ordem, width=20)
        btn_pos_ordem.pack(pady=5)

        btn_in_ordem = tk.Button(root, text="Percurso In-Ordem", command=self.in_ordem, width=20)
        btn_in_ordem.pack(pady=5)

    def adicionar_no(self):
        pai = simpledialog.askstring("Adicionar Nó", "Digite o nome do nó pai:")
        if not pai:
            return

        nome_no = simpledialog.askstring("Adicionar Nó", "Digite o nome do novo nó:")
        if not nome_no:
            return
        
        direcao = simpledialog.askstring("Adicionar Nó", "Digite a direção (E para Esquerda, D para Direita):").upper()
        if direcao not in ["E", "D"]:
            messagebox.showerror("Erro", "A direção deve ser 'E' (Esquerda) ou 'D' (Direita).")
            return
        
        direcao = Direction.ESQUERDA if direcao == "E" else Direction.DIREITA
        try:
            self.arvore.adicionar(pai, Celula(self.arvore.found_index_node(pai), None, nome_no, direcao))
            messagebox.showinfo("Sucesso", f"Nó '{nome_no}' adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_arvore(self):
        self.arvore.imprimir()
        
    def verificar_grau(self):
        no_nome = simpledialog.askstring("Verificar Grau", "Digite o nome do nó")
        
        if no_nome:
            try:
                no = self.arvore.found_index_node(no_nome)
                grau = self.arvore.degree_node(no)
                messagebox.showinfo("Grau do Nó", f'O nó "{no_nome}" tem grau {grau}')
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def verifica_grau_arvore(self):
        """Exibe o grau máximo da árvore."""
        try:
            grau_arvore = max(self.arvore.degree_node(no) for no in self.arvore.Tree.nodes)
            messagebox.showinfo("Grau da Árvore", f"O grau máximo da árvore é {grau_arvore}.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def verificar_profundidade_no(self):
        """Abre uma caixa de diálogo para inserir o nome do nó e exibe sua profundidade."""
        no_nome = simpledialog.askstring("Verificar Profundidade", "Digite o nome do nó:")

        if no_nome:
            try:
                no = self.arvore.found_index_node(no_nome)  # Busca o nó na árvore
                profundidade = self.arvore.depth_node(no)  # Calcula a profundidade
                messagebox.showinfo("Profundidade do Nó", f"O nó '{no_nome}' tem profundidade {profundidade}.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
    
    def verificar_profundidade_arvore(self):
        """Exibe a profundidade da árvore."""
        try:
            profundidade = self.arvore.profundidade_arvore()  # Chama o método de profundidade da árvore
            messagebox.showinfo("Profundidade da Árvore", f"A profundidade da árvore é {profundidade}.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def verificar_no(self):
        """Solicita o nome de um nó e exibe suas informações detalhadas na interface."""
        no_nome = simpledialog.askstring("Verificar Nó", "Digite o nome do nó:")

        if no_nome:
            try:
                no = self.arvore.found_index_node(no_nome)  # Busca o nó na árvore
                info = self.arvore.verificar_no(no)  # Obtém as informações formatadas
                messagebox.showinfo("Informações do Nó", info)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
    
    def mostrar_altura_no(self):
        """Solicita o nome de um nó e exibe sua altura."""
        no_nome = simpledialog.askstring("Altura do Nó", "Digite o nome do nó:")

        if no_nome:
            try:
                no = self.arvore.found_index_node(no_nome)  # Busca o nó na árvore
                altura = self.arvore.altura_no(no)  # Obtém a altura do nó
                messagebox.showinfo("Altura do Nó", f"A altura do nó '{no_nome}' é {altura}.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
    
    def mostrar_altura_arvore(self):
        """Exibe a altura total da árvore."""
        try:
            altura = self.arvore.altura_arvore()  # Obtém a altura da árvore
            messagebox.showinfo("Altura da Árvore", f"A altura da árvore é {altura}.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def mostrar_nivel_no(self):
        """Solicita o nome de um nó e exibe seu nível na árvore."""
        no_nome = simpledialog.askstring("Nível do Nó", "Digite o nome do nó:")

        if no_nome:
            try:
                no = self.arvore.found_index_node(no_nome)  # Busca o nó na árvore
                nivel = self.arvore.nivel_no(no)  # Obtém o nível do nó
                messagebox.showinfo("Nível do Nó", f"O nível do nó '{no_nome}' é {nivel}.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
    
    def mostrar_nivel_arvore(self):
        """Exibe o nível máximo (profundidade) da árvore."""
        try:
            nivel = self.arvore.profundidade_arvore()  # Obtém a profundidade da árvore
            messagebox.showinfo("Nível da Árvore", f"O nível máximo (profundidade) da árvore é {nivel}.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def mostrar_nos_folha(self):
        """Exibe os nós folha da árvore (nós que não possuem filhos)."""
        try:
            nos_folha = self.arvore.identify_node_sheet()  # Obtém a lista de nós folha
            if nos_folha:
                messagebox.showinfo("Nós Folha", f"Os nós folha são: {', '.join(nos_folha)}")
            else:
                messagebox.showinfo("Nós Folha", "A árvore não possui nós folha.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def mostrar_arvore_hierarquica(self):
        """Exibe a estrutura da árvore em formato hierárquico."""
        try:
            output = []
            for node in self.arvore.Tree.nodes:
                content_node = node.content
                filhos = [filho.content for filho in self.arvore.Tree.neighbors(node) 
                        if self.arvore.depth_node(filho) > self.arvore.depth_node(node)]
                output.append(f"{content_node}: {', '.join(filhos) if filhos else 'Sem filhos'}")

            hierarquia = "\n".join(output)
            messagebox.showinfo("Árvore Hierárquica", hierarquia)
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def pre_ordem(self):
        resultado = self.arvore.pre_ordem()  # Agora retorna uma lista
        messagebox.showinfo("Percurso Pré-Ordem", " -> ".join(resultado))

    def in_ordem(self):
        resultado = self.arvore.in_ordem()  # Agora retorna uma lista
        messagebox.showinfo("Percurso In-Ordem", " -> ".join(resultado))

    def pos_ordem(self):
        resultado = self.arvore.pos_ordem()  # Agora retorna uma lista
        messagebox.showinfo("Percurso Pós-Ordem", " -> ".join(resultado))

    def get_percurso(self, func):
        output = []
        func(node=self.arvore.found_index_node('RAIZ'), output=output)  # Modificamos a função para receber 'output' como lista
        return " -> ".join(output)

# Inicializando a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = ArvoreGUI(root)
    root.mainloop()
