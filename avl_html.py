from fasthtml.common import fast_app, serve, Titled, RedirectResponse, H1, Form, Button, Div, P, Ul, Li, Style, Pre, Script
from components.title import gerador_titulo
from components.inputs_arvore_avl import gerar_formulario_avl
from arquivos_arvores.ArvoreAVL import ArvoreAVL
from arquivos_arvores.Celula import Celula, Direction
# from components.gerar_arvore import gerar_avore
from components.avl_hierarquia import avl_hierarquia
from components.formulario_altura_no import formulario_altura_no
from components.formulario_info_no import formulario_info_no
from components.formulario_nivel_no import formulario_nivel_no

app, routes = fast_app()

avl = ArvoreAVL('27')

# Função para gerar representação textual hierárquica da árvore
def gerar_estrutura_textual(no: Celula, prefixo: str = "", eh_esquerdo: bool = True):
    if no is None:
        return ""

    resultado = ""
    if no.node_father:
        marcador = "├── " if eh_esquerdo else "└── "
    else:
        marcador = ""

    resultado += prefixo + marcador + str(no.content) + "\n"

    filhos = no.nodes_children
    filhos_esquerda = [f for f in filhos if f.direction.name == "ESQUERDA"]
    filhos_direita = [f for f in filhos if f.direction.name == "DIREITA"]

    if filhos_esquerda:
        resultado += gerar_estrutura_textual(filhos_esquerda[0], prefixo + ("│   " if eh_esquerdo else "    "), True)
    if filhos_direita:
        resultado += gerar_estrutura_textual(filhos_direita[0], prefixo + ("│   " if eh_esquerdo else "    "), False)

    return resultado


@routes("/")
def homepage():
    titulo = gerador_titulo("Árvore AVL")
    # arvore = gerar_avore(avl)
    
    # Infomações da árvore
    informacoes_title = P("Informações da árvore AVL")
    lista_informacoes = [Li(f"Altura da árvore: {avl.altura_arvore()}"), 
                         Li(f"Nível máximo da árvore: {avl.profundidade_arvore()}"),
                         Li(f"Pré-Ordem: {avl.pre_ordem()}"),
                         Li(f"In-Ordem: {avl.in_ordem()}"),
                         Li(f"Pós-Ordem: {avl.pos_ordem()}"),
                         ]

    # Botões
    add = Form(Button("Adicionar Nó"), method="get", action="/adicionar_nodes")
    mostrar_hierarquia = Form(Button("Mostrar Árvore Hierarquica"), method="get", action="/mostrar_hierarquia")
    altura_no = Form(Button("Mostrar Altura Nó"), method="get", action="/mostrar_altura_no")
    info_no = Form(Button("Informações do Nó"), method="get", action="/info_no")
    mostrar_nivel_no = Form(Button("Mostrar Nível Nó"), method="get", action="/nivel_no")
    
    navbar = Div(add, mostrar_hierarquia, altura_no, info_no, mostrar_nivel_no, style="display: flex; justify-content: space-between; ")
    
    home_page = Titled(titulo, informacoes_title, Ul(*lista_informacoes), navbar)
    return home_page

@routes("/adicionar_no", methods=["post"])
def adicionar_no(no_pai: str, no_filho: str, direcao: str):
    try:
        if direcao not in ('esquerda', 'direita'):
            return RedirectResponse(url="/adicionar_nodes?erro=DirecaoInvalida", status_code=303)
        
        direction = Direction.ESQUERDA if direcao == 'esquerda' else Direction.DIREITA
        
        if no_pai:
            avl.adicionar(avl.found_index_node(no_pai), Celula(None, None, no_filho, direction))
        return RedirectResponse(url="/adicionar_nodes?sucesso=1", status_code=303)
    except Exception as e:
        return RedirectResponse(url=f"/adicionar_nodes?erro={e}", status_code=303)

