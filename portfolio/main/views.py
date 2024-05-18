from django.shortcuts import render, get_object_or_404
from .models import Project,Tag

# Create your views here.

def home(request):
    projects = Project.objects.all() # this will fetch all the projects that we created this can be done because of the Object Relational Mapping of Django
    tags = Tag.objects.all()
    return render(request,"home.html",{"projects":projects, "tags":tags}) # we willl pass a dictionary which will have key value pairs for all the projects and tags to render the dynamic data
    # now what will happen is that in our home.html we will be able to access the variable python which contains all our prijects and variable tags with all the tag
    

def contact(request):
    return render(request,"contact.html")

def project(request,id):
    project = get_object_or_404(Project, pk=id) # the get_object_404 is a helper function which will look for teh model which have the key
    #in this case we are looking for the primary key which will be the id we have specified in the Project model and if it exists return it and of not will return a 404 error page\

    return render(request, "project.html", {"project":project}) # passing a project dictionary to the template
