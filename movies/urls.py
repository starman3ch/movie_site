from django.conf.urls import url
from .views import MovieListView, MovieDetailView, ReviewDetailView


urlpatterns = [
    url(r'^$', MovieListView.as_view(), name='movie-list'),
    url(r'^movie/([0-9]+)/$', MovieDetailView.as_view(), name='movie-detail'),
    url(r'^review/([0-9]+)/$', ReviewDetailView.as_view(), name='review-detail'),
]