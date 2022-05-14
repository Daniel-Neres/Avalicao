from django.db import models

# Create your models here.

class Tipo(models.Model):
    nome = models.CharField(max_length=45, null=False)

class StatusSenha(models.Model):
   nome = models.CharField(max_length=45, null=False)

class Categoria(models.Model):
    nome = models.CharField(max_length=45, null=False)

class Senha(models.Model):
     senha = models.IntegerField(null = False)
     hora_data = models.DateTimeField(null=True)
     painel_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')
     painel_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='tipo')
     painel_status_senha = models.ForeignKey(StatusSenha, on_delete=models.CASCADE, related_name='status')