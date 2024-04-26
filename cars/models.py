from django.db import models
from django.contrib.auth.models import User

# Toda alteracao nas tabelas(criacao ou alteracao) para serem efetivadas na apliacacao precisa desses dois comandos 1 para criar as migracoes e o 2 para aplicar as migracoes
# python manage.py makemigrations 
# python manage.py migrate

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    criador = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_cars', blank=True, null=True)
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    id = models.AutoField(primary_key=True)
    cars_count = models.IntegerField()
    cars_value = models.FloatField(blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # O "-" antes significa para ordenar por ordem descrescente inves de crescente

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'