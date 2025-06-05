from fasthtml.common import Div, Form, Input, Button, A

def formulario_nivel_no():
    formulario = Form(
        Input(type="text", id="no", name="no", placeholder="Insira o nó"),
            
            Div(
                Button("Verificar Nível"),
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