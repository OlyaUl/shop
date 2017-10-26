from django.shortcuts import render
from .models import Car, CarModel, Color, Specifications, Image
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from .forms import CarForm


# list view
class CarListView(ListView):
    template_name = 'cars/cars_list.html'
    model = Car
    context_object_name = 'all_cars'


# delete
class CarDelete(DeleteView):
    model = Car
    fields = ['title']
    template_name = 'cars/car_confirm_delete.html'
    success_url = '/cars/all_cars/'


# detail view
class CarDetailView(DetailView):
    template_name = 'cars/car_detail.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# create view
class CarFormView(CreateView):
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = '/Cars/all_cars/'


# update view
class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'cars/car_update_form.html'
    success_url = '/cars/all_cars/'


def index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html',
                  {'cars': cars})
