from PyQt5.QtWidgets import QDialog
from modulos.carrinho import PaginaCarrinho
from template.paginainicial import Ui_Inicial
from modulos.carrinho_funcs import add_to_carrinho
from template.chapeus import Ui_Chapeus


class PaginaChapeus(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaChapeus, self).__init__(*args, **argvs)
        self.ui = Ui_Chapeus()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.ui.botao_add_chapeu_preto_naruto.clicked.connect(
            lambda: add_to_carrinho(25))
        self.ui.botao_add_chapeu_preto_onep.clicked.connect(
            lambda: add_to_carrinho(26))
        self.ui.botao_add_chapeu_preto_simpsons.clicked.connect(
            lambda: add_to_carrinho(27))
        self.ui.botao_add_chapeu_branco_naruto.clicked.connect(
            lambda: add_to_carrinho(28))
        self.ui.botao_add_chapeu_branco_onep.clicked.connect(
            lambda: add_to_carrinho(29))
        self.ui.botao_add_chapeu_branco_simpsons.clicked.connect(
            lambda: add_to_carrinho(30))
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
