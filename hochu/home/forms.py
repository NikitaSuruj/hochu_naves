from wsgiref import validate
from django import forms 
from .models import frm1, frm2, newfrm

class Firstform(forms.ModelForm):
    class Meta:
        model = frm1
        fields = ['name', 'number']
        widgets = { 
            'name': forms.TextInput(
                attrs={
                'class': 'input',
                'placeholder': 'Ваше имя',
                },
            ),
            'number': forms.NumberInput(attrs={
                'type': 'tel',
                'class': 'input',
                'placeholder': '+7 (***) *** **-**',
            }),
        }
        
        

class Secndform(forms.ModelForm):
    class Meta:
        model = frm2
        fields = ['tip', 'width', 'length','number']
        widgets = { 
            'tip': forms.Select(attrs={
                'class': 'input',
                'placeholder': 'Поликарбонат',
            }),
            'width': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Метры',
            }),
            'length': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Метры',
            }),
            'number': forms.NumberInput(attrs={
                'type': 'tel',
                'class': 'input',
                'placeholder': '+7 (***) *** **-**',
            }),
        }
        
    
class Newform(forms.ModelForm):
    class Meta:
        model = newfrm
        fields = ['name','tip', 'width', 'length','number']
        widgets = { 
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ваше имя',
            }),
            'tip': forms.Select(attrs={
                'class': 'input',
                'placeholder': 'Поликарбонат',
            }),
            'width': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Метры',
            }),
            'length': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Метры',
            }),
            'number': forms.NumberInput(attrs={
                'type': 'tel',
                'class': 'input',
                'placeholder': '+7 (***) *** **-**',
            }),
        }
        