from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


# List of films
class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


# Film Desc
class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})

