from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'Головна сторінка',
        'description': 'Це головна сторінка вашої нової аплікухи.'
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'title': 'Про нас',
        'description': 'Інформація про проект.'
    }
    return render(request, 'main/about.html', context)