from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return render (request, 'home.html',{'name':'Dixon Andres Calderon ortega'})
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})
# Create your views here.


def about(request):
    return HttpResponse('<h1>Welcome to About Page </h1>')