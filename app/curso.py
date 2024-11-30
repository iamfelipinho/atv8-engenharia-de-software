class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.__professor = None
        self.__alunos = []

    def get_nome(self):
        return self.__nome

    def adicionar_professor(self, professor):
        self.__professor = professor

    def remover_professor(self):
        self.__professor = None

    def get_professor(self):
        return self.__professor

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def remover_aluno(self, matricula):
        self.__alunos = [aluno for aluno in self.__alunos if aluno.get_matricula() != matricula]

    def listar_alunos(self):
        return [aluno.get_nome() for aluno in self.__alunos]
