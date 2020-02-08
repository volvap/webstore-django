from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def discover(request):
    return render(request, 'discover.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
