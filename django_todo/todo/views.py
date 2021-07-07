from django.shortcuts import render
from .models import Item

# Create your views here.

def index(request):

    items = Item.object.all()

    context = {
        "items" : items
    }
    
    return render(request, "todo/index.html", context)

def add_item(request):

    if request.method == "POST"

        form = ItemForm(request.post)
        if form.is_valid:
            form.save()
            return redirect("index")
            
    else:
        form = ItemForm()

    context {
        "form" : forms
    }
        
    return rnder(request, "additem.html", context)