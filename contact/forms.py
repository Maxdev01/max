from django import forms
from contact.models import ContactModel

class ContactForm(forms.ModelForm):

	class Meta:
		model = ContactModel
		fields = ('nom' , 'email' , 'message')
		widgets = {
		'nom': forms.TextInput(attrs={'class':'input'}),
		'email': forms.EmailInput(attrs={'class':'input'}),
		'message': forms.Textarea(attrs={'class':'input'})
		}