@routes("/adicionar_nodes", methods=["get"])
def adicionar_nodes(sucesso: str = None, erro: str = None):
    formulario = gerar_formulario_avl()
    mensagem = ""
    script_esconder = ""
    
    if sucesso:
        mensagem = P("✅ Nó adicionado com sucesso!", id="mensagem", style="background-color: #1D2927; color: #49BC94; padding: 10px; border-radius: 5px;")
        script_esconder = Script("""
            setTimeout(function() {
                const msg = document.getElementById("mensagem");
                if (msg) { msg.style.display = "none"; }
            }, 5000);
        """)

    elif erro:
        mensagem = P(f"❌ Erro: {erro}", id="mensagem", style="background-color: #291D21; color: #FA99A4;; padding: 10px; border-radius: 5px;")
    
    return Titled(H1("Adicionar Formulário"), mensagem, formulario, script_esconder)


@routes("/mostrar_hierarquia")
def mostrar_hierarquia():
    avl_hierarquica = avl_hierarquia(avl)
    return Titled(H1("Árvore AVL - Hierarquia", avl_hierarquica, Form(Button("Voltar"), method="get", action="/")))

# Criando a árvore
@routes("/mostrar_hierarquia")
def mostrar_hierarquia():
    estrutura_textual = gerar_estrutura_textual(avl.RAIZ)
    estilo = Style("""
    pre {
        background-color: #f5f5f5;
        padding: 16px;
        font-family: monospace;
        border-radius: 8px;
        font-size: 16px;
    }
    """)
    return Titled(H1("Árvore AVL - Hierarquia"), estilo, Pre(estrutura_textual), Form(Button("Voltar"), method="get", action="/"))


altura_busca = list()
no_name = list()

@routes("/mostrar_altura_no")
def mostrar_altura_no(error: str = None):
    formulario = formulario_altura_no()
    altura_no = f'Altura do nó {no_name[0]}: {altura_busca[0]}' if len(altura_busca) > 0 else None
    
    message = None
    message_error = None
    if error: 
        message = error
        message_error = P(message, style="background-color: #291D21; padding: 12px 16px; color: #FA99A4;")
        
    altura_busca.clear()
    no_name.clear()
    
    
    return Titled(formulario, altura_no, message_error)

@routes("/buscar_altura_no", methods=["post"])
def buscar_altura_no(no: str):
    try:
        if no:
            altura_busca.append(avl.altura_no(avl.found_index_node(no)))
            no_name.append(no)
            return RedirectResponse(url="/mostrar_altura_no", status_code=303)
    except Exception as e:
        altura_busca.clear()
        no_name.clear()
        
        from urllib.parse import quote
        msg = quote(str(e))
        return RedirectResponse(url=f"/mostrar_altura_no?error={msg}", status_code=303)
    

informacoes_node = list()
@routes("/info_no")
def informacoes_no(error: str = None):
    formulario = formulario_info_no()
    
    resultado = ""
    dados = ""
    if len(informacoes_node) > 0:
        resultado = informacoes_node[0]
        dados = [Li(f'Nó: {resultado["Nó"]}'), Li(f'Pai: {resultado["Pai"]}'), Li(f'Filhos: {resultado["Filhos"]}'), Li(f'Direção: {resultado["Direção"]}')]
        
    
    informacoes_node.clear()
    message_error = ""
    if error: 
        message = error
        message_error = P(message, style="background-color: #291D21; padding: 12px 16px; color: #FA99A4; font-size: 17px; margin-top: 10px;")
    
    return Titled(H1("Informações sobre o Nó", formulario, message_error, Ul(*dados, style="font-size: 17px;")))

@routes("/buscar_no", methods=["post"])
def buscar_no(no: str):
    try:
        if no:
            informacoes_node.append((avl.verificar_no(avl.found_index_node(no))))
            return RedirectResponse(url="/info_no", status_code=303)
    except Exception as e:
        informacoes_node.clear()
        from urllib.parse import quote
        msg = quote(str(e))
        return RedirectResponse(url=f"/info_no?error={msg}", status_code=303)
    
    
@routes("/nivel_no")
def mostrar_nivel_no():
    formulario_nivel = formulario_nivel_no()
    
    return Titled(H1("Verificar Nível Nó"), formulario_nivel)
    
serve()