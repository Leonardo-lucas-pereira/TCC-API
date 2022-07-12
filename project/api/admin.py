from django.contrib import admin
from api.models import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Usuario, UserAdmin)
