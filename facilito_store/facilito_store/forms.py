from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, 
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                   'class': 'form-control', 
                                   'id': 'username'
                                }))

    email = forms.EmailField(required=True,
                                 widget=forms.EmailInput(attrs={
                                   'class': 'form-control', 
                                   'id': 'email',
                                   'placeholder': 'micultivo@gmail.com'
                                   }))

    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))

    password2 = forms.CharField(label='Confirmar password',
                                required= True, 
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')   

        if User.objects.filter(username=username).exists() :
            raise forms.ValidationError('El username ya se encuetra en uso') 

        return username  
    
    def clean_email(self):
        email = self.cleaned_data.get('email')   

        if User.objects.filter(email=email).exists() :
            raise forms.ValidationError('El email ya se encuetra en uso') 

        return email 

    def clean(self):
        clean_data = super().clean()

        if clean_data.get('password2') != clean_data.get ('password'):
            self.add_error('password2', 'El password no concide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),


        )