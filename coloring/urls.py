from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('index', views.index, name='new_interaction'),
    path('gallery', views.gallery, name='gallery'),
    path('template', views.template, name='template'),
    path('pony_template', views.pony_template, name='pony_template'),
]
