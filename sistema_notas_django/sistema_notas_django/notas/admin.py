from django.contrib import admin
from .models import Nota
@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'turma', 'disciplina', 'nota', 'criado_em')
    search_fields = ('aluno', 'turma', 'disciplina')
    list_filter = ('turma', 'disciplina')
