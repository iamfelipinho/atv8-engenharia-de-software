import pytest
from app.curso import Curso
from app.professor import Professor
from app.aluno import Aluno

def test_criar_curso():
    curso = Curso("ADS")
    assert curso.get_nome() == "ADS"

def test_associar_professor():
    curso = Curso("ADS")
    professor = Professor("Carlos", 1)
    curso.adicionar_professor(professor)
    assert curso.get_professor().get_nome() == "Carlos"

def test_gerenciar_alunos():
    curso = Curso("ADS")
    aluno1 = Aluno("João", 12345)
    aluno2 = Aluno("Maria", 67890)

    curso.adicionar_aluno(aluno1)
    curso.adicionar_aluno(aluno2)
    assert curso.listar_alunos() == ["João", "Maria"]

    curso.remover_aluno(12345)
    assert curso.listar_alunos() == ["Maria"]
