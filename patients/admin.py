from django.contrib import admin

# Register your models here.

from .models import Patient, User, Note, Session

admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Session)
