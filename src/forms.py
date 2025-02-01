from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    optional_courses = forms.MultipleChoiceField(
        choices=[
            ('quran', 'Qur\'an'),
            ('tarbiya', 'Tarbiya'),
            ('tawhid', 'Tawhid')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Application
        fields = [
            'full_name', 'email', 'phone', 'dob', 'gender', 'category',
            'optional_courses', 'preferred_time', 'motivation',
            'profile_picture', 'certificates'
        ]
