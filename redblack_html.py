# tree_redblack_html.py

from fasthtml.common import fast_app, serve, Titled, RedirectResponse, H1, Form, Button, Div, P, Ul, Li, Style, Pre, Script, Input

# Importa a sua implementação da Árvore Red-Black
from arquivos_arvores.Arvore_RedBlack import RedBlackTree

app, routes = fast_app()

# Instância global da Árvore Red-Black
rb_tree = RedBlackTree()

# Estilo básico para a interface (opcional, pode ser expandido)
BASE_STYLE = Style("""
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f4f4;
        color: #333;
        margin: 20px;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #0056b3;
        text-align: center;
        margin-bottom: 20px;
    }
    .navbar {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    .navbar button {
        background-color: #007bff;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin: 5px;
        flex-grow: 1; /* Permite que os botões cresçam para ocupar espaço */
        max-width: 200px; /* Limita o tamanho máximo para melhor layout */
    }
    .navbar button:hover {
        background-color: #0056b3;
    }
    .message {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 15px;
        text-align: center;
    }
    .success {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    .error {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    pre {
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
        max-width: 300px;
        margin: 0 auto;
    }
    form input[type="number"], form input[type="submit"] {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ddd;
        font-size: 16px;
    }
    form input[type="submit"] {
        background-color: #28a745;
        color: white;
        cursor: pointer;
    }
    form input[type="submit"]:hover {
        background-color: #218838;
    }
""")

# Função auxiliar para exibir mensagens temporárias
def message_script(message_id="message"):
    return Script(f"""
        setTimeout(function() {{
            const msg = document.getElementById("{message_id}");
            if (msg) {{ msg.style.display = "none"; }}
        }}, 5000);
    """)

# Geração da representação textual da árvore (similar ao print_tree)
# Adaptado para capturar a saída do print_tree em uma string
def get_tree_representation():
    import io, sys
    buffer = io.StringIO()
    sys.stdout = buffer
    rb_tree.print_tree()
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

@routes("/")
def homepage(msg_type: str = None, msg_content: str = None):
    # Mensagens de feedback
    message_html = ""
    if msg_content:
        message_class = "success" if msg_type == "success" else "error"
        message_html = P(msg_content, id="message", cls=f"message {message_class}")

    tree_display = Pre(get_tree_representation()) if rb_tree.root != rb_tree.NIL else P("A árvore está vazia.")

    navbar = Div(
        Form(Button("Inserir Nó"), method="get", action="/inserir"),
        Form(Button("Remover Nó"), method="get", action="/remover"),
        Form(Button("Mostrar Árvore"), method="get", action="/"), # Recarrega a home para mostrar a árvore atualizada
        Form(Button("Validar Propriedades"), method="get", action="/validar"),
        cls="navbar"
    )

    return Titled(
        H1("Árvore Red-Black", BASE_STYLE),
        Div(
            message_html,
            navbar,
            P("Representação atual da Árvore Red-Black:"),
            tree_display,
            cls="container"
        ),
        message_script() if msg_content else ""
    )

@routes("/inserir")
def show_insert_form(error: str = None, success: str = None):
    message_html = ""
    if success:
        message_html = P(success, id="message", cls="message success")
    elif error:
        message_html = P(error, id="message", cls="message error")

    return Titled(
        H1("Inserir Nó na Árvore Red-Black", BASE_STYLE),
        Div(
            message_html,
            Form(
                Input(type="number", name="key", placeholder="Valor da Chave", required=True),
                Button("Adicionar"),
                method="post",
                action="/inserir_no"
            ),
            Form(Button("Voltar para Home"), method="get", action="/"),
            cls="container"
        ),
        message_script() if success or error else ""
    )

@routes("/inserir_no", methods=["post"])
def insert_node(key: int):
    try:
        rb_tree.insert(key)
        # Redireciona para a home com mensagem de sucesso
        return RedirectResponse(url=f"/?msg_type=success&msg_content=Nó {key} inserido com sucesso!", status_code=303)
    except Exception as e:
        # Redireciona para o formulário de inserção com mensagem de erro
        from urllib.parse import quote
        error_msg = quote(f"Erro ao inserir nó {key}: {str(e)}")
        return RedirectResponse(url=f"/inserir?error={error_msg}", status_code=303)

@routes("/remover")
def show_remove_form(error: str = None, success: str = None):
    message_html = ""
    if success:
        message_html = P(success, id="message", cls="message success")
    elif error:
        message_html = P(error, id="message", cls="message error")

    return Titled(
        H1("Remover Nó da Árvore Red-Black", BASE_STYLE),
        Div(
            message_html,
            Form(
                Input(type="number", name="key", placeholder="Valor da Chave", required=True),
                Button("Remover"),
                method="post",
                action="/remover_no"
            ),
            Form(Button("Voltar para Home"), method="get", action="/"),
            cls="container"
        ),
        message_script() if success or error else ""
    )

@routes("/remover_no", methods=["post"])
def remove_node(key: int):
    try:
        # Verifica se a chave existe antes de tentar remover para dar um feedback melhor
        # (A sua implementação de delete já lida com chave não encontrada, mas o feedback pode ser mais claro na UI)
        temp_node = rb_tree.root
        found = False
        while temp_node != rb_tree.NIL:
            if temp_node.key == key:
                found = True
                break
            temp_node = temp_node.left if key < temp_node.key else temp_node.right
        
        if not found:
             return RedirectResponse(url=f"/remover?error=Nó {key} não encontrado na árvore.", status_code=303)

        rb_tree.delete(key)
        return RedirectResponse(url=f"/?msg_type=success&msg_content=Nó {key} removido com sucesso!", status_code=303)
    except Exception as e:
        from urllib.parse import quote
        error_msg = quote(f"Erro ao remover nó {key}: {str(e)}")
        return RedirectResponse(url=f"/remover?error={error_msg}", status_code=303)

@routes("/validar")
def validate_tree():
    message_html = ""
    try:
        if rb_tree.validate_properties():
            message_html = P("✅ A árvore é válida conforme as propriedades Red-Black.", cls="message success")
        else:
            message_html = P("❌ A árvore não está válida. Verifique o console para mais detalhes.", cls="message error")
    except Exception as e:
        message_html = P(f"❌ Erro na validação: {str(e)}", cls="message error")

    return Titled(
        H1("Validação da Árvore Red-Black", BASE_STYLE),
        Div(
            message_html,
            Form(Button("Voltar para Home"), method="get", action="/"),
            cls="container"
        ),
        message_script()
    )

# Para executar a aplicação FastHTML:
# 1. Salve o código acima como `tree_redblack_html.py` (ou outro nome de sua preferência).
# 2. Certifique-se de que `Arvore_RedBlack.py` está no mesmo diretório.
# 3. Execute no terminal: `python -m uvicorn tree_redblack_html:app --reload`
# 4. Acesse `http://127.0.0.1:8000` no seu navegador.
serve()