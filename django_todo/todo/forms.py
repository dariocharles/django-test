from django import forms
form .models import Item

class ItemForm(forms.Form):
    class Meta:
        model = Item
        fields = ['name', 'done']
        

