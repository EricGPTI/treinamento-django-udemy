from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço',max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome',max_length=100)
    sobrenome = models.CharField('Sobrenome',max_length=100)
    email = models.EmailField('E-mail',max_length=100)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
