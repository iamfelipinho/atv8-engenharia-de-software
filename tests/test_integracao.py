from app.curso import Curso
from app.professor import Professor
from app.aluno import Aluno

def test_integracao_curso():
    # Criação de professor
    professor = Professor("Carlos", 1)

    # Criação de curso e associação do professor
    curso = Curso("ADS")
    curso.adicionar_professor(professor)

    # Criação de alunos
    aluno1 = Aluno("João", 12345)
    aluno2 = Aluno("Maria", 67890)
    curso.adicionar_aluno(aluno1)
    curso.adicionar_aluno(aluno2)

    # Verificar listagem de alunos e professor
    assert curso.get_professor().get_nome() == "Carlos"
    assert curso.listar_alunos() == ["João", "Maria"]

    # Remover um aluno
    curso.remover_aluno(12345)
    assert curso.listar_alunos() == ["Maria"]
