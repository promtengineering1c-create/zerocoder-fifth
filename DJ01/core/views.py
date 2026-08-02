from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'core/home.html')

def page_2(request):
    return render(request, 'core/page_2.html')

def page_3(request):
    return render(request, 'core/page_3.html')

def page_4(request):
    return render(request, 'core/page_4.html')

def data(request):
    return HttpResponse("Страница с данными")

def test(request):
    return HttpResponse("Страница для тестирования")
