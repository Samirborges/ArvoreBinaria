from fasthtml.common import Form, Input, Button, Div, A

def formulario_info_no():
    formulario = Form(
        Input(type="text", id="no", name="no", placeholder="Digite o conteúdo do nó"),
         Div(
            Button("Buscar"),
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
        action="/buscar_no"
    )
    
    return formulario