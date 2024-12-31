from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name='pets'),
    path('add-pet/', views.add_pet_form, name='add_pet_form'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog/', views.get_blog, name= 'get_blog'),
]