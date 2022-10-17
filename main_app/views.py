from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
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
