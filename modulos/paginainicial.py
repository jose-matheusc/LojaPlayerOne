import os
from PyQt5.QtWidgets import QDialog
from template.paginainicial import Ui_Inicial
from template.shorts import Ui_Shorts

from modulos.shorts import PaginaShorts
from modulos.camisas import PaginaCamisas
from modulos.broches import PaginaBroches
from modulos.chapeus import PaginaChapeus
from modulos.moletons import PaginaMoletom
from modulos.carrinho import PaginaCarrinho


class paginainicial(QDialog):
    def __init__(self, tela_login, *args, **argvs):
        super(paginainicial, self).__init__(*args, **argvs)
        self.ui = Ui_Inicial()
        self.ui.setupUi(self)
        self.ui.botao_logout.clicked.connect(self.sair)
        self.ui.botao_shorts.clicked.connect(self.shorts)
        self.ui.botao_camisas.clicked.connect(self.camisas)
        self.ui.botao_acessorios.clicked.connect(self.broches)
        self.ui.botao_chapeus.clicked.connect(self.chapeus)
        self.ui.botao_moletons.clicked.connect(self.moletom)
        self.ui.botao_carrinho.clicked.connect(self.carrinho)
        self.tela_login = tela_login

    def sair(self):
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, '..', 'db', 'sessao.json'), 'w') as sessao_arquivo:
            sessao_arquivo.write('')

        self.window = self.tela_login.show()
        self.clearMask()
        self.destroy()

    def shorts(self):
        self.window = PaginaShorts(self)
        self.window.show()
        self.hide()

    def camisas(self):
        self.window = PaginaCamisas(self)
        self.window.show()
        self.hide()

    def broches(self):
        self.window = PaginaBroches(self)
        self.window.show()
        self.hide()

    def chapeus(self):
        self.window = PaginaChapeus(self)
        self.window.show()
        self.hide()

    def moletom(self):
        self.window = PaginaMoletom(self)
        self.window.show()
        self.hide()

    def carrinho(self):
        self.window = PaginaCarrinho(self)
        self.window.show()
        self.hide()
