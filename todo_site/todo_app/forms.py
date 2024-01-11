from django import forms
from django.forms import ModelForm
from .models import Todo, Todos

class TodoFrom(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class todoForm(ModelForm):
    class Meta:
        model = Todos
        fields = ['title']