from fasthtml.common import Form, Input, Button, Label, Div, A, P
from arquivos_arvores.ArvoreAVL import ArvoreAVL

def formulario_altura_no():
    formulario = Form(
        Label("Verificar altura", id="no", name="no"),
        Input(type="text", id="no", name="no", placeholder="Insira o nó"),
        
        Div(
            Button("Verificar Altura"),
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
        action="/buscar_altura_no"
    )
    return formulario

