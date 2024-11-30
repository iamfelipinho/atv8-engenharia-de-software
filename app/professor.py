class Professor:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id
