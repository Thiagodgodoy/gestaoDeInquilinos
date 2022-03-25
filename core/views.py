from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Registro
from .forms import TaskForm


@login_required
def moradores(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    inadimplente = Registro.objects.filter(done='done', user=request.user).count()
    adimplente = Registro.objects.filter(done='doing', user=request.user).count()
    (adimplente + inadimplente) == Registro.objects.filter(done='', user=request.user).count()
    total = (adimplente + inadimplente)
    if search:
        inquilinos = Registro.objects.filter(nome__icontains=search, user=request.user)
    elif filter:
        inquilinos = Registro.objects.filter(done=filter, user=request.user)

    else:
        inquilinos = Registro.objects.all().filter(user=request.user)
    return render(request, 'moradores.html',
                  {'inquilinos': inquilinos, 'inadimplente': inadimplente, 'adimplente': adimplente, 'total': total})


@login_required
def inquilinoView(request, id):
    inquilino = get_object_or_404(Registro, pk=id)
    return render(request, 'inquilino.html', {'inquilino': inquilino})


@login_required
def deletar(request, id):
    inquilino = get_object_or_404(Registro, pk=id)
    inquilino.delete()
    messages.info(request, 'Inquilino deletado com sucesso.')
    return redirect('/')


@login_required
def editar(request, id):
    inquilino = get_object_or_404(Registro, pk=id)
    form = TaskForm(instance=inquilino)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=inquilino)
        if form.is_valid():
            inquilino.save()
            return redirect('/')
        else:
            return render(request, 'editar.html', {'form': form, 'inquilino': inquilino})

    else:
        return render(request, 'editar.html', {'form': form, 'inquilino': inquilino})


@login_required
def inserir(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            inquilino = form.save(commit=False)
            inquilino.user = request.user
            inquilino.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'inserir.html', {'form': form})


@login_required
def changeStatus(request, id):
    inquilino = get_object_or_404(Registro, pk=id)

    if inquilino.done == 'doing':
        inquilino.done = 'done'
    else:
        inquilino.done = 'doing'

    inquilino.save()

    return redirect('/')

