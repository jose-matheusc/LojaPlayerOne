from PyQt5.QtWidgets import QDialog
from modulos.carrinho import PaginaCarrinho
from template.paginainicial import Ui_Inicial
from template.broches import Ui_Broches
from modulos.carrinho_funcs import add_to_carrinho


class PaginaBroches(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaBroches, self).__init__(*args, **argvs)
        self.ui = Ui_Broches()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.ui.botao_add_broche_naruto.clicked.connect(
            lambda: add_to_carrinho(13))
        self.ui.botao_add_broche_onep.clicked.connect(
            lambda: add_to_carrinho(14))
        self.ui.botao_add_broche_simpsons.clicked.connect(
            lambda: add_to_carrinho(15))
        self.ui.botao_add_caneca_naruto.clicked.connect(
            lambda: add_to_carrinho(16))
        self.ui.botao_add_caneca_onep.clicked.connect(
            lambda: add_to_carrinho(17))
        self.ui.botao_add_caneca_simpsons.clicked.connect(
            lambda: add_to_carrinho(18))
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
