# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testeInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_titulo = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_titulo.setGeometry(QtCore.QRect(100, 410, 101, 31))
        self.textEdit_titulo.setObjectName("textEdit_titulo")
        self.textEdit_autor = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_autor.setGeometry(QtCore.QRect(220, 410, 101, 31))
        self.textEdit_autor.setObjectName("textEdit_autor")
        self.textEdit_editora = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_editora.setGeometry(QtCore.QRect(340, 410, 101, 31))
        self.textEdit_editora.setObjectName("textEdit_editora")
        self.textEdit_ano = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ano.setGeometry(QtCore.QRect(460, 410, 101, 31))
        self.textEdit_ano.setObjectName("textEdit_ano")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(120, 390, 60, 17))
        self.label_titulo.setObjectName("label_titulo")
        self.label_autor = QtWidgets.QLabel(self.centralwidget)
        self.label_autor.setGeometry(QtCore.QRect(250, 390, 60, 17))
        self.label_autor.setObjectName("label_autor")
        self.label_editora = QtWidgets.QLabel(self.centralwidget)
        self.label_editora.setGeometry(QtCore.QRect(360, 390, 60, 17))
        self.label_editora.setObjectName("label_editora")
        self.label_ano = QtWidgets.QLabel(self.centralwidget)
        self.label_ano.setGeometry(QtCore.QRect(480, 390, 60, 17))
        self.label_ano.setObjectName("label_ano")
        self.textEdit_edicao = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_edicao.setGeometry(QtCore.QRect(580, 410, 101, 31))
        self.textEdit_edicao.setObjectName("textEdit_edicao")
        self.label_edicao = QtWidgets.QLabel(self.centralwidget)
        self.label_edicao.setGeometry(QtCore.QRect(600, 390, 60, 17))
        self.label_edicao.setObjectName("label_edicao")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 520, 466, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_inserir = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_inserir.setObjectName("pushButton_inserir")
        self.horizontalLayout.addWidget(self.pushButton_inserir)
        self.pushButton_alterar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_alterar.setObjectName("pushButton_alterar")
        self.horizontalLayout.addWidget(self.pushButton_alterar)
        self.pushButton_buscar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.horizontalLayout.addWidget(self.pushButton_buscar)
        self.pushButton_excluir = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout.addWidget(self.pushButton_excluir)
        self.textEdit_titulo_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_titulo_2.setGeometry(QtCore.QRect(340, 460, 101, 31))
        self.textEdit_titulo_2.setObjectName("textEdit_titulo_2")
        self.label_titulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_2.setGeometry(QtCore.QRect(290, 470, 41, 17))
        self.label_titulo_2.setObjectName("label_titulo_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(110, 30, 561, 291))
        self.listView.setObjectName("listView")
        self.pushButton_atualizar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atualizar.setGeometry(QtCore.QRect(680, 280, 88, 33))
        self.pushButton_atualizar.setObjectName("pushButton_atualizar")
        self.label_aviso = QtWidgets.QLabel(self.centralwidget)
        self.label_aviso.setGeometry(QtCore.QRect(120, 340, 541, 31))
        self.label_aviso.setText("")
        self.label_aviso.setObjectName("label_aviso")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titulo.setText(_translate("MainWindow", "Título"))
        self.label_autor.setText(_translate("MainWindow", "Autor"))
        self.label_editora.setText(_translate("MainWindow", "Editora"))
        self.label_ano.setText(_translate("MainWindow", "Ano"))
        self.label_edicao.setText(_translate("MainWindow", "Edição"))
        self.pushButton_inserir.setText(_translate("MainWindow", "Inserir"))
        self.pushButton_alterar.setText(_translate("MainWindow", "Aterar"))
        self.pushButton_buscar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_excluir.setText(_translate("MainWindow", "Excluir"))
        self.label_titulo_2.setText(_translate("MainWindow", "Opção"))
        self.pushButton_atualizar.setText(_translate("MainWindow", "Atualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
