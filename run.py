import sys
from PyQt5.QtWidgets import QDialog, QApplication
from modulos.login import PaginaLogin


def main():
    app = QApplication(sys.argv)
    if QDialog.Accepted:
        window = PaginaLogin()
        window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
