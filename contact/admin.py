from django.contrib import admin
from contact.models import ContactModel
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'message', 'email',)
admin.site.register(ContactModel, ContactAdmin)