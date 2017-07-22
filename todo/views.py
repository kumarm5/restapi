from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('hello')

def index(request):
    data = { 'status': 'hello' }
    return render(request, 'index.html', data)
    