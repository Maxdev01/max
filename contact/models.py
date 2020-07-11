from django.db import models

# Create your models here.

class ContactModel(models.Model):
	"""docstring for ClassName"""
	nom = models.CharField(null=False, max_length=30)
	email = models.EmailField(null=False)
	message = models.TextField()

	def __str__(self):
		return 'message de {}'.format(self.nom)