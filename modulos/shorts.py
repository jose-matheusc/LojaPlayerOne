from PyQt5.QtWidgets import QDialog
from modulos.carrinho import PaginaCarrinho
from template.paginainicial import Ui_Inicial
from template.shorts import Ui_Shorts
from modulos.carrinho_funcs import add_to_carrinho


class PaginaShorts(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaShorts, self).__init__(*args, **argvs)
        self.ui = Ui_Shorts()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.ui.botao_add_short_preto_onep.clicked.connect(
            lambda: add_to_carrinho(7))
        self.ui.botao_add_short_preto_simpsons.clicked.connect(
            lambda: add_to_carrinho(8))
        self.ui.botao_add_short_preto_naruto.clicked.connect(
            lambda: add_to_carrinho(9))
        self.ui.botao_add_short_rosa_simpsons.clicked.connect(
            lambda: add_to_carrinho(10))
        self.ui.botao_add_short_rosa_naruto.clicked.connect(
            lambda: add_to_carrinho(11))
        self.ui.botao_add_short_rosa_onep.clicked.connect(
            lambda: add_to_carrinho(12))
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
