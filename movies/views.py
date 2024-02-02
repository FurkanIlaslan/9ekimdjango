from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, "index.html")



def movies(request):

    filmler = Movie.objects.all()
    user = request.user.kullanici

    context = {
        'filmler':filmler,
        'user': user
    }

    return render(request,"browse-index.html", context)