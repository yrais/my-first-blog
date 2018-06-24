from django.db import models                #доступ к коду из других файлов
from django.utils import timezone


class Post(models.Model): #эта строка определяет нашу модель,post-название,models.Model-объектPost является
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #моделью Django должен сохранить его в БД
    title = models.CharField(max_length=200) #так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField()   #так определяется поле для неограниченно длинного текста
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(  #ссылка на другую модель
            blank=True, null=True)

    def publish(self):          #метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self):      #после вызова метода __str__() мы получим текст (строку) с заголовком записи.
        return self.title