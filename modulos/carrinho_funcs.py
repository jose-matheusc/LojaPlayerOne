import json
import os


def get_carrinho():
    session_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'sessao.json')
    with open(session_file_path, 'r') as session_file:
        session = json.load(session_file)

    usuarios_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'usuarios.json')
    with open(usuarios_file_path, 'r') as usuarios_file:
        usuarios = json.load(usuarios_file)

    for user in usuarios:
        if user['id'] == session['id']:
            return user['carrinho']

    return []


def add_to_carrinho(id):
    session_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'sessao.json')
    with open(session_file_path, 'r') as session_file:
        session = json.load(session_file)
    if session['id'] is None:
        return

    usuarios_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'usuarios.json')
    with open(usuarios_file_path, 'r') as usuarios_file:
        usuarios = json.load(usuarios_file)

    items_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'itens.json')
    with open(items_file_path, 'r') as items_file:
        items = json.load(items_file)

    item_a_ser_adicionado = next(
        (item for item in items if item['id'] == id), None
    )

    if item_a_ser_adicionado is None:
        return

    for user in usuarios:
        if user['id'] == session['id']:
            achou = False
            for item in user['carrinho']:
                if item['id'] == id:
                    item['quantidade'] += 1
                    achou = True
                    break
            if not achou:
                user['carrinho'].append({
                    'id': item_a_ser_adicionado['id'],
                    'nome': item_a_ser_adicionado['nome'],
                    'imagem': item_a_ser_adicionado['imagem'],
                    'preco': item_a_ser_adicionado['preco'],
                    'quantidade': 1
                })
            break

    with open(usuarios_file_path, 'w') as usuarios_file:
        json.dump(usuarios, usuarios_file)


def save_carrinho(carrinho):
    session_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'sessao.json')
    with open(session_file_path, 'r') as session_file:
        session = json.load(session_file)

    usuarios_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'usuarios.json')
    with open(usuarios_file_path, 'r') as usuarios_file:
        usuarios = json.load(usuarios_file)

    for user in usuarios:
        if user['id'] == session['id']:
            user['carrinho'] = carrinho
            break

    with open(usuarios_file_path, 'w') as usuarios_file:
        json.dump(usuarios, usuarios_file)


def limpar_carrinho():
    session_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'sessao.json')
    with open(session_file_path, 'r') as session_file:
        session = json.load(session_file)

    usuarios_file_path = os.path.join(
        os.path.dirname(__file__), '..', 'db', 'usuarios.json')
    with open(usuarios_file_path, 'r') as usuarios_file:
        usuarios = json.load(usuarios_file)

    for user in usuarios:
        if user['id'] == session['id']:
            user['carrinho'] = []
            break

    with open(usuarios_file_path, 'w') as usuarios_file:
        json.dump(usuarios, usuarios_file)


def get_sub_total():
    carrinho = get_carrinho()
    if len(carrinho) > 0:
        return sum(item['preco'] * item['quantidade'] for item in carrinho)
    return 0


def get_total():
    subtotal = get_sub_total()
    if subtotal >= 130:
        return subtotal * 0.8
    return subtotal
