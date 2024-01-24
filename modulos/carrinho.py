from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog
from modulos.carrinho_funcs import get_carrinho, get_sub_total, get_total, save_carrinho, limpar_carrinho
from template.carrinho import Ui_Carrinho
from PyQt5 import QtCore, QtWidgets
from modulos.historicodecompra import PaginaHistorico


@dataclass
class Item:
    id: int
    image: str
    quantity: int
    price: float


class PaginaCarrinho(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaCarrinho, self).__init__(*args, **argvs)
        self.ui = Ui_Carrinho()
        self.ui.setupUi(self)
        self.tela_inicial = tela_inicial
        self.ui.button_voltar.clicked.connect(self.voltando)
        self.ui.button_finalizar.clicked.connect(self.finalize)
        self.carrinho: list[Item] = [
            Item(item['id'], item['imagem'], item['quantidade'], item['preco']) for item in get_carrinho()
        ]

        self.ui.label_subtotal.setText(
            f"Subtotal: {self.get_string_reais(get_sub_total())}")
        self.ui.label_subtotal.adjustSize()

        self.ui.label_total.setText(
            f"Total: {self.get_string_reais(get_total())}")
        self.ui.label_total.adjustSize()

        for item in self.carrinho:
            self.addItem(item)

    def refresh_ui(self):
        self.carrinho = [
            Item(item['id'], item['imagem'], item['quantidade'], item['preco']) for item in get_carrinho()
        ]

        for i in reversed(range(self.ui.vBox.count())):
            item = self.ui.vBox.itemAt(i)
            widget = item.widget()
            widget.deleteLater()

        for item in self.carrinho:
            self.addItem(item)

        self.ui.label_subtotal.setText(
            f"Subtotal: {self.get_string_reais(get_sub_total())}")
        self.ui.label_subtotal.adjustSize()

        self.ui.label_total.setText(
            f"Total: {self.get_string_reais(get_total())}")
        self.ui.label_total.adjustSize()

    def voltando(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()

    def addItem(self, item):
        item_layout_widget = QtWidgets.QWidget()

        item_layout_widget.setFixedSize(QtCore.QSize(678, 80))

        item_layout = QtWidgets.QHBoxLayout(item_layout_widget)
        item_layout.setContentsMargins(0, 0, 0, 0)

        item_image = QtWidgets.QLabel(item_layout_widget)
        item_image.setText("")
        item_image.setStyleSheet(
            f"image: url({item.image});")

        item_price = QtWidgets.QLabel(item_layout_widget)
        preco_str = f'{item.price * item.quantity:.2f}'.replace('.', ',')
        item_price.setText(f"R$ {preco_str}")
        item_price.setStyleSheet("font: 75 12pt \"Arial\";")
        item_price.setAlignment(QtCore.Qt.AlignCenter)

        item_quantity = QtWidgets.QSpinBox(item_layout_widget)
        item_quantity.setMinimum(0)
        item_quantity.setValue(item.quantity)
        item_quantity.valueChanged.connect(
            lambda value: self.on_quantity_changed(value, item.id))

        item_layout.addWidget(item_image)
        item_layout.addWidget(item_quantity)
        item_layout.addWidget(item_price)

        self.ui.vBox.addWidget(item_layout_widget)

    def on_quantity_changed(self, value, id):
        carrinho = get_carrinho()
        for item in carrinho:

            if item['id'] == id:
                if value == 0:
                    carrinho.remove(item)
                    break
                item['quantidade'] = value
                break

        save_carrinho(carrinho)

        self.refresh_ui()

    def get_string_reais(self, value):
        return 'R$ 0,00' if value is None else f'R$ {value:.2f}'.replace('.', ',')

    def finalize(self):
        limpar_carrinho()
        self.window = PaginaHistorico(self.tela_inicial)
        self.window.show()
        self.hide()
