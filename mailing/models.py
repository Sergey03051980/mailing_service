from django.db import models
from django.conf import settings


class Client(models.Model):
    """Модель клиента (получателя рассылки)"""
    email = models.EmailField(unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        permissions = [
            ('can_view_client', 'Может просматривать клиентов'),
        ]

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class Message(models.Model):
    """Модель сообщения для рассылки"""
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        permissions = [
            ('can_view_message', 'Может просматривать сообщения'),
        ]

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    """Модель рассылки"""
    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_COMPLETED, 'Завершена'),
    ]

    start_time = models.DateTimeField(verbose_name='Время начала')
    end_time = models.DateTimeField(verbose_name='Время окончания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CREATED, verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ('can_view_mailing', 'Может просматривать рассылки'),
            ('can_disable_mailing', 'Может отключать рассылки'),
        ]

    def __str__(self):
        return f"Рассылка #{self.id} ({self.get_status_display()})"


class MailingAttempt(models.Model):
    """Модель попытки рассылки"""
    STATUS_SUCCESS = 'success'
    STATUS_FAILED = 'failed'

    STATUS_CHOICES = [
        (STATUS_SUCCESS, 'Успешно'),
        (STATUS_FAILED, 'Не успешно'),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name='Время попытки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус')
    server_response = models.TextField(verbose_name='Ответ сервера', blank=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
        ordering = ['-attempt_time']

    def __str__(self):
        return f"Попытка {self.mailing} - {self.get_status_display()}"


from django.db import models

# Create your models here.
