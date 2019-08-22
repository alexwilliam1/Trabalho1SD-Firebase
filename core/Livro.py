
class Livro:
    def __init__(self, titulo, autor, editora, ano, edicao):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.edicao = edicao

    def get_data_serializable(self):
        return self.__dict__
