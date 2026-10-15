from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    # ModelForm monta o formulário a partir dos campos do Model Nota.
    class Meta:
        model = Nota
        fields = ['aluno', 'turma', 'disciplina', 'nota', 'observacao']
        labels = {'aluno':'Nome do aluno','turma':'Turma','disciplina':'Disciplina / UC',
                  'nota':'Nota (0 a 10)','observacao':'Observação'}
        widgets = {
            'aluno': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex.: Ana Souza'}),
            'turma': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex.: TDS5'}),
            'disciplina': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex.: Programação Python'}),
            'nota': forms.NumberInput(attrs={'class':'form-control','min':'0','max':'10','step':'0.1'}),
            'observacao': forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Comentário opcional'}),
        }
    def clean_nota(self):
        # Validação para impedir notas abaixo de zero ou acima de dez.
        nota = self.cleaned_data['nota']
        if nota < 0 or nota > 10:
            raise forms.ValidationError('A nota precisa estar entre 0 e 10.')
        return nota
