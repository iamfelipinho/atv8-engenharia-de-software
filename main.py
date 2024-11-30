from app.aluno import Aluno
from app.professor import Professor
from app.curso import Curso

# Criando instâncias de alunos com os nomes completos
aluno1 = Aluno("Nycolas Felix", "1001")  # Nome completo de Nycolas
aluno2 = Aluno("Felipe Matheus de Souza Alves", "1002")  # Nome completo de Felipe

# Criando instância de professor
professor1 = Professor("Luciano Andre dos Santos", "P001")

# Criando instância de curso
curso = Curso("Análise e Desenvolvimento de Sistemas")

# Associando o professor ao curso
curso.adicionar_professor(professor1)

# Adicionando os alunos ao curso
curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

# Exibindo as informações do curso
print(f"Curso: {curso.get_nome()}")
print(f"Professor responsável: {curso.get_professor().get_nome()}")
print("Alunos inscritos:")
for aluno in curso.listar_alunos():
    print(f"- {aluno}")
