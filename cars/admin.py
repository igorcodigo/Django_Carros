from django.contrib import admin

# Register your models here.
from cars.models import Car,Brand

# Define uma classe de interface de administração personalizada para o modelo Car, herdando de admin.ModelAdmin.
class CarAdmin(admin.ModelAdmin):
    # list_display é um atributo que especifica quais campos do modelo Car devem ser exibidos na visualização de lista da interface de administração.
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    
    # search_fields especifica quais campos devem ser pesquisáveis na interface de administração. Atualmente permite a busca pelo campo 'model' do tabela Car.
    search_fields = ('model','brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Por fim, o modelo Car é registrado no site de administração, usando a classe CarAdmin para definir sua interface de administração. Este passo torna o modelo Car acessível e gerenciável através da interface de administração do Django.
admin.site.register(Car, CarAdmin)

admin.site.register(Brand,BrandAdmin)
