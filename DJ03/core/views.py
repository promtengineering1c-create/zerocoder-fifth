from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/home.html')

def page_2(request):
    return render(request, 'core/page_2.html')

def page_3(request):
    return render(request, 'core/page_3.html')
