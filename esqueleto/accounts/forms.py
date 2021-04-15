from django import forms
from app.models import Servidor

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['username','first_name','last_name','password','email','cpf']
        widgets = {
           'password': forms.PasswordInput,
        }
    
    def __init__(self,*args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def __init__(self,*args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'



class UserEditForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['username','first_name','last_name','password','email','cpf']
        widgets = {
           'password': forms.PasswordInput,
        }
        
    
    def __init__(self,*args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "E-mail"


        
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'