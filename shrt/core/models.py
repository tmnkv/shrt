from django.db import models
from django.utils.timezone import now


class URL(models.Model):
    created = models.DateTimeField(
        default=now,
        verbose_name='Время и дата создания',
        editable=False
    )

    primary= models.URLField(
        verbose_name='Начальный URL'
    )

    shorten= models.URLField(
        verbose_name='Сокращенный URL'
    )

    counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество переходов'
    )

    def counter_plus(self):
        self.counter += 1
        self.save()

    def __str__(self):
        return '{0} => {1}'.format(
            self.shorten,
            self.primary
        )


    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ['-counter']