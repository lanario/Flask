from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)  # This is the blueprint object

# Listar todos os clientes (LIST)
@cliente_route.route('/', methods=['GET'])
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES) 

# Inserir o cliente no servidor (INSERT)
@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass  

# Renderizar um formulário para inserir um novo cliente (FORMULÁRIO)
@cliente_route.route('/new', methods=['GET'])
def form_cliente():
    return render_template('form_cliente.html') 

# Exibir detalhes de um cliente específico (OBTER)
@cliente_route.route('/<int:client_id>/dados_cliente', methods=['GET'])
def obter_cliente(client_id):
    pass  

# Formulário para editar um cliente específico (EDIT)
@cliente_route.route('/<int:client_id>/edit', methods=['GET'])
def form_edit_cliente(client_id):
    return render_template('form_edit_cliente.html')  

# Atualizar dados de um cliente específico (UPDATE)
@cliente_route.route('/<int:client_id>/update', methods=['PUT'])
def atualizar_cliente(client_id):
    pass  

# Deletar um cliente específico (DELETE)
@cliente_route.route('/<int:client_id>/delete', methods=['DELETE'])
def deletar_cliente(client_id):
    pass  
