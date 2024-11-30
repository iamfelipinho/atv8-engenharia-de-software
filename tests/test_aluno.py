import pytest
from app.aluno import Aluno

def test_criar_aluno():
    aluno = Aluno("João", 12345)
    assert aluno.get_nome() == "João"
    assert aluno.get_matricula() == 12345
