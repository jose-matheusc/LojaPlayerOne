# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historicodecompra.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Compra(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 222)
        Dialog.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 70, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.botao_inicio = QtWidgets.QPushButton(Dialog)
        self.botao_inicio.setGeometry(QtCore.QRect(140, 160, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_inicio.setFont(font)
        self.botao_inicio.setObjectName("botao_inicio")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sua compra foi finalizada"))
        self.label_2.setText(_translate("Dialog", "Obrigado pela preferência! "))
        self.botao_inicio.setText(_translate("Dialog", "Voltar para o início"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
