# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_alterar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela_Alterar(object):
    def setupUi(self, Janela_Alterar):
        Janela_Alterar.setObjectName("Janela_Alterar")
        Janela_Alterar.resize(320, 240)
        self.buttonBox = QtWidgets.QDialogButtonBox(Janela_Alterar)
        self.buttonBox.setGeometry(QtCore.QRect(220, 70, 81, 71))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit_titulo = QtWidgets.QTextEdit(Janela_Alterar)
        self.textEdit_titulo.setGeometry(QtCore.QRect(70, 10, 121, 31))
        self.textEdit_titulo.setObjectName("textEdit_titulo")
        self.textEdit_autor = QtWidgets.QTextEdit(Janela_Alterar)
        self.textEdit_autor.setGeometry(QtCore.QRect(70, 50, 121, 31))
        self.textEdit_autor.setObjectName("textEdit_autor")
        self.textEdit_ano = QtWidgets.QTextEdit(Janela_Alterar)
        self.textEdit_ano.setGeometry(QtCore.QRect(70, 90, 121, 31))
        self.textEdit_ano.setObjectName("textEdit_ano")
        self.textEdit_editora = QtWidgets.QTextEdit(Janela_Alterar)
        self.textEdit_editora.setGeometry(QtCore.QRect(70, 130, 121, 31))
        self.textEdit_editora.setObjectName("textEdit_editora")
        self.label = QtWidgets.QLabel(Janela_Alterar)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Janela_Alterar)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 41, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Janela_Alterar)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 31, 17))
        self.label_3.setObjectName("label_3")
        self.textEdit_edicao = QtWidgets.QTextEdit(Janela_Alterar)
        self.textEdit_edicao.setGeometry(QtCore.QRect(70, 170, 121, 31))
        self.textEdit_edicao.setObjectName("textEdit_edicao")
        self.label_4 = QtWidgets.QLabel(Janela_Alterar)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 51, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Janela_Alterar)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 51, 17))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Janela_Alterar)
        self.buttonBox.accepted.connect(Janela_Alterar.accept)
        self.buttonBox.rejected.connect(Janela_Alterar.reject)
        QtCore.QMetaObject.connectSlotsByName(Janela_Alterar)

    def retranslateUi(self, Janela_Alterar):
        _translate = QtCore.QCoreApplication.translate
        Janela_Alterar.setWindowTitle(_translate("Janela_Alterar", "Alterar"))
        self.label.setText(_translate("Janela_Alterar", "Titulo"))
        self.label_2.setText(_translate("Janela_Alterar", "Autor"))
        self.label_3.setText(_translate("Janela_Alterar", "Ano"))
        self.label_4.setText(_translate("Janela_Alterar", "Editora"))
        self.label_5.setText(_translate("Janela_Alterar", "Edição"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela_Alterar = QtWidgets.QDialog()
    ui = Ui_Janela_Alterar()
    ui.setupUi(Janela_Alterar)
    Janela_Alterar.show()
    sys.exit(app.exec_())
