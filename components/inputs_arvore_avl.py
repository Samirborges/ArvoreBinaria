from fasthtml.common import Form, Input, Button, Div, A

def gerar_formulario_avl():
    formulario = Form(
        Input(type="text", name="no_pai", id="no_pai", placeholder="Conteúdo nó pai"),
        Input(type="text", name="no_filho", id="no_filho", placeholder="Conteúdo nó adicionar"),
        Input(type="text", name="direcao", id="direcao", placeholder="Direção do nó [esquerda] ou [direita]"),
        Div(
            Button("Adicionar"),
            A("Voltar", href="/", 
              style='''
              font-size: 17px;
              text-decoration: none;
              color: white;
              background-color: red;
              padding: 12px 16px;
              border-radius: 0.25rem;
              '''),
            style="display: flex; justify-content: space-between;"
        ),
        method="post",
        action="/adicionar_no"
    )
    return formulario