import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("main\inicial.py")
        self.setGeometry(0, 0, 300, 300)
        self.setWindowIcon(QIcon('icones\Gamepad1.ico'))

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    