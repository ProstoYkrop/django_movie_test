from django.db import models
from datetime import date
from django.urls import reverse


# Movie categories and descriptions
class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Movie Genre and descriptions
class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


# Actors and Directors of films and their descriptions
class Actor(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры и режиссеры"
        verbose_name_plural = "Актёры и режиссеры"


# The name of the film, its slogan, description, release date, country, actors and Directors,
# as well as genre and box office in the United States and the world
class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    slogan = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="djntest_movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="director_film")
    actors = models.ManyToManyField(Actor, verbose_name="актёр", related_name="actor_film")
    genres = models.ManyToManyField(Genre, verbose_name="жанр")
    world_premier = models.DateField("Показ в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет фильма", default=0, help_text="Сумма в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="Сумма в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Сумма в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильмы"
        verbose_name_plural = "Фильмы"


# A frame from the movie its title description and image
class MovieShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


# Rating star
class StarRating(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звёзды рейтинга"


# Overall star rating
class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15, default=0)
    star = models.ForeignKey(StarRating, verbose_name="звезда", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


# Reviews of the film
class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"