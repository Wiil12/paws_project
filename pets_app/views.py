from tkinter.tix import Form
from django.shortcuts import render, redirect
from .models import Blog, Pet
from .forms import AddPetForm, BlogForm
# Create your views here.
 
def home(request):
    return render(request, "pets_app/home.html")
 
def pets(request):
    pets = Pet.objects.all()
    return render(request, "pets_app/pets.html", {'pets': pets})

def add_pet_form(request):
    if request.method == 'POST':
        form = AddPetForm(request.POST)
        if form.is_valid():
            pet_data = form.cleaned_data
            new_pet =Pet(
                petName=pet_data['petName'],
                petAge =pet_data['petAge'],
                petBreed=pet_data['petBreed'],
                petImage= pet_data['petImage']
            )
            
            new_pet.save()
           
            print(pet_data)
            return redirect("pets")
    else:
        form = AddPetForm()
    return render(request, "pets_app/add_pet.html", {'form':form})


def create_blog(request):
    blog_form = BlogForm(request.POST)
    if request.method =="POST":
        
        if blog_form.is_valid():
            blog_data = blog_form.cleaned_data
            print(blog_data)
            
            new_blog = Blog(
                title = blog_data['title'],
                content= blog_data['content']
            )
            new_blog.save()
            
            return redirect('get_blog')
        
        else:
          blog_form
    return render (request, "pets_app/create_blog.html", {'blog_form': blog_form})


def get_blog(request):
    blog = Blog.objects.all()
    return render (request, "pets_app/blogs.html", {'blogs': blog})
