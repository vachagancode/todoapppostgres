from django.forms import ModelForm
from .models import Todo

class TodoCreationForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']