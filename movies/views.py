from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Movie
from .forms import ReviewsForm

class MoviesVies(ListView):
    model = Movie
    movies = Movie.objects.filter(draft=False)


class MoviesDetaliVies(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/moviesingle.html', {"movie": movie})


class AddReviews(View):
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent', None))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())