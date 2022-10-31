from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
li=[
    "helo","hola","chao"
]

def index(request):
    return render(request,"index.html")

def sections(request,id):
    if 1<=id<=3 :
        return HttpResponse(li[id-1])
    else:
        return HttpResponse("Notfound")
    