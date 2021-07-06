from django.shortcuts import render

# Create your views here.

def index(request):

    name = "Dario"
    context = {
        "name" : name  
    }
    return render(request, "todo/index.html", context)