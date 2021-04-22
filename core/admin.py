from django.contrib import admin

from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'passkey')

admin.site.register(Usuario, UsuarioAdmin)

