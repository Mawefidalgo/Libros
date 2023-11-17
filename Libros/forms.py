from django import forms
from .models import Libros

class LibrosForm(forms.ModelForm):
     class Meta:
         model = Libros
         fields = ['title','author', 'rating','sinopsis','created_at','update_at']