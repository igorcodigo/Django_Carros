from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car,CarInventory
from django.db.models import Sum
# import datetime
from openai_api.client import gerar_car_ai_bio

def car_inventory_update():
    cars_count = Car.objects.all().count() # Conta quantos objetos tem no banco de dados 
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value'] #Faz a soma do campo total_value de todos os objetos e obtem essa soma
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    ) # Cria um objeto do tipo CarInventory passando esses dois valores como parametros

def exibir_hora_da_acao(descricao): pass
    # now = datetime.datetime.now()
    # print(f"#### {descricao} às {now} ###")

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio: 
        ai_bio = gerar_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        instance.bio = ai_bio

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    exibir_hora_da_acao("Salvou o carro")
    car_inventory_update()

# ============================ Signals Delete =======================
    
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    exibir_hora_da_acao("Indo deletar o carro")

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    exibir_hora_da_acao("Deletou o carro")
    car_inventory_update()