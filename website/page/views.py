'''
from django.shortcuts import render

# Create your views here.
#the bottom was from the video of boston
from django.http import HttpResponse
from django.template import loader
def index(request):
    template=loader.get_template('')
    return HttpResponse("<h1> Hello World!!! <h1>")
'''
from django.shortcuts import render

def index(request):
    return render(request, 'page/templates/page/index.html')