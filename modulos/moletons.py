from PyQt5.QtWidgets import QDialog
from modulos.carrinho import PaginaCarrinho
from template.paginainicial import Ui_Inicial
from modulos.carrinho_funcs import add_to_carrinho
from template.moletom import Ui_Moletons


class PaginaMoletom(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaMoletom, self).__init__(*args, **argvs)
        self.ui = Ui_Moletons()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.ui.botao_add_moletom_preto_onep.clicked.connect(
            lambda: add_to_carrinho(19))
        self.ui.botao_add_moletom_preto_simpsons.clicked.connect(
            lambda: add_to_carrinho(20))
        self.ui.botao_add_moletom_preto_naruto.clicked.connect(
            lambda: add_to_carrinho(21))
        self.ui.botao_add_moletom_branco_onep.clicked.connect(
            lambda: add_to_carrinho(22))
        self.ui.botao_add_moletom_branco_simpsons.clicked.connect(
            lambda: add_to_carrinho(23))
        self.ui.botao_add_moletom_branco_naruto.clicked.connect(
            lambda: add_to_carrinho(24))
        self.ui.botao_carrinho.clicked.connect(self.carrinho)
        self.tela_inicial = tela_inicial

    def voltando(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()

    def carrinho(self):
        self.window = PaginaCarrinho(self.tela_inicial)
        self.window.show()
        self.hide()
