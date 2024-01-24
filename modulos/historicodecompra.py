
from PyQt5.QtWidgets import QDialog
from template.historicodecompra import Ui_Compra


class PaginaHistorico(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaHistorico, self).__init__(*args, **argvs)
        self.ui = Ui_Compra()
        self.ui.setupUi(self)
        self.ui.botao_inicio.clicked.connect(self.voltar_inicio)
        self.tela_inicial = tela_inicial

    def voltar_inicio(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()
