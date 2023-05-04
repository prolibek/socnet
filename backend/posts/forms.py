from django.forms import ModelForm
from .models import Profile

class PostCreateForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ('text')