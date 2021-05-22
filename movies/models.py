from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    #Категориї

    name = models.CharField("Категории", max_length=30)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=30)

    def __str__(self):
        return self.name

    class Metta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
class Actor(models.Model):
    #Актори и режиссери

    name = models.CharField("Имя", max_length=30)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name
    
    class Metta():
        verbose_name = "Актори и режиссери"
        verbose_name_plural = "Актори и режиссери"

class Genre(models.Model):
    #Жинри

    name = models.CharField("Имя", max_length=30)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=30)

    def __str__(self):
        return self.name

    class Metta():
        verbose_name = "Жинр"
        verbose_name_plural = "Жинри"

class Movie(models.Model):
    #Фільм

    title = models.CharField("Название", max_length=30)
    tagline = models.CharField("Слоган", max_length=30, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата вихода", default="2019")
    country = models.CharField("Страна", max_length=30)
    director = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actor = models.ManyToManyField(Actor, verbose_name="актери", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанри")
    world_primiere = models.DateField("Примера в мире", default=date.today)
    budget = models.PositiveIntegerField("Буджет", default=0, help_text="Укажите суму в доларах")
    fees_in_usa = models.PositiveIntegerField("Сбори в США", default=0, help_text="Укажите суму в доларах")
    fees_in_world = models.PositiveIntegerField("Сбори в мире", default=0, help_text="Укажите суму в доларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=30)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('moviesingle', kwargs={'slug':self.url})
    
    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Metta():
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"
    
class Movie_Shorts(models.Model):
    #Кадри из фільма

    title = models.CharField("Заголовок", max_length=30)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shorts/")
    movie = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Metta():
        verbose_name = "Кадр из фільма"
        verbose_name_plural = "Кадри из фільма"

class RatingStar(models.Model):
    #Звезди рейтинга

    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value
    
    class Metta():
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезди рейтинга"   

class Rating(models.Model):
    #Рейтинг

    ip = models.CharField("IP adrres", max_length=15)
    start = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фільм")    

    def __str__(self):
        return f'{self.start} - {self.movie}'
    
    class Metta():
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    #Отзиви  

    email = models.EmailField()
    name = models.CharField("Имя", max_length=30)
    taxt = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="фільм", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'
    
    class Metta():
        verbose_name = "Отзив"
        verbose_name_plural = "Отзиви"
