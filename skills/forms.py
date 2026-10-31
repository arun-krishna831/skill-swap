from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'skill_type', 'description']

        labels = {
            'name': 'Skill to Teach or Learn',
            'skill_type': 'Skill Type',
            'description': 'Description',
        }