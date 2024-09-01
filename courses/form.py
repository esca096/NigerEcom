from django import forms
from .models import Courses

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'