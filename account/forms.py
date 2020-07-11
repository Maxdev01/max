from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
   '''Formulaire pour le login.
   champs:
      username, de l'utilisateur.
      password, de l'utilisateur.
   '''
   username = forms.CharField(widget=forms.TextInput(
   attrs={'class': 'input',
      'placeholder': 'Votre pseudo'
   }))
   
   password = forms.CharField(widget=forms.PasswordInput(
   attrs={'class': 'input',
      'placeholder': 'Votre mot de passe'
   }))
   
class RegisterForm(forms.ModelForm):
   '''Formulaire pour enregister une compte. '''
   first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your firstname'}))
   last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your lastname'}))
   email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'your email'}))
   password = forms.CharField(max_length=120, widget=forms.PasswordInput(attrs={'class': 'input'}), required=True)
  
   class Meta:
      model = User
      fields = ('username', 'first_name' , 'last_name', 'email', 'password')
      widgets = {
         'username': forms.TextInput(attrs={'class': 'input'})
      }
      
   def clean_first_name(self):
      first_name = self.cleaned_data.get('first_name')
      if first_name is None:
         raise forms.ValidationError('Enter your first_name')
      return first_name

   def clean_last_name(self):
      last_name = self.cleaned_data.get('last_name')
      if last_name is None:
         raise forms.ValidationError('enter your last_name')
      return last_name


               

      
      