from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Pizzashop')
    name = models.CharField(max_length=100, verbose_name='Название пиццерии')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    logo = models.ImageField(upload_to='pizzashop_logo/', blank=False)

    class Meta:
        # Название модели в единственном и множественном числе
        verbose_name = 'Пиццерия'
        verbose_name_plural = 'Пиццерии'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    # on_delete=models.SET_NULL - мягкая связь, при удалении первичной таблицы PizzaShop, значение примет параметр NULL
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=100, verbose_name='Краткое описание')
    # ссылка на фото, путь куда грузить фото, и указал что можно грузить без фото
    photo = models.ImageField(upload_to='pizza_images/', blank=False)
    price = models.IntegerField(default=0, verbose_name='Цена')

    class Meta:
        # Название модели в единственном и множественном числе
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']  # Сортировка в админке по соответствующему полю

    def __str__(self):
        return self.name  # Возвращает в админку verbose_name из name
