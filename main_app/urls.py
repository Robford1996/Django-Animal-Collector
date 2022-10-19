from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='index'),
    path('animals/<int:animal_id>/', views.animals_detail, name='detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('animals/<int:pk>/update',
         views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete',
         views.AnimalDelete.as_view(), name='animals_delete'),
    path('animals/<int:animal_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('animals/<int:animal_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name='assoc_toy'),
]
