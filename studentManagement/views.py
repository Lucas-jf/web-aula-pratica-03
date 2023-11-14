from django.shortcuts import render

from studentManagement.models import Student


def list_view(request):
    items = Student.objects.all()
    return render(request, 'list.html', {'items': items})


def list_estudantes(request):
    dados = {}
    if query:
        dados['query'] = query
        queryset = (Q(data__icontains=query))
        items = Student.objects.filter(queryset).distinct()
    else:
        items = Student.objects.all()
    dados['items'] = items
    return render(request, 'lista.html', dados)