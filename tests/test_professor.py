import pytest
from app.professor import Professor

def test_criar_professor():
    professor = Professor("Carlos", 1)
    assert professor.get_nome() == "Carlos"
    assert professor.get_id() == 1
