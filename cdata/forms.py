# import the standard Django Forms
# from built-in library
from django import forms
from.models import Students
   
# creating a form 
class StudentForm(forms.ModelForm):
   
    class Meta:
        model=Students
        fields='__all__'
        labels={'cl':'Class','pro_img':'Profile'}
        widgets={'name':forms.TextInput(attrs=
        {'class':'form-control'}),'cl':forms.TextInput(attrs=
        {'class':'form-control'}),'roll':forms.TextInput(attrs=
        {'class':'form-control'}),
        }
        
