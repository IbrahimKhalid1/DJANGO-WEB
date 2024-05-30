# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is my Home")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'PC.html')

def contact(request):
    return render(request,'contact.html')

def PC(request):
    return render(render,'PC.html')

def Graphiccard(request):
    return render(render,'Graphiccard.html')