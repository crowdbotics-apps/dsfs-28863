from django.contrib import admin
from .models import Profile, Contact, VerificationCode

admin.site.register(VerificationCode)
admin.site.register(Profile)
admin.site.register(Contact)

# Register your models here.
