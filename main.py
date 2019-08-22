from core.config import db1
from core.Livro import Livro
from core.LivroData import LivroData
from Interface import *
from Interface_alterar import *
import sys
from PyQt5.QtGui import QStandardItemModel,QStandardItem

livro_data = LivroData(db1, 'livros')

class Janela_Alterar(QtWidgets.QDialog, Ui_Janela_Alterar, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Janela_Alterar, self).__init__(parent)
        self.setupUi(self)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.lista()
        self.adicionar_registro()
        self.buscar_registro()
        self.remover_registro()
        self.alterar_dados()
        
    def compara(self):
        chaves = db.child("livros").shallow().get()
        key2 = self.textEdit_titulo_2.toPlainText()

        for i, v in enumerate(chaves.val()):
            if int(key2) == int(i):
                liv_ref.child(str(v)).get()

        for i in liv_ref:
            print(i)

    def lista(self):
        self.pushButton_atualizar.clicked.connect(self.atualizar)
 
    def atualizar(self):        
        livros = livro_data.list_all()

        # for l in livros:
        #     print(l.titulo)

        list = self.listView

        model = QStandardItemModel(list)
        
        i=0 
        [model.appendRow(QStandardItem(str(i)+"   Titulo: "+str(e.titulo)+"   |   Autor: "+str(e.autor))) for i, e in enumerate(livros)]
         
        list.setModel(model)
        list.show()

    def adicionar_registro(self):
        self.pushButton_inserir.clicked.connect(self.enviar)

    def enviar(self):
            livro = Livro(self.textEdit_titulo.toPlainText(), self.textEdit_autor.toPlainText(), self.textEdit_editora.toPlainText(), 
                    self.textEdit_ano.toPlainText(), self.textEdit_edicao.toPlainText())
            livro_data.save(livro)
            self.label_aviso.setText("Dados adicionados com sucesso!!")
            #print("Dados salvos com sucesso")
            self.clearText()

    def alterar_dados(self):
        self.pushButton_alterar.clicked.connect(self.abre_tela_alterar)

    def abre_tela_alterar(self):
        key = self.textEdit_titulo_2.toPlainText()
        t = Janela_Alterar()
        t.show()
        t.exec_()
        self.textEdit_titulo_2.clear()

    def buscar_registro(self):
        self.pushButton_buscar.clicked.connect(self.buscar)

    def buscar(self):
        key3 = self.textEdit_titulo_2.toPlainText()
        chaves = db1.child("livros").shallow().get()

        for i, v in enumerate(chaves.val()):
            if int(key3) == int(i):
                L = livro_data.find(str(v))

        print("\n\n-------RESULTADO DA BUSCA-------")
        print("Titulo: "+L.titulo)
        print("Autor: "+L.autor)
        print("Editora: "+L.editora)
        print("Ano: "+L.ano) 
        print("Edição: "+L.edicao)

    def remover_registro(self):
        self.pushButton_excluir.clicked.connect(self.remover)

    def remover(self):
        chaves = db1.child("livros").shallow().get()
        key = self.textEdit_titulo_2.toPlainText()

        for i, v in enumerate(chaves.val()):
            if int(key) == int(i):
                livro_data.remove(str(v))
                self.label_aviso.setText("Dados exluídos com sucesso!!")
                print("\n\n")
                print("Livro removido com sucesso!"+"\n"+"chave removida: "+v)

        self.textEdit_titulo_2.clear()
        
    def clearText(self):
        self.textEdit_titulo.clear()
        self.textEdit_edicao.clear()
        self.textEdit_ano.clear()
        self.textEdit_editora.clear()
        self.textEdit_autor.clear()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


#def message(data):
#    try:
#        livros = [[k, v] for k, v in data['data'].items()]

#        for livro in livros:
#            # key
#            print(livro[0])
#            # value
#            print(livro[1])

#    except:
#        print('Nenhum livro!')


#livro_data.on(message)

''' Listar
livros = livro_data.list_all()

for livro in livros:
    print(livro.titulo)
'''

''' CADASTRO
print('===CADASTRO LIVROS===')
titulo = str(input('Titulo: '))
autor = str(input('Autor: '))
ano = int(input('Ano: '))
paginas = int(input('Nº páginas: '))

livro = Livro(titulo, autor, ano, paginas)
livro_data.save(livro)
'''

# livro_data.remove('-LmoGvYte5p_1riGcsSf')
# livro_data.update('-LmoGvYte5p_1riGcsSf', livro)
# livro_data.find('-LmoGvYte5p_1riGcsSf')
