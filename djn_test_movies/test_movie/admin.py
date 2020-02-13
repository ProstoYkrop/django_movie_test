from django.contrib import admin
from .models import Genre, Movie, Category, MovieShots, Actor, StarRating, Rating, Reviews


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ("title", "category", "url")
    list_display_links = ("title", )
    list_filter = ("category", "year", )
    search_fields = ("title", "category__name",)


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name",)


# Register your models here.
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(StarRating)
admin.site.register(Reviews)
