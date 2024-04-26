from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
                
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

@method_decorator(login_required(login_url='login'), name= 'dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

    
    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super(NewCarCreateView, self).form_valid(form)

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
@method_decorator(login_required(login_url='login'), name= 'dispatch')    
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_queryset(self):
        """ Retorna apenas o carro se o usuário logado for o criador. """
        qs = super().get_queryset()
        return qs.filter(criador=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
     
@method_decorator(login_required(login_url='login'), name= 'dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    def get_queryset(self):
        """ Retorna apenas o carro se o usuário logado for o criador. """
        qs = super().get_queryset()
        return qs.filter(criador=self.request.user)

