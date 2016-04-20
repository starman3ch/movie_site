from django.contrib import admin
from .models import Movie
from .models import Theater
from .models import Director
from .models import Actor
from .models import Review

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Review)