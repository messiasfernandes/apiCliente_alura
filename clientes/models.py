from django.db import models

class Cliente(models.Model):
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=60, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField()
   
    def clean(self):
          ##  self.nome = str(self.nome.upper())
            self.email= str(self.email.lower())
    def __str__(self):
        return self.nome
