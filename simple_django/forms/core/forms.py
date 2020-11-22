from django import forms
from core.models import Group


class GroupCreateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'students': forms.widgets.CheckboxSelectMultiple()
        }
