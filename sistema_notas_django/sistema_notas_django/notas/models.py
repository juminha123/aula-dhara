from django.db import models

class Nota(models.Model):
    # Dados principais do aluno e da avaliação.
    aluno = models.CharField(max_length=120)
    turma = models.CharField(max_length=40)
    disciplina = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=4, decimal_places=1)
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['aluno', 'disciplina']

    def __str__(self):
        return f'{self.aluno} - {self.disciplina}: {self.nota}'
