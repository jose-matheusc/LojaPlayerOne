from PyQt5.QtWidgets import QDialog
from modulos.carrinho import PaginaCarrinho
from modulos.carrinho_funcs import add_to_carrinho
from template.paginainicial import Ui_Inicial
from template.camisas import Ui_Camisas


class PaginaCamisas(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaCamisas, self).__init__(*args, **argvs)
        self.ui = Ui_Camisas()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.ui.botao_add_camisa_branca_naruto.clicked.connect(
            lambda: add_to_carrinho(1))
        self.ui.botao_add_camisa_branca_onep.clicked.connect(
            lambda: add_to_carrinho(2))
        self.ui.botao_add_camisa_branca_simpsonss.clicked.connect(
            lambda: add_to_carrinho(3))
        self.ui.botao_add_camisa_preta_naruto.clicked.connect(
            lambda: add_to_carrinho(4))
        self.ui.botao_add_camisa_preta_onep.clicked.connect(
            lambda: add_to_carrinho(5))
        self.ui.botao_add_camisa_preta_simpsons.clicked.connect(
            lambda: add_to_carrinho(6))
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
