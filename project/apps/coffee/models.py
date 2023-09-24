from django.db import models


class Coffee(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    pictures = models.ImageField(upload_to='coffee/img', default='0.jpg')
    info = models.TextField('Описание', max_length=1000)

    def __str__(self):
        return f'{self.pk}, {self.title}, {self.description}, {self.price}, {self.info}'

    def get_absolute_url(self):
        return f'/coffee'

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'


class Feedback(models.Model):
    user = models.CharField('Пользователь', max_length=50)
    text = models.TextField('Текст отзыва')
    rating = models.IntegerField('Рейтинг')
    coffees = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='feedbacks')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"
        ordering = ['-rating']
