from collections import namedtuple


class LivroData:
    def __init__(self, db1, key):
        self.db1 = db1
        self.key = key

    def save(self, livro):
        self.db1.child(self.key).child(self.db1.generate_key()
                                      ).set(livro.get_data_serializable())

    def find(self, key):
        data = self.db1.child(self.key).child(key).get().val()
        return namedtuple("Livro", data.keys())(*data.values())

    def remove(self, livro_key):
        self.db1.child(self.key).child(livro_key).remove()

    def update(self, key, livro):
        self.db1.child(self.key).child(key).update(
            livro.get_data_serializable())

    def list_all(self):
        livros = []
        data = self.db1.child(self.key).get()
        
        if not data.val():
            return livros

        for livro in data.each():
            aux = livro.val()
            novo_livro = namedtuple("Livro", aux.keys())(*aux.values())
            livros.append(novo_livro)

        return livros
    def on(self, fun):
        self.db1.child(self.key).stream(fun)