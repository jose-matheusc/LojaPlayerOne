from PyQt5.QtWidgets import QDialog
from template.login import Ui_Login
import os
import json

from modulos.cadastro import PaginaCadastro
from modulos.paginainicial import paginainicial


class PaginaLogin(QDialog):
    def __init__(self, *args, **argvs):
        super(PaginaLogin, self).__init__(*args, **argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.botao_login.clicked.connect(self.fazer_login)
        self.ui.botao_cadastro.clicked.connect(self.cadastre_se)
        self.ui.botao_sair.clicked.connect(self.sair)

    def fazer_login(self):
        usuario = self.ui.input_usuario.text()
        senha = self.ui.input_senha.text()

        if usuario == '' or senha == '':
            # Mostrar um dialog
            return

        current_dir = os.path.dirname(__file__)
        usuarios_file_path = os.path.join(
            current_dir, '..', 'db', 'usuarios.json')
        sessao_file_path = os.path.join(current_dir, '..', 'db', 'sessao.json')

        with open(usuarios_file_path, 'r') as arquivo:
            usuarios = json.load(arquivo)
            for user in usuarios:
                if user['usuario'] == usuario and user['senha'] == senha:
                    self.window = paginainicial(self)
                    self.window.show()
                    self.hide()
                    with open(sessao_file_path, 'w') as sessao_arquivo:
                        json.dump(
                            {'id': user['id']}, sessao_arquivo)

    def cadastre_se(self):
        self.window = PaginaCadastro(self)
        self.window.show()
        self.hide()

    def sair(self):
        self.close()
        self.hide()
