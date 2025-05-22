from django.contrib import admin
from .models import Movie
class MovieAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'email_id', 'phone_number', 'movie_name', 'show_datetime', 'no_of_seats')
admin.site.register(Movie, MovieAdmin)
