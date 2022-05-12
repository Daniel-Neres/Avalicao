from django.shortcuts import render
from senhas.models import Senha

# Create your views here.

def index(request):
    return render(request, 'index.html', {'senhas': Senha.objects.all()})
