from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def glossary(request):
    return render(request, 'glossary.html')
