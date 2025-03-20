from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата и время')
    location = models.CharField(max_length=200, verbose_name='Место встречи')
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Организатор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='event_images/', verbose_name='Изображение', null=True, blank=True)
    participant_limit = models.PositiveIntegerField(verbose_name='Лимит участников', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')
    status = models.CharField(max_length=20, choices=[('registered', 'Зарегистрирован'), ('canceled', 'Отменил')],
                              default='registered', verbose_name='Статус')

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'

    class Meta:
        verbose_name = 'Участие'
        verbose_name_plural = 'Участия'

