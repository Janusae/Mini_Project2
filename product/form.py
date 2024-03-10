from django import forms
from .models import Product
class Form_AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name" , "price" , "description" , "image" , ]
