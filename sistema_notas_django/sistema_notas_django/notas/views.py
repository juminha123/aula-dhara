from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import NotaForm
from .models import Nota

@login_required
def lista_notas(request):
    # Busca todos os registros; o termo digitado é opcional.
    busca = request.GET.get('q', '').strip()
    notas = Nota.objects.all()
    if busca:
        # Procura o termo no nome do aluno, turma ou disciplina.
        notas = notas.filter(Q(aluno__icontains=busca) | Q(turma__icontains=busca) | Q(disciplina__icontains=busca))
    media = notas.aggregate(media=Avg('nota'))['media']
    return render(request, 'notas/lista.html', {'notas':notas, 'busca':busca, 'media':media})

@login_required
def criar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota cadastrada com sucesso.')
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/formulario.html', {'form':form, 'titulo':'Cadastrar nota'})

@login_required
def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        # instance informa ao ModelForm qual registro será atualizado.
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota atualizada com sucesso.')
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/formulario.html', {'form':form, 'titulo':'Editar nota'})

@login_required
def excluir_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        # Exclui somente após confirmação por formulário POST.
        nota.delete()
        messages.success(request, 'Nota excluída com sucesso.')
        return redirect('lista_notas')
    return render(request, 'notas/confirmar_exclusao.html', {'nota':nota})
