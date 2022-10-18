from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# class Animal:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, type, description, age):
#         self.name = name
#         self.type = type
#         self.description = description
#         self.age = age


# animals = [
#     Animal('Rhino', 'Mammal', 'big horns', 40),
#     Animal('Turtle', 'reptile', 'hides in shell', 95),
#     Animal('bass', 'fish', 'eats', 5),
#     Animal('horse', 'mammal', 'runs', 25),
# ]


def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', {'animals': animals})


def animals_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animals/detail.html', {'animal': animal})


class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'
    success_url = '/animals/'


class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['type', 'description', 'age']


class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'


def animals_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    feeding_form = FeedingForm()
    return render(request, 'animals/detail.html', {
        'animal': animal, 'feeding_form': feeding_form
    })


def add_feeding(request, animal_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.animal_id = animal_id
        new_feeding.save()
    return redirect('detail', animal_id=animal_id)
