import os
import sys
import json
import uuid
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from template.cadastro import Ui_Cadastro
from modulos.paginainicial import paginainicial


class PaginaCadastro(QDialog):
    def __init__(self, tela_login, *args, **argvs):
        super(PaginaCadastro, self).__init__(*args, **argvs)
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltar)
        self.ui.botao_cadastrar.clicked.connect(self.save_credentials)
        self.tela_login = tela_login

    def voltar(self):
        self.window = self.tela_login.show()
        self.clearMask()
        self.destroy()

    def save_credentials(self):
        username = self.ui.input_usuario.text()
        password = self.ui.input_senha.text()

        if username.strip() == '' or password.strip() == '':
            # Mostra uma mensagem de erro
            return

        # Caminhos
        current_dir = os.path.dirname(__file__)
        caminho_arquivo_usuarios = os.path.join(
            current_dir, '..', 'db', 'usuarios.json')
        caminho_arquivo_sessao = os.path.join(
            current_dir, '..', 'db', 'sessao.json')

        uuid_v4 = uuid.uuid4()

        uuid_string = str(uuid_v4)

        data = {
            "id": uuid_string,
            "usuario": username,
            "senha": password,
            "carrinho": []
        }

        usuarios = []

        # le todos os dados e envia para o dados_destino
        with open(caminho_arquivo_usuarios, "r") as json_file_destino:
            usuarios = json.load(json_file_destino)

        for user in usuarios:
            if user['usuario'] == username:
                # Mensagem de erro: usuario já existe
                return

        # Atualiza a lista de usuarios
        usuarios.append(data)

        with open(caminho_arquivo_usuarios, "w") as arquivo_usuarios:
            json.dump(usuarios, arquivo_usuarios)

        # Atualiza o id da sessao
        with open(caminho_arquivo_sessao, "w") as arquivo_sessao:
            json.dump({'id': data['id']}, arquivo_sessao)

        self.window = paginainicial(self)
        self.window.show()
        self.hide()
