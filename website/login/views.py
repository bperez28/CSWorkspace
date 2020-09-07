from django.shortcuts import render

def index(request):
    
    return render(request, 'login/templates/login/logindisplay.html')