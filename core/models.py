from django.db import models


class Usuario (models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    passkey = models.CharField('Password', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.email} {self.passkey}'
