from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse
from .models import Movie, Review

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list'

    def get(self, request):
        movies = Movie.objects.all()
        # return HttpResponse(movies)
        context = {'movies':movies}
        return render(request, 'movies/movie_list.html', context) 


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie_detail'

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk) #Movie.objects.get(pk=pk)
        reviews = Review.objects.filter(movie_id = pk)
        context = {'movie':movie, 'reviews':reviews}
        return render(request, 'movies/movie_detail.html', context)


class ReviewDetailView(DetailView):
    model = Review

    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        context = {'review':review}
        return render(request, 'movies/review_detail.html', context)